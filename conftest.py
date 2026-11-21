# Make the shared libraries importable in every test: figdata/lib (econdata,
# figout) and code/shared (country). Chapter code under code/<year>/ uses its own
# conftest if it needs more.
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent
for p in (ROOT / "figdata" / "lib", ROOT / "code" / "shared"):
    sys.path.insert(0, str(p))

# data/derived/ is not in git: tools/derive_data.py rebuilds it from the approved downloads. A fresh clone, and so
# CI, has none, and a test that reads real data cannot run there. Without the directory, a test that fails on
# econdata's "missing" message (raised in the test, or printed by a listing it runs) is reported as skipped. With
# the directory present nothing changes: every failure stays a failure.
DERIVED = ROOT / "data" / "derived"
NEEDS_DERIVED = "data/derived/ is built by tools/derive_data.py"  # the message of econdata._need


def _lacks_derived(rep, call):
    text = [str(rep.longrepr)]
    # a listing run with check=True: its traceback is in the exception's streams, not in the report
    exc = call.excinfo.value if call.excinfo else None
    for name in ("stderr", "stdout"):
        stream = getattr(exc, name, None)
        if isinstance(stream, bytes):
            stream = stream.decode(errors="replace")
        if isinstance(stream, str):
            text.append(stream)
    return any(NEEDS_DERIVED in t for t in text)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    if rep.failed and not DERIVED.exists() and _lacks_derived(rep, call):
        rep.outcome = "skipped"
        rep.longrepr = (str(item.path), item.location[1], "Skipped: needs data/derived/ (tools/derive_data.py)")


# A figdata test imports its chapter's make_*.py by module name (import mode is importlib, so the test's own directory
# is not on sys.path by default). Put each collected test file's directory first on sys.path. tools/figdata.sh runs one
# chapter directory per process, so modules of the same name in two chapters never meet.
def pytest_collect_file(file_path, parent):
    if file_path.suffix == ".py" and file_path.name.startswith("test_") and "figdata" in file_path.parts:
        d = str(file_path.parent)
        if d not in sys.path:
            sys.path.insert(0, d)
    return None

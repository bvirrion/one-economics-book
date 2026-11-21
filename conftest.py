# Make the shared libraries importable in every test: figdata/lib (econdata,
# figout) and code/shared (country). Chapter code under code/<year>/ uses its own
# conftest if it needs more.
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
for p in (ROOT / "figdata" / "lib", ROOT / "code" / "shared"):
    sys.path.insert(0, str(p))


# A figdata test imports its chapter's make_*.py by module name (import mode is importlib, so the test's own directory
# is not on sys.path by default). Put each collected test file's directory first on sys.path. tools/figdata.sh runs one
# chapter directory per process, so modules of the same name in two chapters never meet.
def pytest_collect_file(file_path, parent):
    if file_path.suffix == ".py" and file_path.name.startswith("test_") and "figdata" in file_path.parts:
        d = str(file_path.parent)
        if d not in sys.path:
            sys.path.insert(0, d)
    return None

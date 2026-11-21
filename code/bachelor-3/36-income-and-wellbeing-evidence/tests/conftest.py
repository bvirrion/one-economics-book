import os
import subprocess
import sys
from pathlib import Path

import pytest

LISTINGS = Path(__file__).resolve().parents[1] / "listings"
EXERCISES = Path(__file__).resolve().parents[1] / "exercises"
ROOT = Path(__file__).resolve().parents[4]
sys.path[:0] = [str(LISTINGS), str(EXERCISES)]
ENV = {
    **os.environ,
    "PYTHONPATH": os.pathsep.join(
        [str(ROOT / p) for p in ("code/shared", "code/bachelor-3/lib", "figdata/lib")]
        + [str(LISTINGS)]
    ),
}


def _run(folder, name):
    out = subprocess.run(
        [sys.executable, f"{name}.py"],
        cwd=folder,
        capture_output=True,
        text=True,
        check=True,
        env=ENV,
    ).stdout
    rows = {}
    for line in out.splitlines():
        parts = line.rsplit(None, 1)
        if len(parts) == 2:
            rows[parts[0].strip()] = parts[1]
    return out, rows


@pytest.fixture
def run():
    return lambda name: _run(LISTINGS, name)


@pytest.fixture
def run_exercise():
    return lambda name: _run(EXERCISES, name)

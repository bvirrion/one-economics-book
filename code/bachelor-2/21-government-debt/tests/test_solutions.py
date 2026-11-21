"""The numbers the text and solutions of b2 ch. 21 print, recomputed."""

import importlib.util
import os
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
ENV = {
    **os.environ,
    "PYTHONPATH": os.pathsep.join(
        str(ROOT / p) for p in ("code/shared", "figdata/lib")
    ),
}
spec = importlib.util.spec_from_file_location(
    "sol21", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_stabilise():
    out = subprocess.run(
        [sys.executable, "stabilise.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
        env=ENV,
    ).stdout
    rows = [line.split() for line in out.splitlines()[1:]]
    assert rows[0] == ["DE", "61.4", "1.75", "4.28", "-1.49", "-1.67"]
    assert rows[2] == ["IT", "134.3", "2.98", "4.19", "-1.56", "0.48"]
    assert rows[3] == ["EL", "153.5", "2.23", "5.12", "-4.22", "4.86"]
    assert (HERE / "outputs" / "stabilise.txt").read_text().endswith(out)


def test_text_and_exercises():
    assert r(100 * sol.stabilising(0.9, 0.04, 0.03), 3) == 0.874
    assert r(sol.limit_with_deficit(0.02, 0.02, 0.04), 2) == 1.04
    a, half = sol.bohn()
    assert (r(a, 4), r(half, 1)) == (0.9557, 15.3)
    assert sol.smoothing() == {"uneven": 400, "smooth": 200}
    e = sol.eurostat_extended()
    assert [r(100 * e["ES"][k], 2) for k in ("s", "primary")] == [-2.42, -0.74]
    assert [r(100 * e["PT"][k], 2) for k in ("s", "primary")] == [-3.52, 2.78]
    six = sol.eurostat_extended(("DE", "FR", "IT", "EL", "ES", "PT"), 2014)
    got = [r(100 * six[k]["s"], 2) for k in ("DE", "FR", "IT", "EL", "ES", "PT")]
    assert got == [-1.28, -1.32, -0.13, -1.22, -1.88, -2.69]
    assert [r(100 * six[k]["g"], 2) for k in ("IT", "EL")] == [3.07, 3.05]


def test_brenland():
    b = sol.brenland()
    assert (r(100 * b["deficit_ratio"], 1), r(100 * b["ratio"], 1)) == (2.0, 60.2)
    assert (b["check"], r(100 * b["growth"], 1)) == (236818, 3.6)
    assert (r(b["interest"], 0), r(b["primary"], 0)) == (6869, 996)
    assert r(100 * b["primary_ratio"], 2) == 0.25
    assert (r(100 * b["s3"], 2), r(100 * b["next3"], 1)) == (-0.35, 60.1)
    assert (r(100 * b["s5"], 2), r(100 * b["next5"], 1)) == (0.81, 61.3)
    assert (b["years3"], b["years5"], b["years_repressed"]) == (8, 42, 5)
    assert r(100 * b["s_ten"], 2) == 0.70

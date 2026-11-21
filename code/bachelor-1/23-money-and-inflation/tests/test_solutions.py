"""Check the printed numbers of b1 ch. 23."""

import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def test_problem():
    p = sol.problem()
    assert p["s_max"] == p["s_max_exact"] == 3.679
    lo, hi = p["roots2"]
    assert lo < 0.4 < hi


def test_exercises():
    assert sol.exercises()["pi8"] == 3

"""Check the printed numbers of b1 ch. 19."""

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
    assert p["base"]["r"] == 4 and p["debt"]["r"] == 4.8
    assert p["base"]["I"] - p["debt"]["I"] == 8
    assert abs(p["euler"] - 400) < 1e-9


def test_exercises():
    e = sol.exercises()
    assert e["lf"]["r"] == 6 and e["taxcut"]["r"] == 7.5

"""Check the printed numbers of b1 ch. 20."""

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
    assert p["half"] == 17.33
    assert p["k"] == 6.086 and p["cg"] > p["c"]


def test_exercises():
    e = sol.exercises()
    assert e["ratio"] == 1.581

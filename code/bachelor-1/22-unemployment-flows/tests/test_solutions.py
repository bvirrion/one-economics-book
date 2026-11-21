"""Check the printed numbers of b1 ch. 22."""

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
    assert abs(p["inflow"] - p["outflow"]) < 0.5
    assert p["u2"] > p["u"]


def test_exercises():
    e = sol.exercises()
    assert e["u1"] == 6.67 and e["fire"] == e["u1"]

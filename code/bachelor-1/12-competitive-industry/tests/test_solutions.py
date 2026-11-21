"""Check the printed numbers of b1 ch. 12."""

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
    assert p["free_boats"] == 400 and p["boats_high_demand"] == 500
    assert p["cap"]["p"] == 30.0 and p["cap"]["profit"] == 62.5
    assert p["licence_4"] == 1562.5 and p["net_gain"] == 5000.0


def test_exercises():
    e = sol.exercises()
    assert e["lr_firms"] == 80 and e["land_rent"] == 5000 and e["licence"] == 800000

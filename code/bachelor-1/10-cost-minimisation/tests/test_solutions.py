"""Check the printed numbers of b1 ch. 10."""

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
    assert p["L"] == 1000 and p["K"] == 250 and p["C"] == 100000
    assert p["cum"][7] == 64000
    assert p["unit"][:5] == [100.0, 82.0, 67.24, 55.14, 45.21]
    assert p["unit_y8"] == 30.4 and p["moore_y8"] == 24.93


def test_exercises():
    e = sol.exercises()
    assert e["ex2"] == 4000 and e["ex7_mes"] == 100 and e["ex8"] == 48.8

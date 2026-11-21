"""Check the printed numbers of b1 ch. 16."""

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
    assert p["mono"]["w"] == 11.67 and p["mono"]["markdown"] == 0.571
    assert p["floors"][15] - p["mono"]["L"] == 50
    assert p["two"]["w"] == 15 and abs(p["two"]["markdown"] - 1 / 3) < 1e-3


def test_exercises():
    e = sol.exercises()
    assert e["rental"] == 1600 and abs(e["derived"] + 1.7) < 1e-12
    assert abs(e["floor12"] - 80) < 1e-9

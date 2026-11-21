"""Check the printed numbers of b1 ch. 11."""

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
    assert p["lr100"] == {"q": 2000.0, "N": 25000.0, "T": 250.0, "profit": 100000.0}
    assert p["profit_fn"] == 100000.0
    assert p["sr100"]["q"] == 2000.0
    assert p["lr150"]["q"] == 3000.0 and p["lr_both"]["q"] == 2000.0
    assert p["sr150"]["profit"] < p["lr150"]["profit"]


def test_exercises():
    e = sol.exercises()
    assert e["shutdown"] == 9.25 and e["q"] == 32.0 and e["profit"] == 64.0

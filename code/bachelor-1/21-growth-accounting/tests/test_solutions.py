"""Check the printed numbers of b1 ch. 21."""

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
    a = p["a35"]
    assert abs(a["cap"] + a["lab"] + a["tfp"] - a["gy"]) < 0.01
    assert 0 < p["mis"]["gain"] < 0.2


def test_exercises():
    e = sol.exercises()
    assert e["residual"] == 1.25 and e["two_l1"] == 20

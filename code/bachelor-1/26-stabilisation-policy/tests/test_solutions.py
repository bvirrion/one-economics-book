"""Check the printed numbers of b1 ch. 26."""

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
    assert p[0.0]["loss_lag2"] > p[0.0]["loss_none"]
    assert p[0.9]["loss_lag2"] < p[0.9]["loss_none"]
    assert 0.25 < p["stab"]["offset"] < 0.4


def test_exercises():
    e = sol.exercises()
    assert e["taylor"] == 6.5 and e["cycle_k4"] == 2.25
    assert e["loss_opt"] < e["loss_ce"] < e["loss_0"]

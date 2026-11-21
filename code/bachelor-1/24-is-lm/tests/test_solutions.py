"""Check the printed numbers of b1 ch. 24."""

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
    assert abs(p["Y0"] - 393.264) < 1e-6 and abs(p["r0"] - 3) < 1e-9
    assert p["zlb_mult"] == 2.5 and p["zlb"][1] == 0.0


def test_exercises():
    e = sol.exercises()
    assert e["r"] == 5 and e["Y"] == 1000

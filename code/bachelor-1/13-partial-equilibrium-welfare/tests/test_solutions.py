"""Check the printed numbers of b1 ch. 13."""

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
    assert p["t12"]["Q"] == 54 and p["t12"]["R"] == 64.8 and p["t12"]["DWL"] == 3.6
    assert abs(p["harberger_12"] - 3.6) < 1e-9
    assert p["t6"]["R"] == 180 and p["t6"]["DWL"] == 90
    assert p["mdwl_12"] == 0.125


def test_exercises():
    e = sol.exercises()
    assert e["cs_log"] == 69.31 and e["vat_std"] == 2.52 and e["vat_red"] == 1.87

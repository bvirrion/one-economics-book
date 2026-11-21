"""Check the printed numbers of b1 ch. 18."""

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
    assert p["gdp_check"] == 393264 and p["gni"] == 387364
    assert p["ca"] == p["s_minus_i"] == -3587 and p["private"] == 4278
    assert p["fixed"] == [1000, 1350, 2600] and p["chained"][2] == 1949.4
    assert p["g_diff"] == 0.11


def test_exercises():
    e = sol.exercises()
    assert e["ppp"] == 2.4286 and e["price_level"] == 0.81

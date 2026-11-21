"""The numbers the text and solutions of b2 ch. 18 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol18", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_pivot():
    out = subprocess.run(
        [sys.executable, "pivot.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "build True, taxes [100, 0, 0]" in out
    assert "resident 1: truthful 50, best of 401 reports 50" in out
    assert (HERE / "outputs" / "pivot.txt").read_text().endswith(out)
    assert sol.pivot([250, 60, 40], 100) == (True, [100, 0, 0])
    assert sol.pivot([250, 160, 40], 100) == (True, [0, 0, 0])
    assert sol.pivot([250, 60, 40], 110) == (True, [120, 0, 0])


def test_externality():
    assert sol.externality(120, 2, 1) == {
        "free": 60.0,
        "star": 40.0,
        "tax": 40.0,
        "loss": 600.0,
    }
    assert sol.externality(100, 2, 2)["loss"] == 1250.0
    p = sol.permits_two_firms()
    assert (r(p["e_a"], 2), r(p["e_b"], 2), r(p["price"], 2)) == (36.67, 13.33, 46.67)
    assert (p["cost_equal"], r(p["cost_trade"], 1)) == (1837.5, 1633.3)


def test_weitzman():
    w = sol.weitzman(90, 3, 6, 15)
    assert ([r(x, 2) for x in w["tax"]], [r(x, 2) for x in w["quota"]]) == (
        [50.0, 50.0],
        [12.5, 12.5],
    )


def test_public_goods():
    s = sol.samuelson([12, 10, 8], 9)
    assert (s["g_star"], s["g_vol"], s["prices"], s["loss"]) == (
        7.0,
        3,
        [5.0, 3.0, 1.0],
        24.0,
    )
    s4 = sol.samuelson([12, 10, 8, 6], 12)
    assert (s4["g_star"], s4["g_vol"], s4["prices"], s4["loss"]) == (
        6.0,
        0,
        [6.0, 4.0, 2.0, 0.0],
        72.0,
    )
    assert sol.identical_gap(10, 6, 3) == (8.0, 4)


def test_river():
    v = sol.river()
    assert v["base"] == {"free": 30.0, "star": 20.0, "tax": 30.0, "loss": 225.0}
    assert (v["gain_free"], v["damage_free"], v["gain_star"], v["damage_star"]) == (
        1350.0,
        675.0,
        1200.0,
        300.0,
    )
    assert (v["mill_loss_cut"], v["fishery_gain_cut"], v["revenue"]) == (
        150.0,
        375.0,
        600.0,
    )
    assert (v["wrong_e"], v["wrong_loss"]) == (15.0, 56.25)
    w = v["weitzman"]
    assert tuple(r(x, 2) for x in w["e_star"]) == (23.33, 16.67)
    assert w["e_tax"] == (25.0, 15.0)
    assert (r(w["tax"][0], 2), r(w["quota"][0], 2)) == (6.25, 25.0)
    s = v["steep"]
    assert (v["steep_star"]["star"], v["steep_star"]["tax"]) == (12.0, 54.0)
    assert (r(s["tax"][0], 2), r(s["quota"][0], 2)) == (33.75, 15.0)

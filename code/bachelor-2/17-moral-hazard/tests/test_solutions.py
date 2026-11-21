"""The numbers the text and solutions of b2 ch. 17 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol17", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_linear():
    out = subprocess.run(
        [sys.executable, "linear.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "    0.50    0.500     0.500    0.500     0.250        0.250" in out
    assert "    4.00    0.111     0.111    0.111     0.056        0.444" in out
    assert (HERE / "outputs" / "linear.txt").read_text().endswith(out)
    for var in [0.25, 1.0, 2.0]:
        lin = sol.linear(2.0, 1.0, var)
        assert abs(lin["surplus"] - sol.surplus_at(lin["b"], 2.0, 1.0, var)) < 1e-12


def test_two_outcome():
    t = sol.two_outcome()
    assert (t["out_high"], t["out_low"], t["fb_wage"]) == (84.0, 52.0, 49.0)
    assert (t["fb_profit"], t["low_profit"]) == (35.0, 27.0)
    assert (t["u"], t["w"], t["expected_wage"]) == ((3.0, 8.0), (9.0, 64.0), 53.0)
    assert (t["agency_cost"], t["sb_profit"]) == (4.0, 31.0)
    t6 = sol.two_outcome(ubar=6.0)
    assert (t6["w"], t6["expected_wage"], t6["sb_profit"], t6["low_profit"]) == (
        (16.0, 81.0),
        68.0,
        16.0,
        16.0,
    )
    assert sol.risk_neutral() == (3.0, 8.0, 7.0)


def test_small_ones():
    lin = sol.linear(2.0, 1.0, 0.5)
    assert (lin["b"], lin["surplus"], lin["agency"]) == (0.5, 0.25, 0.25)
    assert (lin["risk_premium"], lin["effort_cost"]) == (0.125, 0.125)
    assert sol.team(4) == (0.25, 0.21875, 0.5)
    assert sol.rpe_k(3.0, 1.0) == (0.75, 1.75)
    k, v = sol.rpe_k(3.0, 1.0, n=4)
    assert (r(k, 3), r(v, 3)) == (0.923, 1.231)
    assert sol.holdup() == {"return": 25.0, "invests": False, "min_share": 0.6}
    h = sol.hie()
    assert (r(h["fall25"], 1), r(h["fall95"], 1), r(h["fall25_95"], 1)) == (
        21.6,
        40.6,
        24.2,
    )


def test_orchard():
    o = sol.orchard()
    b = o["base"]
    assert (b["b"], b["effort"], b["risk_premium"], b["effort_cost"]) == (
        0.5,
        50.0,
        12.5,
        12.5,
    )
    assert (b["surplus"], b["agency"], o["fixed_rent"]) == (25.0, 25.0, 0.0)
    assert (r(o["law"], 2), o["law_effort"]) == (18.75, 75.0)
    k1 = o["k1"]
    assert (r(k1["b"], 3), r(k1["effort"], 1), r(k1["surplus"], 2)) == (
        0.833,
        83.3,
        41.67,
    )
    assert r(k1["agency"], 2) == 8.33
    assert (o["k_opt"], o["v_opt"]) == (0.9, 380.0)
    op = o["opt"]
    assert (r(op["b"], 3), r(op["effort"], 1), r(op["surplus"], 2)) == (
        0.84,
        84.0,
        42.02,
    )
    assert (r(op["agency"], 2), r(o["law_rpe"], 2)) == (7.98, 41.53)

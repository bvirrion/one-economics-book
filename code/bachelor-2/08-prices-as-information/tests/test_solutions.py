"""The numbers the text and solutions of b2 ch. 8 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol08", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_informed_share():
    out = subprocess.run(
        [sys.executable, "informed_share.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "error variance 0.250" in out
    assert "slope 0.862" in out
    assert (HERE / "outputs" / "informed_share.txt").read_text().endswith(out)


def test_gs_points():
    assert [r(x, 3) for x in sol.gs(0.1116)] == [0.433, 0.250]
    assert [r(x, 3) for x in sol.gs(0.05)] == [0.729, 0.105]
    assert [r(x, 3) for x in sol.gs(0.2)] == [0.254, 0.492]
    assert [r(x, 3) for x in sol.gs(0.08)] == [0.546, 0.174]
    assert sol.gs(0.4) == (0.0, 1.0)


def test_small_exercises():
    assert sol.counts() == (78_000_000, 39)
    assert sol.two_signal(2, -0.5) == (0.75, 1.5)
    q, q0 = sol.payback(100, -61)
    assert r(q, 4) == 0.0039 and r(q0, 4) == 0.0099
    q, q0 = sol.payback(2, -5.5)
    assert r(q, 3) == 0.315 and r(q0, 3) == 0.333
    assert [r(x, 0) for x in sol.iem()[:2]] == [22, 17]


def test_luck_spending_dual():
    assert r(sol.luck(), 3) == 0.304
    assert r(sol.spending(), 4) == 0.0483
    assert sol.dual_track() == (30, 12, 270, 450, 180)


def test_problem():
    h = sol.harvest()
    assert (h["var_h"], h["err_both"], h["err_one"]) == (41, 9, 25)
    assert (h["naive"], h["revealing"], h["demand_n_naive"]) == (102, 104, 0.16)
    assert sol.expected_msq() == (13, 11.25, 10.5625)
    assert round(sol.seasons_needed()) == 414
    rec = sol.record()
    assert r(rec["mae_office"], 2) == 3.07 and r(rec["mae_market"], 2) == 3.22
    assert r(rec["msq_office"], 2) == 15.0 and r(rec["msq_market"], 2) == 14.28
    assert rec["market_closer"] == 7 and r(rec["mae_avg"], 2) == 2.78
    assert r(rec["d_mean"], 2) == -0.72 and r(rec["d_sd"], 1) == 17.8
    assert r(rec["d_se"], 2) == 5.13

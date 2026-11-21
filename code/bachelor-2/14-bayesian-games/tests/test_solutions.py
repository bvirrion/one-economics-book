"""The numbers the text and solutions of b2 ch. 14 print, recomputed."""

import importlib.util
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "sol14", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def r(x, n):
    return round(float(x), n)


def test_listing_auctions():
    out = subprocess.run(
        [sys.executable, "auctions.py"],
        cwd=HERE / "listings",
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    assert "n = 3: revenue first-price 0.500" in out
    assert "first-price with risk-averse bidders 0.600" in out
    assert (HERE / "outputs" / "auctions.txt").read_text().endswith(out)


def test_cournot():
    assert [r(x, 3) for x in sol.cournot_private()] == [3.667, 2.167, 3.167]
    assert [r(x, 2) for x in sol.cournot_private(theta=0.25)] == [3.5, 2.25, 3.25]


def test_auctions():
    assert [r(sol.first_price_bid(v, 3), 1) for v in (30, 50, 80)] == [20, 33.3, 53.3]
    assert [r(x, 3) for x in sol.revenue(2)] == [0.333, 0.333]
    assert [r(x, 3) for x in sol.revenue(10)] == [0.818, 0.818]
    assert r(sol.risk_aversion_from_slope(0.75, 3), 3) == 0.333
    assert r(sol.first_price_bid(1, 3, 0.5), 2) == 0.8
    assert r(sol.bayes(), 4) == 0.6316
    assert r(sol.bayes_poor_report(), 4) == 0.0968
    assert [r(x, 2) for x in sol.jar()] == [2.01, 2.87]
    assert sol.signalling()


def test_licence():
    d = sol.licence()
    assert (d["e_max"], d["e_second"], d["bid"]) == (640.0, 480.0, 450.0)
    assert r(d["win"], 4) == 0.4219
    assert r(d["payoff_first"], 2) == r(d["payoff_second"], 2) == 63.28
    assert d["revenue"] == (480.0, 480.0)
    assert r(d["risk_bid"], 1) == 514.3
    assert [r(x, 1) for x in d["sd"]] == [98.0, 160.0]
    assert (d["conditional"], d["correction"]) == (440.0, 60.0)
    assert r(d["correction8"], 1) == 77.8

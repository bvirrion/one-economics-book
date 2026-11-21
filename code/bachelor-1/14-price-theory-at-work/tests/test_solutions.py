"""Check the printed numbers of b1 ch. 14."""

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
    assert p["path"][1] == 203.0 and p["path"][10] == 230.68
    assert p["premium_july"] == 15.34
    assert p["trade10"] == {"P_K": 185.0, "P_B": 195.0, "Q": 50.0}
    assert p["trade30"] == {"P_K": 175.0, "P_B": 205.0, "Q": 30.0}
    assert p["value_5"] == 1920000


def clearing_price(c):
    """Kestria price that clears the market, by bisection on excess demand,
    independently of the closed form in solutions.trade."""
    lo, hi = 160.0, 220.0
    for _ in range(200):
        pk = (lo + hi) / 2
        excess = 2 * (220 - (pk + c)) - 2 * (pk - 160)
        lo, hi = (pk, hi) if excess > 0 else (lo, pk)
    return pk


def test_trade_clears_the_market():
    for c in (0, 10, 30, 55):
        t = sol.trade(c)
        assert abs(t["P_K"] - clearing_price(c)) < 1e-9
        assert abs(t["Q"] - 2 * (220 - t["P_B"])) < 1e-9
        assert abs(t["Q"] - 2 * (t["P_K"] - 160)) < 1e-9
    assert sol.trade(60)["Q"] == 0.0


def test_exercises():
    e = sol.exercises()
    assert e["full"] == 34 and e["quota_rent"] == 160
    assert e["ceiling"] == {"shortage": 40, "dwl": 400.0, "queue": 800}
    assert e["random_extra"] == 400 and e["tariff"]["revenue"] == 72

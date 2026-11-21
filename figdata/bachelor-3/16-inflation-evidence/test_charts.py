import numpy as np
from cagan import financing_rates, peak, seigniorage
from make_breakeven import table as be
from make_money_inflation import tables as mi
from make_prices import table as prices
from make_targeting import table as it


def test_peak_is_one_over_alpha():
    mu, s = peak()
    assert np.isclose(mu, 0.5) and s > seigniorage(0.45) and s > seigniorage(0.55)


def test_two_roots_raise_the_deficit():
    lo, hi = financing_rates()
    assert np.isclose(seigniorage(lo), 3.0) and np.isclose(seigniorage(hi), 3.0)


def test_money_and_inflation_one_for_one():
    _, s = mi()
    v = s.set_index("stat").value
    assert abs(v["slope"] - 1) < 0.15


def test_prices_indexed():
    t = prices()
    assert np.allclose(t.iloc[0, 1:], 1.0)


def test_targeters_disinflate():
    t = it().set_index("k")
    assert t.targeters[5] < t.targeters[-5]


def test_breakeven_positive():
    assert (be().breakeven > 0).all()

import numpy as np
from fund import contribution, cost, gamma_drop, optimum
from make_dependency import table as dep
from make_duration import table as dur


def test_optimum_balances():
    u = 0.06
    r = optimum(u)
    assert np.isclose(gamma_drop(r), cost(u))


def test_exact_above_linear():
    assert 0 < optimum(0.06, exact=True) - optimum(0.06) < 0.15


def test_fund_balances():
    assert np.isclose(contribution(0.5, 0.1) * 0.9, 0.05)


def test_estimates_in_range():
    d = dur()
    assert (d.low <= d.high).all() and d.high.max() < 1


def test_dependency_rises():
    t = dep().set_index("year")
    assert (t.loc[2025] > t.loc[1960]).all()

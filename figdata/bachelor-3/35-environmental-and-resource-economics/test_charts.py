import numpy as np
from coal import (
    COST,
    R,
    abatement,
    costs,
    cumulative,
    demand,
    hotelling,
    marginal_damage,
)
from make_co2 import table as co2
from make_scc import table as scc
from make_so2 import paths


def test_hotelling_exhausts_the_stock_at_the_backstop():
    lam, T = hotelling()
    assert np.isclose(COST + lam * np.exp(R * T), 100)
    # independent check: sum of yearly extraction with a fine step
    dt = T / 200000
    t = (np.arange(200000) + 0.5) * dt
    total = (demand(COST + lam * np.exp(R * t)) * dt).sum()
    assert np.isclose(total, 600, rtol=1e-4) and np.isclose(
        cumulative(lam), 600, rtol=1e-6
    )


def test_equal_marginal_costs_by_hand():
    md = marginal_damage()
    assert md == 1200
    x1, x2 = abatement(md)
    assert (x1, x2) == (120, 40)
    # 160 kt split equally: 0.5 (10 + 30) 80^2; efficiently: 0.5 (10 120^2 + 30 40^2)
    assert sum(costs(80, 80)) == 0.5 * 40 * 6400 * 1000
    assert sum(costs(x1, x2)) < sum(costs(80, 80))


def test_data_charts():
    d = paths()
    assert d.kg.max() > 50
    c = co2()
    assert len(c) > 100
    s = scc()
    assert (s.r15 > s.r20).all() and (s.r20 > s.r25).all()

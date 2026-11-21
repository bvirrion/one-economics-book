import numpy as np
from brenland import SIGMA, stats
from make_oaxaca import tables as oax
from make_race import table as race


def test_sigma_recovered():
    assert abs(stats()["sigma"] - SIGMA) < 0.3


def test_oaxaca_adds_up():
    t, _ = oax()
    assert np.allclose(t.explained + t.unexplained, t.gap)


def test_demand_identity():
    d = race()
    assert np.allclose(d.demand, d.supply + 1.62 * d.wage, atol=0.02)

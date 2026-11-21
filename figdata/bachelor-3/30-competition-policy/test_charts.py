import numpy as np
from make_critical_loss import critical_loss
from make_yields import table as yields
from water import aj, average_cost, cap, monopoly, sharing_x


def test_by_hand():
    m = monopoly()
    assert (m["q"], m["p"], m["profit"]) == (40.0, 60.0, 1000.0)
    a = average_cost()
    # (100 - Q) Q = 20 Q + 600: Q = 40 + sqrt(1000)
    assert np.isclose(a["q"], 40 + np.sqrt(1000))
    # 5 % rise, 40 % margin: 0.05 / 0.45
    assert np.isclose(critical_loss(0.05, 0.40), 1 / 9)


def test_aj_overcapitalises_and_binds():
    r = aj()
    assert r["kl"] > 1 and r["cost"] > r["mincost"]
    # binding constraint: profit equals (s - r) K
    assert np.isclose(r["profit"], 2 * r["k"])
    # the cost-minimising plan would earn more than the regulator allows
    assert r["profit_min"] > 2 * 60


def test_cap_shares_equally():
    x = sharing_x()
    s = cap(x, 16.0, 150.0)
    assert np.isclose(s["cs"] - average_cost()["cs"], s["profit"])
    assert 0 < x < 4


def test_three_periods():
    t = yields()
    assert len(t) == 3 and (t["yield"] < 0).all() and (t.traffic > 0).all()

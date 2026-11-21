import numpy as np
from make_union import brenland, estimates, panel
from make_waves import tables as waves
from make_zeros import table as zeros
from world import countries, flows


def test_flows_add_up_to_gdp():
    c = countries()
    X = flows(c)
    assert np.allclose(X.sum(axis=1), c.gdp, rtol=1e-6)
    assert np.allclose(X.sum(axis=0), c.gdp, rtol=1e-6)


def test_union_creates_and_diverts():
    c = countries()
    b = brenland(c, 1.0, 0.5).set_index("partners")
    assert b.change["members"] > 0 > b.change["non-members"]
    assert b.change["members"] < 100 * (np.exp(0.5) - 1)


def test_estimates_near_truth():
    c, p = panel()
    e = estimates(p).set_index("method")
    assert abs(e.dist["PPML with fixed effects"] + 1) < 0.2
    assert 0 < e.union["PPML with fixed effects"] < 1


def test_waves_and_zeros():
    g, pts = waves()
    s = pts.set_index("year").share
    assert s[1913] > s[1932] < s[1970] < s[2008]
    z = zeros()
    assert (z.zero_share > 0).all() and (z.zero_share < 100).all()

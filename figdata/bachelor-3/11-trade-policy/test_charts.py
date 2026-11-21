import numpy as np
from make_steel import optimal, small, tables
from make_tariffs import tables as tariffs
from steel import grain, steel


def test_free_trade_clears():
    s = steel(0.0)
    assert np.isclose(s["imports"], s["q_demand"] - s["q_supply"])
    g = grain(0.0)
    assert np.isclose(g["exports"], 100 - 3 * g["p_kestria"])


def test_welfare_identities():
    s = steel(0.25)
    assert np.isclose(s["brenland"], s["tot_gain"] - s["dwl"])
    assert np.isclose(small(0.25)["brenland"], -small(0.25)["dwl"])
    g = grain(0.25)
    assert np.isclose(g["kestria"], g["tot_gain"] - g["dwl"])


def test_optimal_tariff_is_inverse_elasticity():
    t = optimal()
    pw = steel(t)["p_world"]
    assert abs(t - 1 / (4 * pw / (-40 + 4 * pw))) < 0.002


def test_tariff_war_is_a_prisoners_dilemma():
    p = tables()[2].set_index(["brenland_tariff", "kestria_tariff"])
    assert p.brenland[(0.25, 0.0)] > 0 > p.brenland[(0.25, 0.25)]
    assert p.kestria[(0.0, 0.25)] > 0 > p.kestria[(0.25, 0.25)]


def test_tariffs_fall():
    w, dropped, pts = tariffs()
    assert len(dropped) == 1 and (pts["last"] < pts["first"]).all()


def test_bound_one_eu_point_and_overhang():
    from make_bound import EU27, table
    m = table()
    assert not m.iso3.isin([e for e in EU27 if e != "FRA"]).any()
    assert m.iso3.is_unique and m.year.between(2017, 2021).all()
    assert np.allclose(m.overhang, m.bound - m.applied)

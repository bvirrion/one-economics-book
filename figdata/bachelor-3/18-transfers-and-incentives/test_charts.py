import numpy as np
from brenland_benefit import gini, net, old_transfers, ptr
from country import load
from make_mtr import tables as mtr
from us2024 import eitc, net_income


def test_eitc_trapezoid():
    assert np.isclose(eitc(17_400), 6_960) and eitc(55_768) < 1


def test_net_rises_with_earnings():
    assert net_income(30_000) > net_income(20_000) > net_income(0)


def test_mtr_bounds():
    _, _, s = mtr()
    v = s.set_index("stat").value
    assert -50 < v["mtr_min"] < 0 < v["mtr_max"] < 45


def test_old_transfers_match_survey():
    h = load("households")
    rebuilt = [round(old_transfers(g, s), -1) for g, s in zip(h.gross_income,
                                                                h["size"])]
    assert np.allclose(rebuilt, h.transfers)


def test_reform_lowers_ptr_and_cliff():
    assert ptr(15_000, 3, True) < ptr(15_000, 3)
    assert net(12_000, 3, True) > net(12_000, 3)


def test_gini_bounds():
    assert np.isclose(gini([1, 1, 1]), 0) and 0 < gini([0, 0, 1]) < 1


def test_gini_eu_ordered_and_transfers_lower_inequality():
    from make_gini import table
    t = table()
    assert t.disposable.is_monotonic_increasing and len(t) >= 30
    assert (t.before_all >= t.before_ex_pensions).all()
    assert (t.before_ex_pensions > t.disposable).all()

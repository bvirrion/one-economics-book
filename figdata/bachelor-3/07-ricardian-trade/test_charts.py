import numpy as np
from make_crops import tables as crops
from make_dfs import curves
from make_japan import table as japan
from make_twelve import tables as twelve
from twelve import equilibrium


def test_japan_inner_product_negative_every_year():
    j = japan()
    assert (j.total < 0).all() and (j.sum_components - j.total).abs().max() <= 0.021


def test_crops_sample():
    d, fit, stats = crops()
    assert 50 < len(d) < 120 and np.isfinite(d.x).all()


def test_dfs_equilibrium_where_curves_cross():
    z, A, B, k = curves()
    assert B[k] >= A[k] and B[k - 1] < A[k - 1]


def test_twelve_free_trade_and_iceberg():
    g, r = twelve()
    r = r.set_index("case")
    assert np.isclose(r.omega["free trade"], 1.4) and r.exported["free trade"] == 7
    assert np.isclose(r.omega["iceberg 10 %"], 1.5) and r.nontraded["iceberg 10 %"] == 2
    assert r.gain_B["Kestria +20 %"] > r.gain_B["free trade"]
    assert (r.gain_B > 0).all() and (r.gain_K > 0).all()


def test_balanced_trade_two_good_case():
    w, e, m, nt = equilibrium([6.0, 1.5], 1.0)
    assert 1.5 <= w <= 6.0 and abs(w * m - e) < 1e-9

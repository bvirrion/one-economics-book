import numpy as np
import pandas as pd
from make_koreas import tables as koreas
from make_opening import tables as opening
from make_transition import index, stats
from river import districts, iv, panel, required_p, synth


def test_wald_ratio_equals_two_stage_least_squares():
    d = districts()
    r = iv(d)
    # 2SLS by the two stages: regress s on z, then ln y on the fitted s
    X = np.column_stack([np.ones(len(d)), d.z])
    shat = X @ np.linalg.lstsq(X, d.s, rcond=None)[0]
    Z = np.column_stack([np.ones(len(d)), shat])
    assert np.isclose(np.linalg.lstsq(Z, d.lny, rcond=None)[0][1], r["tsls"])
    assert 0.8 < r["tsls"] < 1.2 < r["ols"]


def test_synth_weights_and_known_combination():
    p = panel()
    w, _ = synth(p)
    assert np.isclose(w.sum(), 1) and (w >= -1e-9).all()
    # a treated unit built as a known mix of two donors is recovered
    q = p.copy()
    q["X"] = 0.25 * p.D2 + 0.75 * p.D7
    w2, _ = synth(q, "X")
    assert abs(w2.D2 - 0.25) < 0.02 and abs(w2.D7 - 0.75) < 0.02


def test_required_p_by_hand():
    # output ratio ((1 - pS) / (1 - pN)) ** 0.5 = exp(-0.3) when a = 1/3
    pS = required_p(0.3, 0.05)
    assert np.isclose(((1 - pS) / 0.95) ** 0.5, np.exp(-0.3))


def test_data_charts():
    c, west, east, st = opening()
    assert c.year.min() == 1950 and len(west) == len(east)
    s, n, ks = koreas()
    assert n.year.min() == 1990
    i = index()
    assert np.allclose(i.loc[1989], 100)
    t = stats(i).set_index("iso3")
    assert (t.trough < 100).all() and isinstance(t, pd.DataFrame)

"""HC1 standard errors and binned residual spread, recomputed by hand with numpy."""

import numpy as np
from econdata import sm_dataset
from make_inference import se_table, spread


def test_hc1_by_hand():
    d = sm_dataset("randhie")
    X = np.column_stack([np.ones(len(d)), d.drop(columns="mdvis").to_numpy(float)])
    y = d.mdvis.to_numpy(float)
    n, k = X.shape
    a = np.linalg.inv(X.T @ X)
    b = a @ X.T @ y
    e = y - X @ b
    classical = np.sqrt(np.diag(a) * (e @ e) / (n - k))
    hc1 = np.sqrt(np.diag(a @ (X.T * e**2) @ X @ a) * n / (n - k))
    t = se_table()
    assert np.allclose(t.se, classical.round(4), atol=1e-4)
    assert np.allclose(t.hc1, hc1.round(4), atol=1e-4)
    r = t.set_index("term").ratio
    # the chart prints the ratios to two decimals; check them from the hand-made errors
    hand = dict(zip(t.term, (hc1 / classical).round(2)))
    assert all(r[k] == hand[k] for k in hand)
    assert (r["hlthp"], r["disea"], r["physlm"], r["lncoins"], r["idp"]) == (
        1.55,
        1.29,
        1.25,
        0.93,
        0.95,
    )


def test_spread():
    s = spread()
    assert s.n.sum() == 20190 and s.n.min() >= 1009
    assert s.sd.iloc[-1] > 3 * s.sd.iloc[0]

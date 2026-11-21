import numpy as np
import pandas as pd
import statsmodels.api as sm
from paneltools import demean, ols_cluster, twoway_demean


def _panel(n=40, t=8, seed=4, drop=0):
    rng = np.random.default_rng(seed)
    d = pd.DataFrame({"i": np.repeat(np.arange(n), t), "t": np.tile(np.arange(t), n)})
    a = rng.normal(size=n)[d.i]
    d["x"] = a + rng.normal(size=len(d)) + 0.1 * d.t
    d["y"] = 2 * d.x + 3 * a + 0.2 * d.t + rng.normal(size=len(d))
    return d.iloc[drop:].reset_index(drop=True)


def test_demean_equals_unit_dummies():
    d = _panel()
    w = demean(d, ["y", "x"], "i")
    b_w = (w.x @ w.y) / (w.x @ w.x)
    D = pd.get_dummies(d.i, dtype=float)
    b_d = sm.OLS(d.y, pd.concat([d.x, D], axis=1)).fit().params["x"]
    assert np.isclose(b_w, b_d)


def test_twoway_demean_equals_both_dummies_unbalanced():
    d = _panel(drop=5)
    w = twoway_demean(d, ["y", "x"], "i", "t")
    b_w = (w.x @ w.y) / (w.x @ w.x)
    D = pd.get_dummies(d.i, dtype=float)
    T = pd.get_dummies(d.t, dtype=float).iloc[:, 1:]
    b_d = sm.OLS(d.y, pd.concat([d.x, D, T], axis=1)).fit().params["x"]
    assert np.isclose(b_w, b_d, atol=1e-8)


def test_cluster_se_matches_statsmodels():
    d = _panel()
    X = sm.add_constant(d.x)
    r = ols_cluster(d.y, X, d.i)
    f = sm.OLS(d.y, X).fit(cov_type="cluster", cov_kwds={"groups": d.i})
    assert np.allclose(r["se_cluster"], f.bse)
    f0 = sm.OLS(d.y, X).fit()
    assert np.allclose(r["se_iid"], f0.bse)
    assert np.allclose(r["se_hc1"], f0.get_robustcov_results("HC1").bse)

import numpy as np
import statsmodels.api as sm
from ivtools import first_stage_f, ols, tsls
from statsmodels.sandbox.regression.gmm import IV2SLS


def _data(n=2000, seed=3):
    rng = np.random.default_rng(seed)
    z = rng.normal(size=(n, 2))
    w = rng.normal(size=n)
    v = rng.normal(size=n)
    u = 0.7 * v + rng.normal(size=n)
    x = 0.5 * z[:, 0] + 0.3 * z[:, 1] + 0.2 * w + v
    y = 1.0 + 2.0 * x - 1.0 * w + u
    X = np.column_stack([np.ones(n), w, x])
    Z = np.column_stack([np.ones(n), w, z])
    return y, X, Z, x, z, w


def test_ols_matches_statsmodels():
    y, X, _, *_ = _data()
    r = ols(y, X)
    f = sm.OLS(y, X).fit()
    assert np.allclose(r["beta"], f.params)
    assert np.allclose(r["se"], f.bse)
    assert np.allclose(ols(y, X, se="HC1")["se"], f.get_robustcov_results("HC1").bse)


def test_tsls_matches_statsmodels_iv2sls():
    y, X, Z, *_ = _data()
    r = tsls(y, X, Z)
    f = IV2SLS(y, X, Z).fit()
    assert np.allclose(r["beta"], f.params)
    assert np.allclose(r["se"], f.bse)


def test_tsls_consistent_and_ols_biased():
    y, X, Z, *_ = _data(n=50_000)
    assert abs(tsls(y, X, Z)["beta"][2] - 2.0) < 0.03
    assert ols(y, X)["beta"][2] > 2.2


def test_first_stage_f_equals_statsmodels_ftest():
    y, X, Z, x, z, w = _data()
    W = np.column_stack([np.ones(len(x)), w])
    f = sm.OLS(x, np.column_stack([W, z])).fit()
    ft = f.f_test(np.array([[0, 0, 1, 0], [0, 0, 0, 1]]))
    assert np.isclose(first_stage_f(x, z, W), float(np.squeeze(ft.fvalue)))


def test_just_identified_tsls_is_wald_ratio():
    rng = np.random.default_rng(0)
    n = 5000
    z = rng.integers(0, 2, n).astype(float)
    x = 0.4 * z + rng.normal(size=n)
    y = 0.3 * x + rng.normal(size=n)
    one = np.ones(n)
    b = tsls(y, np.column_stack([one, x]), np.column_stack([one, z]))["beta"][1]
    wald = (y[z == 1].mean() - y[z == 0].mean()) / (x[z == 1].mean() - x[z == 0].mean())
    assert np.isclose(b, wald)

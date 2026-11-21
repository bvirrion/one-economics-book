import numpy as np
import statsmodels.api as sm
from choicetools import clogit, logit_newton
from statsmodels.discrete.conditional_models import ConditionalLogit


def test_logit_matches_statsmodels():
    rng = np.random.default_rng(0)
    X = sm.add_constant(rng.normal(size=(2000, 2)))
    y = (rng.uniform(size=2000) < 1 / (1 + np.exp(-(X @ [0.3, 1.0, -0.5])))).astype(float)
    r = logit_newton(y, X)
    f = sm.Logit(y, X).fit(disp=0)
    assert np.allclose(r["beta"], f.params, atol=1e-6)
    assert np.allclose(r["se"], f.bse, atol=1e-6)
    assert abs(r["loglik"] - f.llf) < 1e-6


def test_clogit_matches_statsmodels_conditional_logit():
    rng = np.random.default_rng(1)
    n, J = 400, 3
    groups = np.repeat(np.arange(n), J)
    X = rng.normal(size=(n * J, 2))
    u = X @ [1.0, -0.7] + rng.gumbel(size=n * J)
    chosen = np.zeros(n * J)
    chosen[np.arange(n) * J + u.reshape(n, J).argmax(1)] = 1
    r = clogit(chosen, X, groups)
    f = ConditionalLogit(chosen, X, groups=groups).fit(disp=0)
    assert np.allclose(r["beta"], f.params, atol=1e-6)
    assert np.allclose(r["se"], f.bse, atol=1e-5)
    p = r["prob"].reshape(n, J)
    assert np.allclose(p.sum(1), 1)

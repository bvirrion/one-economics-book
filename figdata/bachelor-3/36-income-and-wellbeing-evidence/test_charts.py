import numpy as np
from brenland import gini
from make_satisfaction import table as sat
from make_welfare import compute
from welfare import log_lambda, sigma_from_gini


def test_gini_by_hand():
    # incomes 1, 2, 3, 4 equally weighted: G = sum |xi - xj| / (2 n^2 mean) = 20 / 80
    assert np.isclose(gini([1, 2, 3, 4], [1, 1, 1, 1]), 0.25)


def test_lognormal_gini_round_trip():
    # Monte Carlo: the Gini of a lognormal sample with the implied sigma is G
    rng = np.random.default_rng(0)
    s = float(sigma_from_gini(0.35))
    x = np.sort(np.exp(rng.normal(0, s, 200000)))
    n = len(x)
    g = (2 * np.arange(1, n + 1) - n - 1) @ x / (n * x.sum())
    assert abs(g - 0.35) < 0.003


def test_log_lambda_solves_the_definition():
    e0, c0, h0, s0, th, k = 78.0, 1.0, 0.15, 0.6, 40.0, 5.0
    e, c, h, s = 70.0, 0.5, 0.2, 0.5
    ll, _ = log_lambda(e, c, h, s, e0, c0, h0, s0, th, k)
    ubar = k - np.log(c0) + th * h0**2 / 2 + s0**2 / 2

    def u(cc, hh, ss):
        return ubar + np.log(cc) - th * hh**2 / 2 - ss**2 / 2

    assert np.isclose(e0 * u(np.exp(ll) * c0, h0, s0), e * u(c, h, s))


def test_charts():
    d = sat()
    assert len(d) > 25 and d.s24.between(0, 10).all()
    w, th = compute()
    assert np.isclose(w.set_index("iso3").loc["USA", "ll"], 0) and th > 0

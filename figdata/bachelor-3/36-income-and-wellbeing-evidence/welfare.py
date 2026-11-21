"""Consumption-equivalent welfare in the Jones--Klenow form.

A person's flow utility is u = ubar + ln c - v(h) - sigma^2 / 2, where c is mean
consumption, h hours worked per person as a share of 5,840 hours a year (16 a day),
v(h) = theta h^2 / 2, and sigma^2 the variance of log consumption (lognormal, read
off the Gini coefficient: sigma = sqrt(2) Phi^{-1}((1 + G) / 2)). Lifetime welfare is e
u, with e life expectancy. Country i's welfare relative to the reference country 0
is the lambda with e_0 u(lambda c_0, h_0, sigma_0) = e_i u(c_i, h_i, sigma_i):
ln lambda = (e_i - e_0) / e_0 * u_i + ln(c_i / c_0) - (v(h_i) - v(h_0))
            - (sigma_i^2 - sigma_0^2) / 2,
with ubar set so that u_0 = KAPPA. theta is set so that the reference country's
marginal hour is worth its wage: theta = s_L (y_0 / c_0) / h_0^2 with s_L = 0.6."""

import numpy as np
from scipy.stats import norm

KAPPA, S_L, YEAR_HOURS = 5.0, 0.6, 5840.0


def sigma_from_gini(g):
    return np.sqrt(2) * norm.ppf((1 + np.asarray(g)) / 2)


def theta(y0, c0, h0):
    return S_L * (y0 / c0) / h0**2


def log_lambda(e, c, h, sig, e0, c0, h0, sig0, th, kappa=KAPPA):
    v = th * np.asarray(h) ** 2 / 2
    v0 = th * h0**2 / 2
    u = (
        kappa
        + np.log(np.asarray(c) / c0)
        - (v - v0)
        - (np.asarray(sig) ** 2 - sig0**2) / 2
    )
    life = (np.asarray(e) - e0) / e0 * u
    cons = np.log(np.asarray(c) / c0)
    leis = -(v - v0)
    ineq = -(np.asarray(sig) ** 2 - sig0**2) / 2
    return life + cons + leis + ineq, {
        "life": life,
        "cons": cons,
        "leisure": leis,
        "ineq": ineq,
    }

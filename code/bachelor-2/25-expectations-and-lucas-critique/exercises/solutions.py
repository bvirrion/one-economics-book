"""Worked numbers for the text, exercises and problem of Book 4, chapter 25.

Inflation-bias model: u = u* - a (pi - pi_e) + e; the bank minimises
(pi - target)**2 / 2 + w (u - u* + k)**2 / 2; society's weight is lam.
"""


def bias(w, a, k):
    """Inflation above target under discretion, with rational expectations."""
    return w * a * k


def responses(w, a):
    """Response of inflation and of unemployment to a supply shock e, discretion."""
    return w * a / (1 + w * a**2), 1 / (1 + w * a**2)


def expected_loss(w, lam, a, k, sigma2):
    """Society's expected loss when a bank with weight w sets policy."""
    p, u = responses(w, a)
    return 0.5 * (bias(w, a, k) ** 2 + p**2 * sigma2) + 0.5 * lam * (
        k**2 + u**2 * sigma2
    )


def commitment_loss(lam, a, k, sigma2):
    """Expected loss under the best rule: no bias, the same responses to shocks."""
    p, u = responses(lam, a)
    return 0.5 * p**2 * sigma2 + 0.5 * lam * (k**2 + u**2 * sigma2)


def best_weight(lam, a, k, sigma2, steps=200000):
    grid = (lam * i / steps for i in range(steps + 1))
    return min(grid, key=lambda w: expected_loss(w, lam, a, k, sigma2))


def decade_inflation():
    from econdata import jst

    j = jst(since=1949, until=2019, cols=["cpi"]).sort_values(["iso3", "year"])
    j["infl"] = 100 * j.groupby("iso3").cpi.pct_change()
    j = j[j.year >= 1950]
    j["decade"] = (j.year // 10) * 10
    t = j.groupby(["decade", "iso3"]).infl.mean().unstack()
    return t.median(axis=1).round(1), t.max(axis=1).round(1), t.idxmax(axis=1)


BRENLAND = {"target": 2.0, "a": 0.5, "k": 2.0, "lam": 1.0, "sigma2": 4.0}

"""Worked numbers for Book 4, chapter 28, in closed form.

Analytic RBC: log output responds to a 1 per cent technology shock at date 0 as
y_t = (rho**(t + 1) - alpha**(t + 1)) / (rho - alpha), and y_t = alpha**t if rho = 0.
"""

from math import log


def irf(t, rho, alpha):
    if rho == alpha:
        return (t + 1) * alpha**t
    return (rho ** (t + 1) - alpha ** (t + 1)) / (rho - alpha)


def half_life(rho, alpha, horizon=500):
    """First period after the peak at which the response is below half its peak."""
    path = [irf(t, rho, alpha) for t in range(horizon)]
    peak = max(path)
    top = path.index(peak)
    return next(t for t in range(top, horizon) if path[t] < peak / 2), top, peak


def steady_k(alpha, beta, a=1.0):
    return (alpha * beta * a) ** (1 / (1 - alpha))


def shares(alpha, beta):
    return alpha * beta, 1 - alpha * beta


def iid_half_life(alpha):
    return log(2) / log(1 / alpha)


BRENLAND = {"alpha": 0.3, "beta": 0.95, "rho": 0.8}


def growth_moments():
    """Exercise 9: the moments on quarterly log differences instead of HP cycles."""
    import numpy as np
    from econdata import sm_dataset

    m = sm_dataset("macrodata")
    names = (
        ("output", "realgdp"),
        ("consumption", "realcons"),
        ("investment", "realinv"),
    )
    g = {k: 100 * np.diff(np.log(m[c].to_numpy())) for k, c in names}
    out = {}
    for k, s in g.items():
        out[k] = (
            round(float(s.std(ddof=1) / g["output"].std(ddof=1)), 2),
            round(float(np.corrcoef(s, g["output"])[0, 1]), 2),
        )
    return out

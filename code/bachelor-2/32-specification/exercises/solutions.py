"""Worked numbers for Book 4, chapter 32 (exercises and the weekend problem)."""

import numpy as np


def engel_quadratic():
    """D exercise: log food on centred log income and its square (Engel data)."""
    import statsmodels.formula.api as smf
    from econdata import sm_dataset

    d = sm_dataset("engel")
    d["lf"] = np.log(d.foodexp)
    d["li"] = np.log(d.income)
    centre = d.li.mean()
    d["c"] = d.li - centre
    fit = smf.ols("lf ~ c + I(c**2)", d).fit()
    b1, b2 = fit.params["c"], fit.params["I(c ** 2)"]
    q10, q90 = np.log(d.income.quantile([0.1, 0.9]))
    return {
        "b1": b1,
        "b2": b2,
        "p2": fit.pvalues["I(c ** 2)"],
        "e10": b1 + 2 * b2 * (q10 - centre),
        "e90": b1 + 2 * b2 * (q90 - centre),
    }


def proxy_coef(noise, seed=32, n=100_000):
    """The proxy listing with a different noise in the test score."""
    import statsmodels.api as sm

    rng = np.random.default_rng(seed)
    ability = rng.standard_normal(n)
    school = 12 + 1.5 * ability + 2 * rng.standard_normal(n)
    lwage = 1 + 0.08 * school + 0.10 * ability + 0.4 * rng.standard_normal(n)
    score = ability + noise * rng.standard_normal(n)
    X = sm.add_constant(np.column_stack([school, score]))
    return sm.OLS(lwage, X).fit().params[1]


def percent(log_points):
    return np.exp(log_points) - 1


def any_rejection(k, alpha=0.05):
    return 1 - (1 - alpha) ** k


def bonferroni_z(k, alpha=0.05):
    from scipy import stats

    return stats.norm.isf(alpha / k / 2)


def corrected(slope, reliability):
    return slope / reliability


def brenland_food():
    """Problem: food on disposable income, size dummies, owner and an interaction."""
    import statsmodels.formula.api as smf
    from country import load

    h = load("households")
    h["lfood"] = np.log(h.food)
    h["linc"] = np.log(h.disposable)
    plain = smf.ols("lfood ~ linc", h).fit()
    sizes = smf.ols("lfood ~ linc + C(size) + owner", h).fit()
    inter = smf.ols("lfood ~ linc * owner + C(size)", h).fit()
    return h, plain, sizes, inter

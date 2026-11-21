"""Worked numbers of the exercises and weekend problem of b1 ch. 32.

Weekend problem: schooling and earnings in Brenland (households.csv, households with
positive gross income). Part III is a seeded extension: a cohort of 2,000 invented
people with an ability score, true return 0.05, ability effect 0.08.
"""

import numpy as np
import statsmodels.formula.api as smf
from country import load
from econdata import nsw


def problem():
    h = load("households").query("gross_income > 0").copy()
    h["ly"] = np.log(h.gross_income)
    fit = smf.ols("ly ~ school_years", data=h).fit()
    b0, b1 = fit.params
    se = fit.bse["school_years"]
    x = h.school_years
    # Part III: a simulated cohort with an ability score
    rng = np.random.default_rng(2026)
    n = 2_000
    ability = rng.standard_normal(n)
    school = np.round(12.6 + 1.2 * ability + rng.normal(0, 2.2, n))
    log_y = 9.4 + 0.05 * school + 0.08 * ability + rng.normal(0, 0.45, n)
    delta = np.polyfit(school, ability, 1)[0]
    short = np.polyfit(school, log_y, 1)[0]
    X = np.column_stack([np.ones(n), school, ability])
    long_ = np.linalg.lstsq(X, log_y, rcond=None)[0]
    with_age = smf.ols("ly ~ school_years + age_head", data=h).fit()
    return {
        "n": len(h),
        "b0": round(b0, 4),
        "b1": round(b1, 4),
        "se": round(se, 4),
        "t": round(b1 / se, 1),
        "r2": round(fit.rsquared, 4),
        "ci": (round(b1 - 1.96 * se, 4), round(b1 + 1.96 * se, 4)),
        "fitted12": round(b0 + 12 * b1, 3),
        "fitted16": round(b0 + 16 * b1, 3),
        "ratio16_12": round(np.exp(4 * b1), 3),
        "mean_x": round(x.mean(), 2),
        "sd_x": round(x.std(), 2),
        "resid_sum": float(fit.resid.sum()),
        "t_vs_010": round((b1 - 0.10) / se, 1),
        "level_slope": round(
            smf.ols("gross_income ~ school_years", data=h).fit().params.iloc[1], 0
        ),
        "delta": round(delta, 4),
        "short": round(short, 4),
        "long": round(long_[1], 4),
        "gamma_hat": round(long_[2], 4),
        "bias_true_gamma": round(0.08 * delta, 4),
        "bias_identity": round(long_[2] * delta, 4),
        "gap": round(short - long_[1], 4),
        "bias": round(short - 0.05, 4),
        "with_age": round(with_age.params["school_years"], 4),
        "age": round(with_age.params["age_head"], 4),
        "r_age": round(x.corr(h.age_head), 3),
    }


def exercises():
    x = np.array([8, 10, 12, 14, 16])
    y = np.array([9.4, 9.6, 9.9, 10.0, 10.3])
    b1 = ((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum()
    d = nsw("psid_controls").query("re78 > 0")
    fit = smf.ols("np.log(re78) ~ education", data=d).fit()
    ages = {}
    for name, q in (("under 30", "age < 30"), ("over 40", "age > 40")):
        s = d.query(q)
        f = smf.ols("np.log(re78) ~ education", data=s).fit()
        ages[name] = (
            len(s),
            round(f.params["education"], 4),
            round(f.bse["education"], 4),
        )
    return {
        "five": (round(b1, 4), round(y.mean() - b1 * x.mean(), 4)),
        "fitted16": round(fit.params.iloc[0] + 16 * fit.params.iloc[1], 3),
        "earn16": round(np.exp(fit.params.iloc[0] + 16 * fit.params.iloc[1]), 0),
        "ages": ages,
        "pct06": round(100 * (np.exp(0.06) - 1), 2),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem(), width=100)
    pprint.pprint(exercises())

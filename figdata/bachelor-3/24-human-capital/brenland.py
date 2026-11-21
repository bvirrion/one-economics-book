"""The last year of school in Brenland (weekend problem). Data: the household survey
(heads who work). Assumptions of the problem: a reform raises the minimum schooling
from 10 to 11 years for later cohorts, and everyone who would have left earlier
stays to 11; the reformed cohorts earn 2.9 log points more (reduced form); income
tax is proportional; a quarter of the measured return is a signal; the public cost
of a year of school is 30 % of the earnings a pupil gives up."""
import numpy as np
import statsmodels.formula.api as smf
from country import load

MIN_OLD, MIN_NEW, REDUCED, SIGNAL, PUBLIC = 10, 11, 0.029, 0.25, 0.30


def workers():
    h = load("households")
    w = h[h.hours > 0].copy()
    w["lw"] = np.log(w.gross_income)
    return w


def stats():
    w = workers()
    simple = smf.ols("lw ~ school_years", w).fit(cov_type="HC1")
    full = smf.ols("lw ~ school_years + age_head + I(age_head**2)", w).fit(
        cov_type="HC1")
    s = w.school_years
    first = (np.maximum(s, MIN_NEW) - s).mean()
    comp = s <= MIN_OLD
    wald = REDUCED / first
    return {"n": len(w), "mean_school": s.mean(), "b_simple": simple.params.iloc[1],
            "b_full": full.params["school_years"],
            "se_full": full.bse["school_years"],
            "complier_share": 100 * comp.mean(), "complier_mean": s[comp].mean(),
            "complier_gain": MIN_NEW - s[comp].mean(), "first_stage": first,
            "wald": 100 * wald, "private": 100 * wald,
            "social": 100 * wald * (1 - SIGNAL) / (1 + PUBLIC)}

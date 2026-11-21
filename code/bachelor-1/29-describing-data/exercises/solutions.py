"""Worked numbers of the exercises and weekend problem of b1 ch. 29.

Weekend problem: Brenland's household survey (2,000 households, 2025), described.
"""

import numpy as np
import pandas as pd
from country import load
from scipy.stats import skew


def problem():
    h = load("households")
    y = h.disposable
    counts, edges = np.histogram(y, bins=np.arange(0, 100_001, 10_000))
    logc, logedges = np.histogram(np.log10(y), bins=np.arange(3.8, 5.01, 0.2))
    top = y.sort_values(ascending=False)
    top10 = top.iloc[: len(y) // 10].sum() / y.sum()
    q = y.quantile([0.1, 0.5, 0.9])
    groups = pd.cut(
        h.school_years, [0, 11, 12, 15, 20], labels=["<12", "12", "13-15", "16+"]
    )
    by_school = h.groupby(groups, observed=True).gross_income.mean().round(0)
    h = h.assign(older=h.age_head >= 50, works=h.hours > 0)
    overall = h.groupby("older").disposable.mean()
    within = h.groupby(["works", "older"]).disposable.mean()
    share = h.groupby("older").works.mean()
    # the overall means as weighted averages of the within-group means
    rebuilt = {
        o: share[o] * within[(True, o)] + (1 - share[o]) * within[(False, o)]
        for o in (False, True)
    }
    # older households with the younger households' share working
    reweighted = (
        share[False] * within[(True, True)] + (1 - share[False]) * within[(False, True)]
    )
    return {
        "hist": counts.tolist(),
        "loghist": logc.tolist(),
        "mean": round(y.mean(), 1),
        "median": y.median(),
        "below_mean": round((y < y.mean()).mean(), 3),
        "sd": round(y.std(), 1),
        "skew": round(skew(y), 3),
        "skew_log": round(skew(np.log(y)), 3),
        "p10": q[0.1],
        "p50": q[0.5],
        "p90": q[0.9],
        "p90_p10": round(q[0.9] / q[0.1], 2),
        "top10": round(100 * top10, 1),
        "by_school": by_school.to_dict(),
        "r_school": round(h.school_years.corr(h.gross_income), 3),
        "r_school_log": round(
            h.school_years[h.gross_income > 0].corr(
                np.log(h.gross_income[h.gross_income > 0])
            ),
            3,
        ),
        "overall": overall.round(0).to_dict(),
        "gap": round(overall[False] - overall[True], 0),
        "within": within.round(0).to_dict(),
        "share_working": share.round(3).to_dict(),
        "rebuilt": {k: round(v, 0) for k, v in rebuilt.items()},
        "reweighted": round(reweighted, 0),
    }


def exercises():
    five = [2, 3, 3, 4, 18]
    town_mean_rise = 1e9 / 10_001
    return {
        "five": (np.mean(five), np.median(five)),
        "r": 12 / (3 * 5),
        "billionaire": round(town_mean_rise, 0),
        # Simpson by construction: department A admits most, B few
        "simpson": {
            "men": {"A": 80 / 100, "B": 10 / 50, "all": 90 / 150},
            "women": {"A": 18 / 20, "B": 30 / 130, "all": 48 / 150},
        },
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem(), width=100)
    pprint.pprint(exercises())

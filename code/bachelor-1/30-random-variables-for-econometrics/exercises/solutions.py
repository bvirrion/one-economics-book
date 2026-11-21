"""Worked numbers of the exercises and weekend problem of b1 ch. 30.

Weekend problem: the Brenland lottery of surveys. The 2,000 households of Brenland's
survey are the population; surveys of 100 households are drawn from it with
replacement (seed 2026), 10,000 times.
"""

import numpy as np
import pandas as pd
from country import load
from econdata import nsw
from scipy import stats


def problem(n=100, reps=10_000):
    h = load("households")
    y = h.disposable.to_numpy(float)
    bracket = pd.cut(
        h.disposable, [0, 20_000, 30_000, 1e9], labels=["<20k", "20-30k", "30k+"]
    )
    joint = pd.crosstab(h["size"], bracket, normalize=True)
    cond_mean = h.groupby("size").disposable.mean()
    p_size = h["size"].value_counts(normalize=True).sort_index()
    mu, sigma = y.mean(), y.std()
    rng = np.random.default_rng(2026)
    draws = rng.choice(y, size=(reps, n))
    means = draws.mean(axis=1)
    sds = draws.std(axis=1, ddof=1)
    half = np.quantile(np.abs(means - mu), 0.95)
    t = (means - mu) / (sds / np.sqrt(n))
    crit = stats.t.ppf(0.975, n - 1)
    return {
        "joint": joint.round(3),
        "p_size": p_size.round(3).to_dict(),
        "p_high_given_1": round(joint.loc[1, "30k+"] / joint.loc[1].sum(), 3),
        "p_high_given_4": round(joint.loc[4, "30k+"] / joint.loc[4].sum(), 3),
        "cond_mean": cond_mean.round(0).to_dict(),
        "lie": round((cond_mean * p_size).sum(), 3),
        "mu": round(mu, 3),
        "sigma": round(sigma, 1),
        "se": round(sigma / np.sqrt(n), 1),
        "sd_means": round(means.std(), 1),
        "half95": round(half, 0),
        "clt_half": round(1.96 * sigma / np.sqrt(n), 0),
        "t_share": round(np.mean(np.abs(t) > crit), 4),
        "crit": round(crit, 3),
        "t_sd": round(t.std(), 3),
    }


def exercises():
    y = nsw("psid_controls").re78.to_numpy()
    sigma = y.std()
    se200 = sigma / np.sqrt(200)
    return {
        "lin": (2 * 5 + 3, 4 * 2),
        "se120": round(sigma / np.sqrt(120), 0),
        "lie2": 0.4 * 10 + 0.6 * 20,
        "var_sum": 4 + 9 + 2 * 1.5,
        "ci200": (round(y.mean() - 1.96 * se200, 0), round(y.mean() + 1.96 * se200, 0)),
        "half200": round(1.96 * se200, 0),
        "cond": round(0.138 / 0.353, 3),
    }


if __name__ == "__main__":
    import pprint

    p = problem()
    print(p.pop("joint"))
    pprint.pprint(p, width=100)
    pprint.pprint(exercises())

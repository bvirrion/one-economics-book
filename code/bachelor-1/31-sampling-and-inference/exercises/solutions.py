"""Worked numbers of the exercises and weekend problem of b1 ch. 31.

Weekend problem: Brenland's labour-force survey (invented here). Three regions with
their labour force (millions) and true unemployment rates; 4,000 people sampled in each
region each month (12,000 in all), independently from month to month; true rates rise
by 0.2 point in every region in month 2. Seed 2028, chosen among 2020-2039 so that the
drawn change (0.30) is within half a standard error of the true 0.2: a typical draw.
The sample sizes of Part IV are planned from the true rates, not from the draw.
"""

import numpy as np
from econdata import nsw
from scipy import stats

REGIONS = {"Capital": (2.0, 0.050), "North": (1.5, 0.065), "South": (1.0, 0.0725)}
N_PER_REGION = 4_000


def survey(rise, rng):
    """Unemployed counts per region in one month's sample."""
    return {r: rng.binomial(N_PER_REGION, p + rise) for r, (_, p) in REGIONS.items()}


def estimate(counts):
    lf = np.array([REGIONS[r][0] for r in REGIONS])
    w_share = lf / lf.sum()
    p = np.array([counts[r] / N_PER_REGION for r in REGIONS])
    est = (w_share * p).sum()
    se = np.sqrt((w_share**2 * p * (1 - p) / N_PER_REGION).sum())
    return p, est, se


def problem():
    rng = np.random.default_rng(2028)
    m1, m2 = survey(0.0, rng), survey(0.002, rng)
    lf = np.array([REGIONS[r][0] for r in REGIONS])
    share = lf / lf.sum()
    prob = N_PER_REGION / (lf * 1e6)
    weight = 1 / prob
    n = 3 * N_PER_REGION
    w_each = np.repeat(weight, N_PER_REGION)
    deff = 1 + (w_each.std() / w_each.mean()) ** 2
    p1, est1, se1 = estimate(m1)
    p2, est2, se2 = estimate(m2)
    unweighted = sum(m1.values()) / n
    true = (share * np.array([p for _, p in REGIONS.values()])).sum()
    se_srs = np.sqrt(est1 * (1 - est1) / n)
    change = est2 - est1
    se_change = np.sqrt(se1**2 + se2**2)
    t = change / se_change
    pval = 2 * stats.norm.sf(abs(t))
    true_p = np.array([p for _, p in REGIONS.values()])
    se_true = np.sqrt((share**2 * true_p * (1 - true_p) / N_PER_REGION).sum())
    se_change_true = np.sqrt(2) * se_true
    need = 0.002 / (stats.norm.ppf(0.975) + stats.norm.ppf(0.8))
    n_need = n * (se_change_true / need) ** 2
    n_srs = 2 * true * (1 - true) / need**2
    n_overlap = n_need * (1 - 0.5)  # samples correlated at 0.5 halve the variance
    return {
        "share": share.round(3).tolist(),
        "true": round(100 * true, 3),
        "prob": [f"{x:.5f}" for x in prob],
        "weight": weight.round(0).tolist(),
        "deff": round(deff, 3),
        "counts1": m1,
        "counts2": m2,
        "p1": (100 * p1).round(2).tolist(),
        "se_regions": (100 * np.sqrt(p1 * (1 - p1) / N_PER_REGION)).round(3).tolist(),
        "unweighted": round(100 * unweighted, 3),
        "est1": round(100 * est1, 3),
        "se1": round(100 * se1, 4),
        "se_srs": round(100 * se_srs, 4),
        "ci1": (
            round(100 * (est1 - 1.96 * se1), 2),
            round(100 * (est1 + 1.96 * se1), 2),
        ),
        "est2": round(100 * est2, 3),
        "change": round(100 * change, 3),
        "se_change": round(100 * se_change, 4),
        "se_change_true": round(100 * se_change_true, 4),
        "t": round(t, 3),
        "p": round(pval, 3),
        "need": round(100 * need, 4),
        "need_month": round(100 * need / np.sqrt(2), 4),
        "n_need": round(n_need, -3),
        "n_srs": round(n_srs, -3),
        "n_overlap": round(n_overlap, -3),
    }


def exercises():
    d = nsw("nsw_dw")
    s1 = d.re78[d.treat == 1].std()
    s0 = d.re78[d.treat == 0].std()
    z = stats.norm.ppf(0.975) + stats.norm.ppf(0.8)
    # equal arms of size m: se = sqrt((s1^2 + s0^2) / m) = 1000 / z
    m = (s1**2 + s0**2) * (z / 1_000) ** 2
    # two proportions: 120 of 400 against 90 of 400
    pa, pb, pool = 120 / 400, 90 / 400, 210 / 800
    zp = (pa - pb) / np.sqrt(pool * (1 - pool) * (2 / 400))
    return {
        "se": 9_000 / np.sqrt(400),
        "s1": round(s1, 0),
        "s0": round(s0, 0),
        "m": round(m, 0),
        "z": round(z, 4),
        "zp": round(zp, 3),
        "pp": round(2 * stats.norm.sf(zp), 4),
        "false": 50 * 0.05,
        "bonf": 0.05 / 50,
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem(), width=100)
    pprint.pprint(exercises())

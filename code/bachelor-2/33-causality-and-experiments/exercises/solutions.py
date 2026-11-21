"""Worked numbers for Book 4, chapter 33 (exercises and the weekend problem).

The weekend problem's pilot is a seeded simulation of Brenland's training vouchers:
800 workers, earnings in dalens a year.
"""

import numpy as np

N, SEED = 800, 33


def population(seed=SEED, n=N):
    rng = np.random.default_rng(seed)
    drive = rng.standard_normal(n)  # unobserved motivation
    y0 = 24_000 + 3_000 * drive + 4_000 * rng.standard_normal(n)
    effect = 1_500 + 500 * drive
    return drive, y0, y0 + effect, rng


def rct(seed=SEED):
    """Half the workers drawn at random get a voucher."""
    drive, y0, y1, rng = population(seed)
    d = np.zeros(N, bool)
    d[rng.permutation(N)[: N // 2]] = True
    y = np.where(d, y1, y0)
    diff = y[d].mean() - y[~d].mean()
    se = np.sqrt(y[d].var(ddof=1) / d.sum() + y[~d].var(ddof=1) / (~d).sum())
    lo, hi = diff - 1.96 * se, diff + 1.96 * se
    sd0 = y[~d].std(ddof=1)
    return {
        "ate": (y1 - y0).mean(),
        "diff": diff,
        "se": se,
        "sd0": sd0,
        "lo": lo,
        "hi": hi,
    }


def rollout(seed=SEED):
    """Vouchers to those who apply: the more motivated apply."""
    drive, y0, y1, rng = population(seed)
    d = drive + rng.standard_normal(N) > 0
    y = np.where(d, y1, y0)
    att = (y1 - y0)[d].mean()
    bias = y0[d].mean() - y0[~d].mean()
    return {"diff": y[d].mean() - y[~d].mean(), "att": att, "bias": bias,
            "share": d.mean()}  # fmt: skip


def n_per_arm(delta, sigma, alpha=0.05, power=0.8):
    from scipy import stats

    z = stats.norm.isf(alpha / 2) + stats.norm.ppf(power)
    return 2 * z**2 * sigma**2 / delta**2


def any_imbalance(k, alpha=0.05):
    return 1 - (1 - alpha) ** k


CONTROLS = (
    "age + I(age**2) + education + black + hispanic + married + nodegree + re74 + re75"
)


def low_earners(cap=5000):
    """D exercise: survey men with 1975 earnings below `cap` as the comparison."""
    import pandas as pd
    import statsmodels.formula.api as smf
    from econdata import nsw

    exp = nsw("nsw_dw")
    cps = nsw("cps_controls")
    low = cps[cps.re75 < cap]
    d = pd.concat([exp.query("treat == 1"), low])
    raw = smf.ols("re78 ~ treat", d).fit(cov_type="HC1")
    adj = smf.ols("re78 ~ treat + " + CONTROLS, d).fit(cov_type="HC1")
    return len(low), raw.params.treat, raw.bse.treat, adj.params.treat, adj.bse.treat


def power(n_arm, delta, sigma):
    from scipy import stats

    return stats.norm.cdf(delta / (sigma * (2 / n_arm) ** 0.5) - stats.norm.isf(0.025))

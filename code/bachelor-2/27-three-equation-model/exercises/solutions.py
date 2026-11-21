"""Worked numbers for Book 4, chapter 27, in closed form.

IS x[t] = -a (r[t-1] - r*); PC pi[t] = pi[t-1] + alpha x[t];
loss (pi - target)**2 + lam x**2.
"""

from math import ceil, log


def ws_ps(b0, slope, ps):
    """Equilibrium unemployment where the wage-setting curve b0 - slope * u meets ps."""
    return (b0 - ps) / slope


def taylor1993(p, y):
    return p + 0.5 * y + 0.5 * (p - 2) + 2


def decay(alpha, lam):
    """Share of the inflation gap left after one period on the MR curve."""
    return 1 / (1 + alpha**2 / lam)


def rule_coef(alpha, lam, a):
    """r - r* = rule_coef * (pi - target)."""
    return alpha / (a * (lam + alpha**2))


def first_step(pi0, target, alpha, lam, a, r_star):
    pi1 = target + (pi0 - target) * decay(alpha, lam)
    x1 = -(alpha / lam) * (pi1 - target)
    r0 = r_star - x1 / a
    return pi1, x1, r0, r0 + pi0


def periods_below(gap0, alpha, lam, gap):
    return ceil(log(gap0 / gap) / log(1 / decay(alpha, lam)))


def cumulated_loss(gap0, alpha):
    return gap0 / alpha


def stability_factor(phi, a, alpha):
    """Next inflation gap over this one, if r - r* = (phi - 1)(pi - target)."""
    return 1 - a * alpha * (phi - 1)


def residuals_by_decade():
    """Funds rate minus the 1993 rule, quarterly 1960-2008, mean by decade."""
    import numpy as np
    from econdata import fed_series, sm_dataset
    from statsmodels.tsa.filters.hp_filter import hpfilter

    m = sm_dataset("macrodata")
    idx = [f"{int(y)}Q{int(q)}" for y, q in zip(m.year, m.quarter)]
    cpi = m.cpi.set_axis(idx)
    gap = 100 * hpfilter(np.log(m.realgdp.set_axis(idx)), lamb=1600)[0]
    infl = 100 * (cpi / cpi.shift(4) - 1)
    f = fed_series("h15", "RIFSPFF_N.M")
    keys = [f"{d.year}Q{(d.month - 1) // 3 + 1}" for d in f.date]
    ffr = f.value.groupby(keys).mean()
    dev = (ffr - taylor1993(infl, gap)).dropna()
    dev = dev[[("1960Q1" <= k <= "2008Q4") for k in dev.index]]
    dec = [int(k[:3]) * 10 for k in dev.index]
    return dev.groupby(dec).mean().round(2), dev.abs().groupby(dec).mean().round(2)


BRENLAND = {
    "target": 2.0,
    "alpha": 0.5,
    "lam": 0.5,
    "a": 0.5,
    "r_star": 2.0,
    "pi0": 5.0,
}


def zlb(pi, target, alpha, lam, a, r_star):
    """Desired nominal rate, rate set, desired and achieved next-period gap."""
    r = r_star + rule_coef(alpha, lam, a) * (pi - target)
    i = r + pi
    i_set = max(i, 0.0)
    return i, i_set, -a * (r - r_star), -a * (i_set - pi - r_star)

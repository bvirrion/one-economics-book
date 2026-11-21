"""Worked numbers for the exercises and the problem of Book 4, chapter 8."""

import numpy as np

S_Z = 0.25  # noise in supply in the Grossman--Stiglitz market of the chapter


def gs(c, a=1.0, s_theta2=1.0, s_eps2=1.0, s_z=S_Z):
    """Equilibrium informed share and Var(theta | price) at the cost c."""
    k = np.exp(2 * a * c) - 1
    target = k * s_eps2
    if target >= s_theta2:
        return 0.0, s_theta2
    su2 = target * s_theta2 / (s_theta2 - target)
    phi = min(1.0, a * s_eps2 * s_z / np.sqrt(su2))
    su2 = (a * s_eps2 / phi) ** 2 * s_z**2
    return phi, s_theta2 * su2 / (s_theta2 + su2)


def counts(households=2_000_000, goods=40):
    """Numbers a planner collects (Cobb-Douglas shares); prices a market posts."""
    return households * (goods - 1), goods - 1


def two_signal(s1, s2):
    """Naive and fully revealing prices, unit variances, equal groups."""
    return (s1 + s2) / 2, s1 + s2


def payback(odds, ret):
    """Win probability implied by a return at odds `odds`/1, and the odds' own."""
    return (1 + ret / 100) / (odds + 1), 1 / (odds + 1)


def iem():
    poll, eve, week = 1.91, 1.49, 1.58
    return 100 * (poll - eve) / poll, 100 * (poll - week) / poll, 9 / 15


def luck(wins=9, n=15):
    """Chance of at least `wins` successes in `n` fair coin flips."""
    from math import comb

    return sum(comb(n, k) for k in range(wins, n + 1)) / 2**n


def spending(c=0.1116):
    phi, _ = gs(c)
    return phi * c


def dual_track(qbar=18, pbar=20, p=30):
    """Mine with C(q) = q^2/2: output, plan and market sales, profits, transfer."""
    q = p
    cost = q**2 / 2
    dual = pbar * qbar + p * (q - qbar) - cost
    return q, q - qbar, dual, p * q - cost, (p - pbar) * qbar


def harvest(s_n=6, s_s=-2, var_s=16, var_e=9):
    """Problem parts I--II: variances and prices in Kestria's harvest market."""
    return {
        "var_h": 2 * var_s + var_e,
        "err_both": var_e,
        "err_one": var_s + var_e,
        "err_none": 2 * var_s + var_e,
        "naive": 100 + (s_n + s_s) / 2,
        "revealing": 100 + s_n + s_s,
        "demand_n_naive": (100 + s_n - (100 + (s_n + s_s) / 2)) / (var_s + var_e),
    }


def record(seed=808, seasons=12):
    """Problem part IV: a seeded record of the office and the market."""
    rng = np.random.default_rng(seed)
    base = 100 + rng.normal(0, 4, seasons) + rng.normal(0, 4, seasons)
    h = np.round(base + rng.normal(0, 3, seasons), 1)
    office = np.round(base + rng.normal(0, 2, seasons), 1)
    market = np.round(base + rng.normal(0, 1.5, seasons), 1)
    e_o, e_m = office - h, market - h
    return {
        "h": h,
        "office": office,
        "market": market,
        "mae_office": np.abs(e_o).mean(),
        "mae_market": np.abs(e_m).mean(),
        "msq_office": (e_o**2).mean(),
        "msq_market": (e_m**2).mean(),
        "market_closer": int((np.abs(e_m) < np.abs(e_o)).sum()),
        "mae_avg": np.abs((office + market) / 2 - h).mean(),
        "d_mean": (e_m**2 - e_o**2).mean(),
        "d_sd": (e_m**2 - e_o**2).std(ddof=1),
        "d_se": (e_m**2 - e_o**2).std(ddof=1) / np.sqrt(seasons),
    }


def seasons_needed(sd=17.8, diff=1.75):
    """Seasons for the expected difference to be two standard errors from zero."""
    return (2 * sd / diff) ** 2


def expected_msq():
    return 9 + 4, 9 + 2.25, 9 + (4 + 2.25) / 4


if __name__ == "__main__":
    for c in [0.05, 0.08, 0.1116, 0.2]:
        print(c, gs(c))
    print(counts(), two_signal(2, -0.5), payback(100, -61), payback(2, -5.5))
    print(iem(), harvest(), expected_msq())
    r = record()
    for k, v in r.items():
        print(k, v)

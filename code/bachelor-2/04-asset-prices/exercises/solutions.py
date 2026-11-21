"""Book 4, chapter 4 (asset prices): every number the solutions print."""

import math
from pathlib import Path

import numpy as np
import pandas as pd

OUT = Path(__file__).resolve().parents[4] / "figdata/bachelor-2/04-asset-prices/out"


def state_prices(price_bond, pay_bond, price_x, pay_x):
    """Two states; pay_* = (payoff in state 1, payoff in state 2)."""
    a = np.array([pay_bond, pay_x], dtype=float)
    return np.linalg.solve(a, np.array([price_bond, price_x], dtype=float))


def ex_state_prices():
    return state_prices(0.96, (1, 1), 1.1, (2, 0.5))


def ex_rf():
    return (1 / 0.98) * 1.02**2


def ex_capm():
    beta = 0.024 / 0.04
    return {"beta": beta, "er": 0.01 + beta * (0.07 - 0.01)}


def ex_premium_size():
    cov = 0.5 * 0.02 * 0.16
    return {"cov": cov, "g2": 2 * cov, "g10": 10 * cov, "need": 0.06 / cov}


def ex_geomean():
    from econdata import jst

    out = {}
    for iso in ("USA", "GBR"):
        d = jst(isos=[iso], since=1899, until=2020, cols=["eq_tr", "cpi"])
        infl = d.cpi.pct_change()
        r = ((1 + d.eq_tr) / (1 + infl) - 1)[d.year >= 1900]
        out[iso] = {
            "n": len(r),
            "arith": r.mean(),
            "geo": np.prod(1 + r) ** (1 / len(r)) - 1,
            "sd": r.std(),
        }
    return out


def ex_minvar():
    s1, s2 = 0.2, 0.1
    w1 = s2**2 / (s1**2 + s2**2)
    return {"w1": w1, "sd": math.sqrt(w1**2 * s1**2 + (1 - w1) ** 2 * s2**2)}


def ex_cumulative():
    c = pd.read_csv(OUT / "cumulative.csv").iloc[-1]
    return {k: (c[k], c[k] ** (1 / 71) - 1) for k in c.index if k != "year"}


def ex_gamble(gamma=25.0, h=0.2):
    """CRRA risk premium, as a share of wealth, of a 50-50 gamble of -h or +h."""
    eu = 0.5 * (1 - h) ** (1 - gamma) + 0.5 * (1 + h) ** (1 - gamma)
    return 1 - eu ** (1 / (1 - gamma))


def ex_gamma_needed():
    return pd.read_csv(OUT / "summary.csv").iloc[0]


def problem():
    q = state_prices(100, (105, 105), 95, (130, 80))
    prob = np.array([0.5, 0.5])
    m = q / prob
    rf = 1 / q.sum()
    er = (0.5 * 130 + 0.5 * 80) / 95
    call = 30 * q[0]
    # SDF from consumption: m_s = beta * g_s ** -gamma, g = (1.04, 0.98)
    gamma = math.log(m[1] / m[0]) / math.log(1.04 / 0.98)
    beta = m[0] * 1.04**gamma
    # covariance form of the premium
    r_eq = np.array([130, 80]) / 95
    cov_mr = (prob * (m - m.mean()) * (r_eq - er)).sum()
    # mean-variance, two risky assets
    me, mb, se, sb, rho = 0.07, 0.03, 0.18, 0.06, 0.2
    cov = rho * se * sb
    den = se**2 + sb**2 - 2 * cov

    def w_star(g):
        return (me - mb + g * (sb**2 - cov)) / (g * den)

    g_6040 = (me - mb) / (0.6 * den - (sb**2 - cov))
    w_min = (sb**2 - cov) / den
    sd_min = math.sqrt(
        w_min**2 * se**2 + (1 - w_min) ** 2 * sb**2 + 2 * w_min * (1 - w_min) * cov
    )
    # tangency with a safe rate of 2 per cent
    sig = np.array([[se**2, cov], [cov, sb**2]])
    z = np.linalg.solve(sig, np.array([me, mb]) - 0.02)
    wt = z / z.sum()
    mt = wt @ np.array([me, mb])
    st = math.sqrt(wt @ sig @ wt)

    def mv(w):
        mean = w * me + (1 - w) * mb
        var = w**2 * se**2 + (1 - w) ** 2 * sb**2 + 2 * w * (1 - w) * cov
        return mean, math.sqrt(var)

    pred = pd.read_csv(OUT / "brenland_predict.csv").iloc[0]
    lev3 = (mt - 0.02) / (3 * st**2)
    se_diff = pred.sd_eq * math.sqrt(1 / pred.n_up + 1 / pred.n_down)
    diff = pred.mean_after_up - pred.mean_after_down
    return {
        "q": q,
        "m": m,
        "rf": rf,
        "er": er,
        "prem": er - rf,
        "call": call,
        "arb_profit": call - 10,
        "gamma": gamma,
        "beta": beta,
        "cov_mr": cov_mr,
        "prem_cov": -rf * cov_mr,
        "w3": w_star(3),
        "w2": w_star(2),
        "w5": w_star(5),
        "g_6040": g_6040,
        "w_min": w_min,
        "sd_min": sd_min,
        "mv60": mv(0.6),
        "mv3": mv(w_star(3)),
        "wt": wt,
        "mt": mt,
        "st": st,
        "sharpe_t": (mt - 0.02) / st,
        "pred": pred,
        "lev3": lev3,
        "eq3_total": lev3 * wt[0],
        "sharpe60": (mv(0.6)[0] - 0.02) / mv(0.6)[1],
        "diff": diff,
        "se_diff": se_diff,
        "t_diff": diff / se_diff,
    }

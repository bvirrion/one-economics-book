"""Book 4, chapter 3 (intertemporal choice): every number the solutions print."""

import math
from pathlib import Path

import numpy as np
import pandas as pd

OUT = (
    Path(__file__).resolve().parents[4]
    / "figdata/bachelor-2/03-intertemporal-choice/out"
)


def pv(incomes, r):
    return sum(m / (1 + r) ** t for t, m in enumerate(incomes))


def ex_pv():
    return pv([30_000, 40_000, 50_000], 0.04)


def two_period_log(m0, m1, r, beta):
    """Two periods, u = ln: c0 = PV / (1 + beta), c1 = beta (1 + r) c0."""
    w = m0 + m1 / (1 + r)
    c0 = w / (1 + beta)
    return {"pv": w, "c0": c0, "c1": beta * (1 + r) * c0, "save": m0 - c0}


def ex_euler_log():
    return two_period_log(40_000, 42_000, 0.05, 0.95)


def ex_ce_table():
    t = pd.read_csv(OUT / "ce_age.csv").set_index("group")
    return t


def ex_crra_growth():
    r, rho, gamma = 0.04, 0.02, 2.0
    return {
        "approx": (r - rho) / gamma,
        "exact": ((1 + r) / (1 + rho)) ** (1 / gamma) - 1,
        "approx_half": (r - rho) / 0.5,
        "exact_half": ((1 + r) / (1 + rho)) ** 2 - 1,
    }


def c0_income_first(m0, r, beta, gamma):
    """All income in period 0, two periods, CRRA: first-period consumption."""
    return m0 / (1 + beta ** (1 / gamma) * (1 + r) ** (1 / gamma - 1))


def ex_rate_rise():
    return {
        g: (
            c0_income_first(100_000, 0.03, 0.96, g),
            c0_income_first(100_000, 0.06, 0.96, g),
        )
        for g in (2.0, 1.0, 0.5)
    }


def ex_borrowing():
    m0, m1, r, beta = 20_000, 60_000, 0.05, 0.95
    free = two_period_log(m0, m1, r, beta)
    mrs = m1 / m0  # u'(c0) / u'(c1) at the endowment, u = ln
    u_free = math.log(free["c0"]) + beta * math.log(free["c1"])
    u_lim = math.log(m0) + beta * math.log(m1)
    lam = math.exp((u_lim - u_free) / (1 + beta))  # share of resources kept
    return {**free, "mrs": mrs, "lam": lam, "cost": (1 - lam) * free["pv"]}


def ex_brenland():
    """Exercise 8: Brenland's survey by age band of the head, and the fitted slope."""
    from country import load

    h = load("households")
    h["band"] = pd.cut(h.age_head, [21, 30, 40, 50, 60, 70, 80], right=False)
    g = h.groupby("band", observed=True)[["disposable", "consumption"]].mean()
    g["ratio"] = g.consumption / g.disposable
    slope = np.polyfit(h.disposable, h.consumption, 1)[0]
    swing_m = g.disposable.max() / g.disposable.min()
    swing_c = g.consumption.max() / g.consumption.min()
    return {"table": g, "slope": slope, "swing_m": swing_m, "swing_c": swing_c}


def sophisticated_cake(w, phi):
    """Three periods, u = ln, long-run factor 1, present-bias factor phi, r = 0."""
    c0 = w / (1 + 2 * phi)
    w1 = w - c0
    c1 = w1 / (1 + phi)
    return {"c0": c0, "c1": c1, "c2": w1 - c1, "c1_planned": w1 / 2}


def ex_cake():
    return sophisticated_cake(90_000, 0.5)


def problem():
    m = [24_000, 60_000, 6_000]
    r, beta = 0.25, 0.8
    w = pv(m, r)
    k = 1 + beta + beta**2
    c = w / k  # flat: beta (1 + r) = 1
    b0 = m[0] - c
    b1 = b0 * (1 + r) + m[1] - c
    # r = 0.5: c0 = PV / (1 + beta + beta^2) still (log utility)
    w5 = pv(m, 0.5)
    c05 = w5 / k
    # borrowing limit b0 >= 0
    w1 = m[1] + m[2] / (1 + r)
    c1_lim = w1 / (1 + beta)
    u_free = k * math.log(c)
    u_lim = math.log(m[0]) + (beta + beta**2) * math.log(c1_lim)
    cbar = math.exp(u_lim / k)
    # present bias phi = 0.7, sophisticated (= naive under log)
    phi = 0.7
    s0 = w / (1 + phi * beta * (1 + beta))
    w1p = (w - s0) * (1 + r)
    s1 = w1p / (1 + phi * beta)
    s2 = (w1p - s1) * (1 + r)
    commit = w1p / (1 + beta)  # c1 = c2 under commitment, beta (1 + r) = 1
    # self 0's utility (weights 1, phi beta, phi beta^2) without and with commitment
    u0_no = math.log(s0) + phi * beta * math.log(s1) + phi * beta**2 * math.log(s2)
    u0_c = (
        math.log(s0) + phi * beta * math.log(commit) + phi * beta**2 * math.log(commit)
    )
    # value: the extra dalens at period 1 (no commitment) that give self 0 the same
    # utility; with log, scaling w1 by x raises self-0 utility by phi beta (1+beta) ln x
    x = math.exp((u0_c - u0_no) / (phi * beta * (1 + beta)))
    # long-run (exponential) utility of the two paths
    lr_no = math.log(s0) + beta * math.log(s1) + beta**2 * math.log(s2)
    lr_c = math.log(s0) + (beta + beta**2) * math.log(commit)
    u_hand = math.log(m[0]) + beta * math.log(m[1]) + beta**2 * math.log(m[2])
    return {
        "u_hand": u_hand,
        "c_hand": math.exp(u_hand / k),
        "c_pay": (w - 1000) / k,
        "pv": w,
        "c": c,
        "b0": b0,
        "b1": b1,
        "check": b1 * (1 + r) + m[2] - c,
        "pv5": w5,
        "c05": c05,
        "c15": c05 * 1.2,
        "c25": c05 * 1.44,
        "w1": w1,
        "c1_lim": c1_lim,
        "u_free": u_free,
        "u_lim": u_lim,
        "cbar": cbar,
        "cost_per": c - cbar,
        "cost_pv": (c - cbar) * k,
        "s0": s0,
        "w1p": w1p,
        "s1": s1,
        "s2": s2,
        "commit": commit,
        "x": x,
        "value": (x - 1) * w1p,
        "value0": (x - 1) * w1p / (1 + r),
        "lr_no": lr_no,
        "lr_c": lr_c,
    }

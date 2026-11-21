"""A cash transfer for Brenland's poorest (weekend problem).

The poverty line is 60 % of the median of disposable income per person in the 2025
household survey (households.csv), counted over people (household size as weight).
The invented programme covers every household below the line. Half of them, drawn
at random (seed 34), receive a one-time transfer whose size is itself drawn at
random among 3,000, 6,000 and 9,000 dalens; the other half are controls. Each
household has invented productive assets a0 (lognormal, median 2,000 dalens, seed
34). After two years assets are (a0 + T) x 1.25 when a0 + T is at least 7,000
dalens (the threshold) and (a0 + T) x 0.55 otherwise; controls keep 0.95 a0.
Consumption per person after two years is baseline consumption per person x
exp(0.04 + e), e ~ N(0, 0.08), plus 0.20 x (a2 - 0.95 a0) / size. Administration
costs 10 % of the transfers."""
import numpy as np
import pandas as pd
from country import load

THRESHOLD, ADMIN = 7000.0, 0.10
SIZES = [3000.0, 6000.0, 9000.0]


def line():
    h = load("households")
    pc = h.disposable / h["size"]
    return 0.6 * weighted_median(pc, h["size"])


def weighted_median(x, w):
    o = np.argsort(np.asarray(x))
    x, w = np.asarray(x)[o], np.asarray(w)[o]
    c = np.cumsum(w)
    return float(x[np.searchsorted(c, c[-1] / 2)])


def experiment():
    h = load("households")
    z = line()
    pc = h.disposable / h["size"]
    d = h[pc < z].copy().reset_index(drop=True)
    rng = np.random.default_rng(34)
    n = len(d)
    treat = np.zeros(n, dtype=bool)
    treat[rng.permutation(n)[: n // 2]] = True
    T = np.where(treat, rng.choice(SIZES, n), 0.0)
    a0 = 2000 * np.exp(rng.normal(0, 0.5, n))
    total = a0 + T
    a2 = np.where(treat, np.where(total >= THRESHOLD, 1.25, 0.55) * total, 0.95 * a0)
    c0 = d.consumption / d["size"]
    growth = np.exp(0.04 + rng.normal(0, 0.08, n))
    c2 = c0 * growth + 0.20 * (a2 - 0.95 * a0) / d["size"]
    return pd.DataFrame({"hh": d.hh, "size": d["size"],
                         "inc_pc": pc[pc < z].to_numpy(),
                         "c0": c0, "treat": treat, "T": T, "a0": a0, "a2": a2,
                         "c2": c2})


def effect(e):
    t, c = e[e.treat], e[~e.treat]
    diff = t.c2.mean() - c.c2.mean()
    se = np.sqrt(t.c2.var(ddof=1) / len(t) + c.c2.var(ddof=1) / len(c))
    return diff, se


def stats():
    from fgt import fgt
    h = load("households")
    pc = h.disposable / h["size"]
    z = line()
    e = experiment()
    diff, se = effect(e)
    t, c = e[e.treat], e[~e.treat]
    above_t, above_c = (t.c2 >= z).mean(), (c.c2 >= z).mean()
    cost = (1 + ADMIN) * t["T"].sum()
    lifted = (above_t - above_c) * len(t)
    out = {"z": z, "median_pc": z / 0.6, "people": h["size"].sum(),
           "p0": 100 * fgt(pc, z, 0, h["size"]), "p1": 100 * fgt(pc, z, 1, h["size"]),
           "p2": 100 * fgt(pc, z, 2, h["size"]),
           "gap_total": float(((z - pc).clip(lower=0) * h["size"]).sum()),
           "n_poor_hh": len(e), "n_treat": len(t), "n_control": len(c),
           "c0_t": t.c0.mean(), "c0_c": c.c0.mean(),
           "c2_t": t.c2.mean(), "c2_c": c.c2.mean(), "effect": diff, "se": se,
           "lo": diff - 1.96 * se, "hi": diff + 1.96 * se,
           "above_t": 100 * above_t, "above_c": 100 * above_c,
           "mean_T": t["T"].mean(), "cost": cost, "lifted": lifted,
           "cost_per_lifted": cost / lifted}
    for size in [0.0] + SIZES:
        s = c if size == 0 else t[t["T"] == size]
        k = int(size)
        out[f"n_{k}"] = len(s)
        out[f"a0_{k}"] = s.a0.mean()
        out[f"a2_{k}"] = s.a2.mean()
        out[f"above_{k}"] = 100 * (s.c2 >= z).mean()
        out[f"cross_{k}"] = 100 * ((s.a0 + s["T"]) >= THRESHOLD).mean()
    return out

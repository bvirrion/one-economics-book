"""Brenland and the land across the river (weekend problem). All data invented.

Two provinces on either bank of the Varn, North and South, share one path until 1995
(log income per person ln 20,000 + 1.5 % a year + common shocks). In 1995 North
gives farmers and firms registered titles; from 1996 its trend growth is 2.9 % a year,
while South stays at 1.5 %. Eight other provinces (the donors) have their own levels
and trend growth between 1.0 and 2.0 % a year and no reform. Noise: common shocks of
sd 0.01, province noise of sd 0.004 (seed 32).

A cross-section of 60 districts in 2025 (30 on each bank, seed 320): soil quality q
~ N(0, 1); distance z (km, uniform 0--100) to the land-survey office of 1890, which
titled plots near it first; titled share s = 0.30 + 0.30 North - 0.004 z + 0.05 q +
noise (sd 0.04); ln income = 9.9 + 1.0 s + 0.10 North + 0.15 q + noise (sd 0.08).
The true effect of the titled share is 1.0; soil raises both, so OLS is biased up."""
import numpy as np
import pandas as pd
from scipy.optimize import minimize

YEARS = np.arange(1980, 2026)
REFORM = 1995
DONOR_G = [0.010, 0.012, 0.014, 0.015, 0.016, 0.017, 0.019, 0.020]
DONOR_A = [-0.15, 0.10, -0.05, 0.20, -0.20, 0.05, -0.10, 0.15]


def panel():
    rng = np.random.default_rng(32)
    t = YEARS - 1980
    common = np.cumsum(rng.normal(0, 0.01, len(YEARS)))
    base = np.log(20000) + common
    post = np.clip(YEARS - REFORM, 0, None)
    d = {"North": base + 0.015 * t + 0.014 * post + rng.normal(0, 0.004, len(t)),
         "South": base + 0.015 * t + rng.normal(0, 0.004, len(t))}
    for k, (a, g) in enumerate(zip(DONOR_A, DONOR_G)):
        d[f"D{k + 1}"] = base + a + g * t + rng.normal(0, 0.004, len(t))
    return pd.DataFrame(d, index=YEARS)


def synth(p, treated="North", donors=None):
    donors = donors or [c for c in p.columns if c.startswith("D")]
    pre = p.loc[:REFORM]
    X, y = pre[donors].to_numpy(), pre[treated].to_numpy()
    n = len(donors)
    res = minimize(lambda w: ((X @ w - y) ** 2).sum(), np.full(n, 1 / n),
                   bounds=[(0, 1)] * n, method="SLSQP",
                   constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1}],
                   options={"ftol": 1e-14, "maxiter": 500})
    w = pd.Series(res.x, index=donors)
    return w, p[donors] @ w


def districts():
    rng = np.random.default_rng(320)
    north = np.r_[np.ones(30), np.zeros(30)]
    q = rng.normal(0, 1, 60)
    z = rng.uniform(0, 100, 60)
    s = 0.30 + 0.30 * north - 0.004 * z + 0.05 * q + rng.normal(0, 0.04, 60)
    lny = 9.9 + 1.0 * s + 0.10 * north + 0.15 * q + rng.normal(0, 0.08, 60)
    return pd.DataFrame({"north": north, "z": z, "s": s, "lny": lny})


def slope(x, y):
    x, y = np.asarray(x), np.asarray(y)
    return np.cov(x, y, ddof=0)[0, 1] / np.var(x)


def iv(d):
    fs, rf = slope(d.z, d.s), slope(d.z, d.lny)
    e = d.s - d.s.mean() - fs * (d.z - d.z.mean())
    se = np.sqrt((e @ e) / (len(d) - 2) / ((d.z - d.z.mean()) ** 2).sum())
    return {"ols": slope(d.s, d.lny), "fs": fs, "rf": rf, "tsls": rf / fs,
            "F": (fs / se) ** 2}


def required_p(log_gap, p_north, a=1 / 3):
    """Expropriation probability in South that gives the log output gap, with
    output proportional to (1 - p) ** (a / (1 - a))."""
    return 1 - (1 - p_north) * np.exp(-log_gap * (1 - a) / a)


def stats():
    p = panel()
    y = np.exp(p)
    w, sc = synth(p)
    pre = p.loc[:REFORM]
    rmse = np.sqrt(((pre.North - sc.loc[:REFORM]) ** 2).mean())
    d = districts()
    r = iv(d)
    gs = d.groupby("north")
    ds = gs.s.mean()[1] - gs.s.mean()[0]
    dy = gs.lny.mean()[1] - gs.lny.mean()[0]
    did = (p.North[2025] - p.North[REFORM]) - (p.South[2025] - p.South[REFORM])
    out = {f"{b}{yr}": y[b][yr] for b in ("North", "South")
           for yr in (1980, 1995, 2025)}
    out.update({
        "gap1995": 100 * (p.North[1995] - p.South[1995]),
        "gap2025": 100 * (p.North[2025] - p.South[2025]),
        "gN_pre": 100 * (p.North[1995] - p.North[1980]) / 15,
        "gS_pre": 100 * (p.South[1995] - p.South[1980]) / 15,
        "gN_post": 100 * (p.North[2025] - p.North[1995]) / 30,
        "gS_post": 100 * (p.South[2025] - p.South[1995]) / 30,
        "did": 100 * did, "rmse": 100 * rmse,
        "synth_gap2025": 100 * (p.North[2025] - sc[2025]),
        **{f"w_{k}": round(v, 4) for k, v in w.items()},
        **r, "ds": ds, "dy": dy, "share": 100 * r["tsls"] * ds / dy,
        "share_ols": 100 * r["ols"] * ds / dy,
        "p_south": required_p(r["tsls"] * ds, 0.05)})
    return out

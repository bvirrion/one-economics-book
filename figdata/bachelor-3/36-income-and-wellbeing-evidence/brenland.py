"""Fifty years of Brenland, in one number (weekend problem).

GDP per person (2015 dalens): 2025 from accounts.csv; 1975 from the series of the
growth-empirics chapter (2000 back to 1975 at 2.0 % a year for 1996--2000, 4.0 % for
1982--1995 and 0.5 % for 1976--1981). Consumption share: C / GDP in accounts.csv for
2025, and for 1975 the 2000 share (invented). Invented: life expectancy 72.0 years in
1975 and 81.0 in 2025; hours worked per person 900 a year in 1975 and 760 in 2025; the
Gini of consumption per person 0.27 in 1975 (the 2025 one is computed from the
household survey, people weighted). Kestria in 2025: income 27,700 dalens of 2015 (the
series' convention), consumption share 0.60, life expectancy 79.0, hours 820, Gini
0.33 (invented). Reference: Brenland 2025, with KAPPA = 5."""

import numpy as np
from country import load
from welfare import YEAR_HOURS, log_lambda, sigma_from_gini, theta

BACK = 5 * 0.02 + 14 * 0.04 + 6 * 0.005


def gini(x, w):
    o = np.argsort(x)
    x, w = np.asarray(x, float)[o], np.asarray(w, float)[o]
    cw = np.cumsum(w) / w.sum()
    cx = np.cumsum(x * w) / (x * w).sum()
    return 1 - np.sum((cw - np.r_[0, cw[:-1]]) * (cx + np.r_[0, cx[:-1]]))


def inputs():
    a = load("accounts").set_index("year")
    y = a.real_gdp / a["pop"] * 1000
    h = load("households")
    g25 = gini(h.consumption / h["size"], h["size"])
    return {
        "b75": {
            "y": y[2000] * np.exp(-BACK),
            "cs": a.C[2000] / a.gdp[2000],
            "e": 72.0,
            "hours": 900.0,
            "gini": 0.27,
        },
        "b25": {
            "y": y[2025],
            "cs": a.C[2025] / a.gdp[2025],
            "e": 81.0,
            "hours": 760.0,
            "gini": g25,
        },
        "k25": {"y": 27700.0, "cs": 0.60, "e": 79.0, "hours": 820.0, "gini": 0.33},
    }


def welfare(kappa=5.0):
    d = inputs()
    for v in d.values():
        v["c"] = v["y"] * v["cs"]
        v["h"] = v["hours"] / YEAR_HOURS
        v["sig"] = float(sigma_from_gini(v["gini"]))
    r = d["b25"]
    th = theta(r["y"], r["c"], r["h"])
    out = {"theta": th}
    for k in ("b75", "k25"):
        v = d[k]
        ll, parts = log_lambda(
            v["e"],
            v["c"],
            v["h"],
            v["sig"],
            r["e"],
            r["c"],
            r["h"],
            r["sig"],
            th,
            kappa,
        )
        out[k] = {**v, "ll": float(ll), **{p: float(x) for p, x in parts.items()}}
    out["b25"] = r
    return out


def stats():
    w = welfare()
    b75, b25, k25 = w["b75"], w["b25"], w["k25"]
    s = {"theta": w["theta"]}
    for name, v in (("b75", b75), ("b25", b25), ("k25", k25)):
        for f in ("y", "cs", "c", "e", "hours", "h", "gini", "sig"):
            s[f"{name}_{f}"] = v[f]
    for name, v in (("b75", b75), ("k25", k25)):
        for f in ("ll", "life", "cons", "leisure", "ineq"):
            s[f"{name}_{f}"] = v[f]
    s["g_gdp"] = 100 * np.log(b25["y"] / b75["y"]) / 50
    s["g_cons"] = 100 * np.log(b25["c"] / b75["c"]) / 50
    s["g_welfare"] = -100 * b75["ll"] / 50
    s["k_gdp_ratio"] = 100 * k25["y"] / b25["y"]
    s["k_welfare"] = 100 * np.exp(k25["ll"])
    s["g_welfare_k3"] = -100 * welfare(3.0)["b75"]["ll"] / 50
    s["g_welfare_k7"] = -100 * welfare(7.0)["b75"]["ll"] / 50
    return s

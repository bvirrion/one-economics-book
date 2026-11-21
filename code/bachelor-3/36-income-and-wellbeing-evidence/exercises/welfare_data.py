"""Shared by exercises 5 and 11: consumption-equivalent welfare relative to the United
States, 2019, as in the chapter (PWT 11.0, WDI life expectancy and Gini)."""

import numpy as np
from econdata import pwt, wdi
from scipy.stats import norm


def countries():
    p = pwt(
        since=2019, until=2019, cols=["rgdpe", "pop", "csh_c", "avh", "emp"]
    ).dropna()
    p["y"] = p.rgdpe / p["pop"]
    p["c"] = p.y * p.csh_c
    p["h"] = p.avh * p.emp / p["pop"] / 5840
    e = wdi("SP.DYN.LE00.IN", since=2019, until=2019, countries_only=True)
    g = wdi("SI.POV.GINI", since=2010, until=2019, countries_only=True)
    g = g.dropna(subset=["value"]).sort_values("year").groupby("iso3").tail(1)
    d = p.merge(e[["iso3", "value"]].rename(columns={"value": "e"}), on="iso3")
    d = d.merge(g[["iso3", "value"]].rename(columns={"value": "gini"}), on="iso3")
    d = d.dropna().reset_index(drop=True)
    d["sig"] = np.sqrt(2) * norm.ppf((1 + d.gini / 100) / 2)
    return d


def log_welfare(d, kappa):
    u0 = d.set_index("iso3").loc["USA"]
    th = 0.6 * (u0.y / u0.c) / u0.h**2
    dv = th * (d.h**2 - u0.h**2) / 2
    ds = (d.sig**2 - u0.sig**2) / 2
    u = kappa + np.log(d.c / u0.c) - dv - ds
    return (d.e - u0.e) / u0.e * u + np.log(d.c / u0.c) - dv - ds

"""Exercise 5: absolute convergence, 1960--2019, in three samples of PWT 11.0: all
countries with data in both years, the 25 richest in 1960, and the 25 richest in 2019.
Regress annual growth of real GDP per person (national accounts, rgdpna) on ln income
in 1960 (expenditure side, rgdpe, comparable across countries)."""
import numpy as np
from econdata import pwt

p = pwt(cols=["rgdpe", "rgdpna", "pop"])
p["y"], p["ya"] = p.rgdpe / p["pop"], p.rgdpna / p["pop"]
w = p.pivot(index="year", columns="iso3", values="y").loc[[1960, 2019]]
a = p.pivot(index="year", columns="iso3", values="ya").loc[[1960, 2019]]
ok = w.dropna(axis=1).columns.intersection(a.dropna(axis=1).columns)
w, a = w[ok], a[ok]
x, g = np.log(w.loc[1960]), np.log(a.loc[2019] / a.loc[1960]) / 59
samples = {"all": ok,
           "richest 25 in 1960": x.sort_values().index[-25:],
           "richest 25 in 2019": np.log(w.loc[2019]).sort_values().index[-25:]}
for name, idx in samples.items():
    b = np.polyfit(x[idx], g[idx], 1)[0]
    print(f"{name:19s} slope {b:+.4f} ({len(idx)} countries)")

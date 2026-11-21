"""Exercise 6: how persistent is growth? Correlation of countries' annual growth of real
GDP per person (PWT 11.0, national accounts, rgdpna) in one decade with the next, and of
the log level of income (expenditure side, rgdpe) at the start of one decade with the
next."""
import numpy as np
from econdata import pwt

p = pwt(cols=["rgdpe", "rgdpna", "pop"])
p["y"], p["ya"] = p.rgdpe / p["pop"], p.rgdpna / p["pop"]
w = p.pivot(index="year", columns="iso3", values="y")
v = p.pivot(index="year", columns="iso3", values="ya")
ends = [1960, 1970, 1980, 1990, 2000, 2010, 2019]
for a, b, c in zip(ends, ends[1:], ends[2:]):
    ok = w.loc[[a, b]].dropna(axis=1).columns.intersection(
        v.loc[[a, b, c]].dropna(axis=1).columns)
    g1, g2 = np.log(v.loc[b, ok] / v.loc[a, ok]), np.log(v.loc[c, ok] / v.loc[b, ok])
    r_g = np.corrcoef(g1, g2)[0, 1]
    r_y = np.corrcoef(np.log(w.loc[a, ok]), np.log(w.loc[b, ok]))[0, 1]
    print(f"{a}s to {b}s: growth {r_g:+.2f}, level {r_y:.2f} ({len(ok)} countries)")

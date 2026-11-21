"""Exercise 12: current-account reversals, 1990--2024 (WDI).

A reversal: the current account (percent of GDP) was a deficit of at least 4 in year
t - 1 and rose by at least 4 points by year t + 1. One episode per country within
any three years; countries of over a million people. Reports the mean current
account and GDP growth around the episodes.
"""
import pandas as pd
from econdata import wdi, wdi_countries

c = wdi_countries()
real = set(c.loc[c.Region.notna(), "Country Code"])
pop = wdi("SP.POP.TOTL", since=2024, until=2024).set_index("iso3").value
real = {iso for iso in real if pop.get(iso, 0) >= 1e6}
ca = wdi("BN.CAB.XOKA.GD.ZS", since=1990, until=2024).rename(columns={"value": "ca"})
gr = wdi("NY.GDP.MKTP.KD.ZG", since=1990, until=2024).rename(columns={"value": "g"})
d = ca.merge(gr[["iso3", "year", "g"]], on=["iso3", "year"])
d = d[d.iso3.isin(real)].set_index(["iso3", "year"]).sort_index()

rows = []
for iso, s in d.groupby(level=0):
    s = s.droplevel(0)
    last = -10
    for t in s.index:
        if {t - 2, t - 1, t + 1} <= set(s.index) and t - last > 3:
            if s.ca[t - 1] <= -4 and s.ca[t + 1] - s.ca[t - 1] >= 4:
                rows.append({"iso3": iso, "year": t,
                             **{f"ca{k}": s.ca[t + k] for k in (-1, 0, 1)},
                             **{f"g{k}": s.g[t + k] for k in (-2, -1, 0, 1)}})
                last = t
e = pd.DataFrame(rows).dropna()
print(f"reversals: {len(e)} in {e.iso3.nunique()} countries")
print("current account (% of GDP), t-1, t, t+1: "
      + ", ".join(f"{e[f'ca{k}'].mean():.1f}" for k in (-1, 0, 1)))
print("GDP growth (%), t-2, t-1, t, t+1: "
      + ", ".join(f"{e[f'g{k}'].mean():.1f}" for k in (-2, -1, 0, 1)))

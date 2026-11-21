"""Exercise 5: half-lives of real exchange rates against the dollar (JST data).

q = log(local currency per dollar) + log(U.S. CPI) - log(local CPI). An AR(1) by OLS
on consecutive years, q_t = a + rho q_{t-1}, gives the half-life ln(0.5) / ln(rho).
"""
import numpy as np
from econdata import jst

j = jst(cols=["xrusd", "cpi"], since=1870, until=2020)
us = j[j.iso3 == "USA"].set_index("year").cpi
j = j[j.iso3 != "USA"].copy()
j["q"] = np.log(j.xrusd) + np.log(j.year.map(us)) - np.log(j.cpi)


def half_life(g):
    s = g.set_index("year").q.dropna().sort_index()
    prev = s.shift(1)
    ok = prev.notna() & (s.index.to_series().diff() == 1)
    rho = np.polyfit(prev[ok], s[ok], 1)[0]
    return rho, np.log(0.5) / np.log(rho)


print("economy  rho 1870-2020  half-life  rho 1974-2020  half-life")
lives = {"all": [], "float": []}
for iso, g in j.groupby("iso3"):
    r1, h1 = half_life(g)
    r2, h2 = half_life(g[g.year >= 1974])
    lives["all"].append(h1)
    lives["float"].append(h2)
    print(f"{iso}      {r1:.3f}         {h1:5.1f}      {r2:.3f}         {h2:5.1f}")
print(f"median half-life: {np.median(lives['all']):.1f} years (1870-2020), "
      f"{np.median(lives['float']):.1f} years (1974-2020)")

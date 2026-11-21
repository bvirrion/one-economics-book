"""Convergence across countries; postwar recovery; Brenland's Solow paths.

Grade 12, chapter 5 (the Solow model, a first look).
Penn World Table 11.0: GDP per person in 1960 (rgdpe / pop, 2021 dollars at chained PPPs) and average annual growth of
GDP per person 1960-2019 (rgdpna / pop, geometric, per cent); countries with both years. Group "eur" = 20 countries of
western Europe, the United States, Canada and Turkey (AUT BEL CAN CHE DEU DNK ESP FRA GBR GRC IRL ISL ITA LUX NLD NOR
PRT SWE TUR USA); correlation of growth with log income 1960 in each group.
Maddison Project Database: GDP per person, DEU, JPN, USA, 1938-1973.
Brenland (invented): s = I / GDP in 2025 (accounts.csv), alpha = 0.35, delta = 0.05; A from output and capital per worker
in 2025 (chapter 4's capital stock); k(t+1) = s A k(t)^alpha + (1 - delta) k(t); no population or technology growth.
Writes:
  out/conv.csv        iso3, y1960, g, eur   (eur 1 or 0)
  out/conv_key.csv    n, n_eur, corr_all, corr_eur
  out/recovery.csv    year, DEU, JPN, USA
  out/paths.csv       t, low, high, rise   (k, thousands of 2015 dalens per worker)
  out/solow_key.csv   s, A, kstar, ystar, k2025, y2025, half_now, s2, kstar2, ystar2, half_rise
"""
import numpy as np
import pandas as pd

import country
from econdata import maddison, pwt
from figout import write_table

EUR = "AUT BEL CAN CHE DEU DNK ESP FRA GBR GRC IRL ISL ITA LUX NLD NOR PRT SWE TUR USA".split()
ALPHA, DELTA, S2 = 0.35, 0.05, 0.25
K2025, Y2025 = 218.42, 66.97      # chapter 4, bren.csv (thousands of 2015 dalens per worker)


def convergence():
    p = pwt(since=1960, until=2019, cols=["rgdpe", "rgdpna", "pop"]).set_index(["iso3", "year"])
    rows = []
    for iso in sorted(set(p.index.get_level_values(0))):
        d = p.loc[iso]
        if 1960 not in d.index or 2019 not in d.index:
            continue
        a, b = d.loc[1960], d.loc[2019]
        if a[["rgdpe", "rgdpna", "pop"]].isna().any() or b[["rgdpna", "pop"]].isna().any():
            continue
        g = 100 * (((b.rgdpna / b["pop"]) / (a.rgdpna / a["pop"])) ** (1 / 59) - 1)
        rows.append({"iso3": iso, "y1960": round(a.rgdpe / a["pop"]), "g": round(g, 2), "eur": int(iso in EUR)})
    t = pd.DataFrame(rows)
    e = t[t.eur == 1]
    key = pd.DataFrame([{"n": len(t), "n_eur": len(e),
                         "corr_all": round(float(np.corrcoef(np.log(t.y1960), t.g)[0, 1]), 3),
                         "corr_eur": round(float(np.corrcoef(np.log(e.y1960), e.g)[0, 1]), 3)}])
    return t, key


def recovery():
    m = maddison(isos=["DEU", "JPN", "USA"], since=1938, until=1973)
    t = m.pivot(index="year", columns="iso3", values="gdppc")[["DEU", "JPN", "USA"]].round(0)
    t.columns.name = None
    return t.reset_index()


def step(k, s, A):
    return s * A * k ** ALPHA + (1 - DELTA) * k


def half_time(k0, s, A):
    ks = (s * A / DELTA) ** (1 / (1 - ALPHA))
    k, t = k0, 0
    while abs(ks - k) > abs(ks - k0) / 2:
        k, t = step(k, s, A), t + 1
    return t


def brenland():
    a = country.load("accounts").set_index("year")
    s = float(a.I.loc[2025] / a.gdp.loc[2025])
    A = Y2025 / K2025 ** ALPHA
    kstar = (s * A / DELTA) ** (1 / (1 - ALPHA))
    kstar2 = (S2 * A / DELTA) ** (1 / (1 - ALPHA))
    rows, lo, hi, ri = [], 100.0, 600.0, kstar
    for t in range(0, 101):
        rows.append({"t": t, "low": round(lo, 2), "high": round(hi, 2), "rise": round(ri, 2)})
        lo, hi, ri = step(lo, s, A), step(hi, s, A), step(ri, S2, A)
    key = pd.DataFrame([{"s": round(s, 4), "A": round(A, 4), "kstar": round(kstar, 1), "ystar": round(A * kstar ** ALPHA, 2),
                         "k2025": K2025, "y2025": Y2025, "half_now": half_time(K2025, s, A), "s2": S2,
                         "kstar2": round(kstar2, 1), "ystar2": round(A * kstar2 ** ALPHA, 2), "half_rise": half_time(kstar, S2, A)}])
    return pd.DataFrame(rows), key


if __name__ == "__main__":
    t, key = convergence()
    write_table(t, __file__, "conv")
    write_table(key, __file__, "conv_key")
    write_table(recovery(), __file__, "recovery")
    paths, skey = brenland()
    write_table(paths, __file__, "paths")
    write_table(skey, __file__, "solow_key")

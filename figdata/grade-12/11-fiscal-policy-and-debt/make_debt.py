"""Public debt ratios: the UK and US since 1870; euro-area countries since 2000; the UK's fall 1946-1975 decomposed.

Grade 12, chapter 11 (fiscal policy and public debt).
Jorda-Schularick-Taylor Macrohistory Database: debtgdp (public debt / GDP), gdp (nominal), ltrate (long-term government bond
yield, per cent), cpi; GBR and USA 1870-2020.
Eurostat gov_10dd_edpt1, general government (S13), per cent of GDP: GD (gross debt) 2000-2025 for six countries; B9 (net
lending) to count the years with a deficit above 3 % of GDP among twelve countries that have used the euro since 2002 or
earlier (AT BE DE EL ES FI FR IE IT LU NL PT), 2002-2025.
Decomposition of the change in the UK debt ratio, year by year, 1947-1975, with d the ratio, i the long rate (an
approximation of the rate paid on the debt), gamma nominal GDP growth, pi CPI inflation and g real growth from
(1+gamma) = (1+g)(1+pi):
  d_t - d_{t-1} = d_{t-1} i/(1+gamma) - d_{t-1} gamma/(1+gamma) + residual,
the growth term split between real growth and inflation in proportion to log(1+g) and log(1+pi); the residual is the
primary balance with the opposite sign plus other adjustments (sales of assets, valuation, data revisions).
Writes:
  out/debt_long.csv     year, gbr, usa (per cent of GDP)
  out/debt_euro.csv     year, EL, IT, FR, ES, DE, IE
  out/uk_decomp.csv     item, points (sum over 1947-1975, percentage points of GDP), share (of the fall)
  out/debt_key.csv      values quoted in the text
"""
import numpy as np
import pandas as pd

from econdata import eurostat, jst
from figout import write_table

EURO12 = ["AT", "BE", "DE", "EL", "ES", "FI", "FR", "IE", "IT", "LU", "NL", "PT"]
SIX = ["EL", "IT", "FR", "ES", "DE", "IE"]


def long_run():
    j = jst(isos=["GBR", "USA"])
    p = j.pivot(index="year", columns="iso3", values="debtgdp").loc[1870:2020]
    return pd.DataFrame({"year": p.index, "gbr": (100 * p.GBR).round(1).values, "usa": (100 * p.USA).round(1).values})


def euro():
    e = eurostat("gov_10dd_edpt1")
    e = e[(e.unit == "PC_GDP") & (e.sector == "S13")]
    gd = e[e.na_item == "GD"].pivot(index="time", columns="geo", values="value").loc[2000:2025, SIX]
    b9 = e[e.na_item == "B9"].pivot(index="time", columns="geo", values="value").loc[2002:2025, EURO12]
    over = int((b9 < -3).sum().sum())
    total = int(b9.notna().sum().sum())
    t = gd.round(1).reset_index().rename(columns={"time": "year"})
    k = {"euro12_over3": over, "euro12_obs": total, "euro12_share": round(100 * over / total, 1)}
    for c in SIX:
        k[f"gd2007_{c}"] = round(gd.loc[2007, c], 1)
        k[f"gd2025_{c}"] = round(gd.loc[2025, c], 1)
    for y in (2008, 2009, 2010, 2011, 2012, 2013):
        k[f"el_gd{y}"] = round(gd.loc[y, "EL"], 1)
    k["el_b9_2009"] = round(b9.loc[2009, "EL"], 1)
    ea = e[(e.na_item == "B9") & (e.geo == "EA20")].set_index("time").value
    k["ea_b9_2007"], k["ea_b9_2009"] = round(ea[2007], 1), round(ea[2009], 1)
    return t, k


def decompose():
    x = jst(isos=["GBR"]).set_index("year").loc[1946:1975]
    d, gam = x.debtgdp, x.gdp / x.gdp.shift(1) - 1
    i, pi = x.ltrate / 100, x.cpi / x.cpi.shift(1) - 1
    g = (1 + gam) / (1 + pi) - 1
    rows = []
    for t in range(1947, 1976):
        d0 = d[t - 1]
        intr = d0 * i[t] / (1 + gam[t])
        grow = -d0 * gam[t] / (1 + gam[t])
        sr = np.log(1 + g[t]) / np.log(1 + gam[t])
        rows.append({"interest": intr, "real growth": grow * sr, "inflation": grow * (1 - sr),
                     "other": (d[t] - d0) - intr - grow})
    r = 100 * pd.DataFrame(rows).sum()
    fall = 100 * (d[1946] - d[1975])
    out = pd.DataFrame({"item": r.index, "points": r.round(1).values, "share": (-100 * r / fall).round(1).values})
    k = {"uk1946": round(100 * d[1946], 1), "uk1975": round(100 * d[1975], 1), "fall": round(fall, 1),
         "gamma_mean": round(100 * gam.loc[1947:1975].mean(), 2), "i_mean": round(100 * i.loc[1947:1975].mean(), 2),
         "pi_mean": round(100 * pi.loc[1947:1975].mean(), 2), "g_mean": round(100 * g.loc[1947:1975].mean(), 2),
         "uk_nominal_ratio": round(float(d[1975] * x.gdp[1975] / (d[1946] * x.gdp[1946])), 2),
         "growth_net": round(-(r["interest"] + r["real growth"] + r["inflation"]), 1),
         "growth_net_share": round(-100 * (r["interest"] + r["real growth"] + r["inflation"]) / fall, 1)}
    return out, k


if __name__ == "__main__":
    lr = long_run()
    write_table(lr, __file__, "debt_long")
    t, k1 = euro()
    write_table(t, __file__, "debt_euro")
    dec, k2 = decompose()
    write_table(dec, __file__, "uk_decomp")
    L = lr.set_index("year")
    k3 = {f"{c}{y}": L.loc[y, c] for c in ("gbr", "usa") for y in (1870, 1914, 1918, 1946, 1975, 2007, 2020)}
    k3["gbr_max"], k3["gbr_max_year"] = L.gbr.max(), int(L.gbr.idxmax())
    write_table(pd.DataFrame([{**k1, **k2, **k3}]), __file__, "debt_key")

"""Unemployment: youth and total rates across Europe (2024), the long record of three countries, Brenland's flows.

Grade 11, chapter 12 (unemployment).
Eurostat une_rt_a, PC_ACT, both sexes, ages 15-24 and 15-74, 2024, fifteen countries and the EU.
Jorda-Schularick-Taylor Macrohistory Database `unemp` for USA, GBR, DEU, 1870-2020; the JST value for the United States
in 2019 (2.0) is an error in that release and is replaced by WDI SL.UEM.TOTL.NE.ZS (3.7).
Brenland (invented): monthly separation rate s and job-finding rate f for two groups; u(t+1) = s + (1 - s - f) u(t).
Group A (upper secondary schooling, 75 % of the labour force): s = 0.01, f = 0.24; group B (25 %): s = 0.02, f = 0.18.
A recession lowers f to 0.15 (A) and 0.10 (B) for 12 months, then f returns to normal; 36 months are traced.
Writes:
  out/eu_unemp.csv    x, geo, youth, total
  out/jst_<ISO>.csv   year, unemp ("nan" for years with no figure, so the chart shows gaps)
  out/bren_path.csv   month, A, B, all  (per cent)
  out/bren_key.csv    uA, uB, uall, uA_rec, uB_rec, A12, B12, all12, halfA, halfB
  out/growth_2024.csv iso3, growth (WDI NY.GDP.MKTP.KD.ZG, real GDP growth in 2024, per cent) for DEU, ESP, SWE
"""
import math

import numpy as np
import pandas as pd

from econdata import eurostat, jst, wdi
from figout import write_table

GEOS = ["DE", "CZ", "PL", "NL", "IE", "AT", "DK", "BE", "IT", "PT", "FI", "FR", "EL", "SE", "ES", "EU27_2020"]
A = dict(s=0.01, f=0.24, f_rec=0.15, w=0.75)
B = dict(s=0.02, f=0.18, f_rec=0.10, w=0.25)


def eu(year=2024):
    u = eurostat("une_rt_a")
    u = u[(u.unit == "PC_ACT") & (u.sex == "T") & (u.time == year)]
    p = u.pivot_table(index="geo", columns="age", values="value")
    d = pd.DataFrame({"geo": GEOS, "youth": [p.loc[g, "Y15-24"] for g in GEOS], "total": [p.loc[g, "Y15-74"] for g in GEOS]})
    d.insert(0, "x", range(len(d)))
    return d


def long_record():
    j = jst(isos=["USA", "GBR", "DEU"])
    w = wdi("SL.UEM.TOTL.NE.ZS", isos=["USA"]).set_index("year").value
    out = {}
    for iso in ["USA", "GBR", "DEU"]:
        x = j[(j.iso3 == iso) & (j.year <= 2020)][["year", "unemp"]].copy()
        x = x[x.year >= x.dropna().year.min()]
        if iso == "USA":
            x.loc[x.year == 2019, "unemp"] = round(float(w.loc[2019]), 1)
        x["unemp"] = x.unemp.round(1).astype(object).where(x.unemp.notna(), "nan")
        out[iso] = x.reset_index(drop=True)
    return out


def path(g, months=36, rec=12):
    u = g["s"] / (g["s"] + g["f"])
    us = [u]
    for t in range(months):
        f = g["f_rec"] if t < rec else g["f"]
        u = g["s"] + (1 - g["s"] - f) * u
        us.append(u)
    return np.array(us)


def brenland():
    pa, pb = path(A), path(B)
    allp = A["w"] * pa + B["w"] * pb
    d = pd.DataFrame({"month": range(len(pa)), "A": np.round(100 * pa, 2), "B": np.round(100 * pb, 2), "all": np.round(100 * allp, 2)})
    half = lambda g: math.log(0.5) / math.log(1 - g["s"] - g["f"])
    key = {"uA": round(100 * A["s"] / (A["s"] + A["f"]), 2), "uB": round(100 * B["s"] / (B["s"] + B["f"]), 2),
           "uall": round(100 * allp[0], 2),
           "uA_rec": round(100 * A["s"] / (A["s"] + A["f_rec"]), 2), "uB_rec": round(100 * B["s"] / (B["s"] + B["f_rec"]), 2),
           "A12": round(100 * pa[12], 2), "B12": round(100 * pb[12], 2), "all12": round(100 * allp[12], 2),
           "halfA": round(half(A), 1), "halfB": round(half(B), 1)}
    return d, pd.DataFrame([key])


def growth_2024():
    g = wdi("NY.GDP.MKTP.KD.ZG", isos=["DEU", "ESP", "SWE"], since=2024, until=2024)
    return pd.DataFrame({"iso3": g.iso3, "growth": g.value.round(2)}).sort_values("iso3").reset_index(drop=True)


if __name__ == "__main__":
    write_table(growth_2024(), __file__, "growth_2024")
    write_table(eu(), __file__, "eu_unemp")
    for iso, x in long_record().items():
        write_table(x, __file__, f"jst_{iso}")
    d, k = brenland()
    write_table(d, __file__, "bren_path")
    write_table(k, __file__, "bren_key")

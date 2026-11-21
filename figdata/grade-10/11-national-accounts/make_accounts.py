"""Spending shares of GDP in six countries (2023) and Brenland's nominal and real GDP (2000-2025).

Grade 10, chapter 11 (national-accounts).
World Bank WDI, 2023, percent of GDP: NE.CON.PRVT.ZS (households' consumption), NE.GDI.TOTL.ZS (gross capital
formation), NE.CON.GOVT.ZS (general government final consumption), NE.EXP.GNFS.ZS and NE.IMP.GNFS.ZS (exports and
imports of goods and services). Brenland: code/shared/country accounts.csv (invented).
Writes:
  out/shares.csv     pos, iso3, C, I, G, X, M, NX (= X - M), total (= C + I + G + NX), all in percent of GDP
  out/brenland.csv   year, gdp, real_gdp (millions of dalens), deflator
  out/bren_2025.csv  one row: C, I, G, X, M, gdp, real_gdp, deflator, pop for 2024 and 2025 (suffixes _24, _25),
                     nominal growth, real growth, deflator inflation, real growth per person (percent, 2 d.p.)
  out/gni.csv        iso3, gni_pct (GNI as a percentage of GDP, both in current local currency, 2023:
                     NY.GNP.MKTP.CN / NY.GDP.MKTP.CN)
"""
import pandas as pd

import country
from econdata import wdi
from figout import write_table

YEAR = 2023
ISOS = ["USA", "DEU", "CHN", "IND", "VNM", "KEN"]
CODES = {"C": "NE.CON.PRVT.ZS", "I": "NE.GDI.TOTL.ZS", "G": "NE.CON.GOVT.ZS", "X": "NE.EXP.GNFS.ZS",
         "M": "NE.IMP.GNFS.ZS"}


def shares():
    d = pd.DataFrame({"iso3": ISOS})
    for k, code in CODES.items():
        w = wdi(code, isos=ISOS)
        d[k] = d.iso3.map(w[w.year == YEAR].set_index("iso3").value).round(1)
    d["NX"] = (d.X - d.M).round(1)
    d["total"] = (d.C + d.I + d.G + d.NX).round(1)
    d.insert(0, "pos", range(1, len(d) + 1))
    return d


def brenland():
    a = country.load("accounts")
    b = a[["year", "gdp", "real_gdp", "deflator"]].copy()
    r = a.set_index("year")
    y0, y1 = r.loc[2024], r.loc[2025]
    row = {}
    for k in ["C", "I", "G", "X", "M", "gdp", "real_gdp", "deflator", "pop"]:
        row[f"{k}_24"], row[f"{k}_25"] = y0[k], y1[k]
    row["g_nom"] = round(100 * (y1.gdp / y0.gdp - 1), 2)
    row["g_real"] = round(100 * (y1.real_gdp / y0.real_gdp - 1), 2)
    row["g_defl"] = round(100 * (y1.deflator / y0.deflator - 1), 2)
    row["g_real_pp"] = round(100 * ((y1.real_gdp / y1["pop"]) / (y0.real_gdp / y0["pop"]) - 1), 2)
    return b, pd.DataFrame([row])


GNI_ISOS = ["IRL", "LUX", "USA", "DEU", "BGD", "PHL"]


def gni():
    g = wdi("NY.GNP.MKTP.CN", isos=GNI_ISOS)
    d = wdi("NY.GDP.MKTP.CN", isos=GNI_ISOS)
    g = g[g.year == YEAR].set_index("iso3").value
    d = d[d.year == YEAR].set_index("iso3").value
    return pd.DataFrame({"iso3": GNI_ISOS, "gni_pct": [round(100 * g[i] / d[i], 1) for i in GNI_ISOS]})


if __name__ == "__main__":
    write_table(gni(), __file__, "gni")
    write_table(shares(), __file__, "shares")
    b, r = brenland()
    write_table(b, __file__, "brenland")
    write_table(r, __file__, "bren_2025")

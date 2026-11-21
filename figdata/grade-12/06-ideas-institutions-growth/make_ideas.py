"""Haiti and the Dominican Republic; energy intensity; the patent and the prize of the weekend problem.

Grade 12, chapter 6 (ideas, institutions and growth).
Maddison Project Database: GDP per person, HTI and DOM, 1950-2022 (2011 dollars).
World Development Indicators EG.EGY.PRIM.PP.KD (energy intensity of primary energy, megajoules per dollar of GDP at
constant PPP), USA CHN DEU IND GBR JPN and WLD, 2000-2021; NY.GDP.MKTP.PP.KD (GDP, constant PPP), WLD, 2000 and 2021, so
that world primary energy use moves as intensity times GDP.
Weekend problem (invented): demand P = 100 - Q, marginal cost 20, patent 20 years, r = 5 %.
Writes:
  out/island.csv        year, HTI, DOM
  out/intensity.csv     year, USA, CHN, DEU, IND, GBR, JPN, WLD
  out/intensity_key.csv wld2000, wld2021, gdp_ratio, energy_ratio, usa_rate
  out/patent_key.csv    pm, qm, profit, cs_m, dwl, qc, cs_c, af20, pv_patent, pv_dwl, af25, pv_patent25
"""
import pandas as pd

from econdata import maddison, wdi
from figout import write_table

ISOS = ["USA", "CHN", "DEU", "IND", "GBR", "JPN", "WLD"]


def island():
    m = maddison(isos=["HTI", "DOM"], since=1950, until=2022)
    t = m.pivot(index="year", columns="iso3", values="gdppc")[["HTI", "DOM"]].round(0)
    t.columns.name = None
    return t.reset_index()


def intensity():
    w = wdi("EG.EGY.PRIM.PP.KD", isos=ISOS, since=2000, until=2021)
    t = w.pivot(index="year", columns="iso3", values="value")[ISOS].round(2)
    t.columns.name = None
    g = wdi("NY.GDP.MKTP.PP.KD", isos=["WLD"], since=2000, until=2021).set_index("year").value
    gdp_ratio = float(g.loc[2021] / g.loc[2000])
    e_ratio = float(t.loc[2021, "WLD"] / t.loc[2000, "WLD"]) * gdp_ratio
    usa_rate = 100 * ((t.loc[2021, "USA"] / t.loc[2000, "USA"]) ** (1 / 21) - 1)
    key = pd.DataFrame([{"wld2000": t.loc[2000, "WLD"], "wld2021": t.loc[2021, "WLD"], "gdp_ratio": round(gdp_ratio, 3),
                         "energy_ratio": round(e_ratio, 3), "usa_rate": round(usa_rate, 2)}])
    return t.reset_index(), key


def patent(r=0.05):
    a, b, c = 100, 1, 20
    qm = (a - c) / (2 * b)
    pm = a - b * qm
    profit = (pm - c) * qm
    cs_m = 0.5 * (a - pm) * qm
    qc = (a - c) / b
    dwl = 0.5 * (pm - c) * (qc - qm)
    cs_c = 0.5 * (a - c) * qc
    af = lambda n: (1 - (1 + r) ** -n) / r
    return pd.DataFrame([{"pm": pm, "qm": qm, "profit": profit, "cs_m": cs_m, "dwl": dwl, "qc": qc, "cs_c": cs_c,
                          "af20": round(af(20), 4), "pv_patent": round(profit * af(20), 1), "pv_dwl": round(dwl * af(20), 1),
                          "af25": round(af(25), 4), "pv_patent25": round(profit * af(25), 1)}])


if __name__ == "__main__":
    write_table(island(), __file__, "island")
    t, key = intensity()
    write_table(t, __file__, "intensity")
    write_table(key, __file__, "intensity_key")
    write_table(patent(), __file__, "patent_key")

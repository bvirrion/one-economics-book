"""Health spending per person against GDP per person, 2019, all countries (both at PPP, current dollars).

Grade 10, chapter 7 (elasticities): an income elasticity read across countries. World Bank WDI
SH.XPD.CHEX.PP.CD and NY.GDP.PCAP.PP.CD, countries only. The slope of log(health) on log(gdp) is
the elasticity the chart suggests (a comparison across countries, not a demand curve).
Writes:
  out/health.csv        iso3, gdppc, health (dollars per person)
  out/health_fit.csv    n, slope, intercept (log10), times (health multiple for a tenfold income)
  out/health_line.csv   gdppc, health (two points of the fitted line, for the chart)
  out/health_marked.csv iso3, gdppc, health for the labelled countries
"""
import numpy as np
import pandas as pd

from econdata import wdi
from figout import write_table

YEAR = 2019
MARKED = ["USA", "DEU", "CHN", "IND", "BDI"]


def tables():
    h = wdi("SH.XPD.CHEX.PP.CD", countries_only=True)
    g = wdi("NY.GDP.PCAP.PP.CD", countries_only=True)
    d = (g[g.year == YEAR][["iso3", "value"]].rename(columns={"value": "gdppc"})
         .merge(h[h.year == YEAR][["iso3", "value"]].rename(columns={"value": "health"}), on="iso3").dropna())
    d = d.sort_values("iso3").reset_index(drop=True)
    d["gdppc"] = d.gdppc.round(0)
    d["health"] = d.health.round(1)
    slope, icpt = np.polyfit(np.log10(d.gdppc), np.log10(d.health), 1)
    fit = pd.DataFrame({"n": [len(d)], "slope": [round(slope, 2)], "intercept": [round(icpt, 3)],
                        "times": [round(10 ** slope, 1)]})
    xs = np.array([800.0, 120000.0])
    line = pd.DataFrame({"gdppc": xs, "health": (10 ** (icpt + slope * np.log10(xs))).round(1)})
    marked = d[d.iso3.isin(MARKED)].reset_index(drop=True)
    return d, fit, line, marked


if __name__ == "__main__":
    d, fit, line, marked = tables()
    write_table(d, __file__, "health")
    write_table(fit, __file__, "health_fit")
    write_table(line, __file__, "health_line")
    write_table(marked, __file__, "health_marked")

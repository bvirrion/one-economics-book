"""US real GDP, its trend and the output gap, with NBER recessions; inflation in two supply shocks.

Grade 12, chapter 8 (aggregate demand and supply).
World Development Indicators NY.GDP.MKTP.KD (GDP, constant 2015 dollars), USA 1960-2024, in trillions; trend from a
Hodrick-Prescott filter on log GDP (lambda 100, annual data; statsmodels); gap = 100 x (log GDP - log trend), in per cent of
trend. A straight log-linear trend over the whole period is also fitted, for the exercise on why a trend is not potential
output. Recessions: the NBER table of peaks and troughs, typed in src/recessions.csv and checked against the ledger
(cited.py); shaded from peak to trough in decimal years.
WDI FP.CPI.TOTL.ZG and NY.GDP.MKTP.KD.ZG, USA: inflation and growth in the years of the records.
Writes:
  out/gdp.csv         year, gdp, trend, linear
  out/gap.csv         year, gap
  out/recessions.csv  start, end (decimal years)
  out/adas_key.csv    hp growth per decade, linear growth, gaps and inflation of the records
"""
import numpy as np
import pandas as pd
from statsmodels.tsa.filters.hp_filter import hpfilter

from cited import load_cited
from econdata import wdi
from figout import write_table


def series():
    d = wdi("NY.GDP.MKTP.KD", isos=["USA"], since=1960, until=2024).dropna().set_index("year").value
    lg = np.log(d.values)
    cyc, tr = hpfilter(lg, lamb=100)
    b = np.polyfit(d.index, lg, 1)
    gdp = pd.DataFrame({"year": d.index, "gdp": (d.values / 1e12).round(3), "trend": (np.exp(tr) / 1e12).round(3),
                        "linear": (np.exp(np.polyval(b, d.index)) / 1e12).round(3)})
    gap = pd.DataFrame({"year": d.index, "gap": (100 * cyc).round(1)})
    return gdp, gap, b, tr


def recessions():
    r = load_cited(__file__, "recessions").drop(columns="ledger")
    return pd.DataFrame({"start": (r.peak_year + (r.peak_month - 1) / 12).round(3),
                         "end": (r.trough_year + r.trough_month / 12).round(3)})


def key(gap, b, tr, years, gdp_values):
    g = gap.set_index("year").gap
    cpi = wdi("FP.CPI.TOTL.ZG", isos=["USA"], since=1970, until=2024).dropna().set_index("year").value
    gr = wdi("NY.GDP.MKTP.KD.ZG", isos=["USA"], since=1970, until=2024).dropna().set_index("year").value
    t = pd.Series(tr, index=years)
    k = {"linear_growth": round(100 * (np.exp(b[0]) - 1), 2),
         "hp_growth_1960s": round(100 * (np.exp((t[1970] - t[1960]) / 10) - 1), 1),
         "hp_growth_2010s": round(100 * (np.exp((t[2019] - t[2010]) / 9) - 1), 1)}
    for y in (1973, 1975, 1982, 2007, 2009, 2020, 2022):
        k[f"gap{y}"] = g[y]
    lin = 100 * (np.exp(np.log(gdp_values) - np.polyval(b, years)) - 1)
    for y in (1960, 2000, 2024):
        k[f"lingap{y}"] = round(float(lin[list(years).index(y)]), 1)
    for y in (1973, 1974, 1975, 2009, 2020, 2021, 2022):
        k[f"cpi{y}"] = round(cpi[y], 1)
    for y in (1974, 1975, 2009, 2020, 2021):
        k[f"growth{y}"] = round(gr[y], 1)
    return pd.DataFrame([k])


if __name__ == "__main__":
    gdp, gap, b, tr = series()
    write_table(gdp, __file__, "gdp")
    write_table(gap, __file__, "gap")
    write_table(recessions(), __file__, "recessions")
    write_table(key(gap, b, tr, gdp.year.values, gdp.gdp.values * 1e12), __file__, "adas_key")

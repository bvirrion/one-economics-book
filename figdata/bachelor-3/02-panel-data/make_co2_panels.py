"""Carbon dioxide per person against income per person, across and within countries.

WDI EN.GHG.CO2.PC.CE.AR5 (tonnes of CO2 per person) and NY.GDP.PCAP.KD (GDP per person,
constant 2015 US dollars), 1990-2022, countries only (200 countries, 6,419 country-years).
Writes
  out/between.csv       iso3, gdp (geometric mean over the years), co2 (mean): 200 dots
  out/between_line.csv  gdp, co2: the least-squares line of co2 on log gdp, at the ends
  out/within_bins.csv   dly, dco2: deviations from each country's own means, in 20 bins
                        of equal count of dly (means within each bin)
  out/within_line.csv   dly, dco2: the within least-squares line at the ends of the bins
  out/co2_stats.csv     between, within, countries, rows
Book 5, chapter 2, opening chart (two panels).
"""
import numpy as np
import pandas as pd
from econdata import wdi
from figout import write_table


def panel():
    co2 = wdi("EN.GHG.CO2.PC.CE.AR5", since=1990, until=2022, countries_only=True)
    gdp = wdi("NY.GDP.PCAP.KD", since=1990, until=2022, countries_only=True)
    d = co2.merge(gdp, on=["iso3", "year"], suffixes=("_co2", "_gdp"))
    d = d.rename(columns={"value_co2": "co2"}).dropna(subset=["co2", "value_gdp"])
    d["ly"] = np.log(d.value_gdp)
    return d


def slope(x, y):
    x, y = x - x.mean(), y - y.mean()
    return float((x @ y) / (x @ x))


def tables():
    d = panel()
    m = d.groupby("iso3")[["co2", "ly"]].mean()
    b = slope(m.ly, m.co2)
    a = m.co2.mean() - b * m.ly.mean()
    between = pd.DataFrame({"iso3": m.index, "gdp": np.exp(m.ly).values, "co2": m.co2.values})
    ends = np.array([m.ly.min(), m.ly.max()])
    bline = pd.DataFrame({"gdp": np.exp(ends), "co2": a + b * ends})
    w = d[["co2", "ly"]] - d.groupby("iso3")[["co2", "ly"]].transform("mean")
    wb = slope(w.ly, w.co2)
    w["bin"] = pd.qcut(w.ly.rank(method="first"), 20, labels=False)
    bins = w.groupby("bin")[["ly", "co2"]].mean().rename(columns={"ly": "dly", "co2": "dco2"})
    wends = np.array([bins.dly.min(), bins.dly.max()])
    wline = pd.DataFrame({"dly": wends, "dco2": wb * wends})
    stats = pd.DataFrame({"between": [b], "within": [wb], "countries": [len(m)], "rows": [len(d)]})
    return between, bline, bins.reset_index(drop=True), wline, stats


if __name__ == "__main__":
    for t, name in zip(tables(), ["between", "between_line", "within_bins", "within_line",
                                  "co2_stats"]):
        write_table(t, __file__, name)

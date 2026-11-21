"""Chart 4: employment in agriculture (percent of employment, modelled ILO estimate)
against GDP per person (PPP, constant 2021 dollars), 2019 (WDI SL.AGR.EMPL.ZS,
NY.GDP.PCAP.PP.KD). Writes out/agri.csv and out/agri_stats.csv."""
import numpy as np
import pandas as pd
from econdata import wdi
from figout import write_table

Y = 2019


def table():
    a = wdi("SL.AGR.EMPL.ZS", since=Y, until=Y, countries_only=True)
    g = wdi("NY.GDP.PCAP.PP.KD", since=Y, until=Y, countries_only=True)
    d = a[["iso3", "value"]].rename(columns={"value": "agri"}).merge(
        g[["iso3", "value"]].rename(columns={"value": "gdp"}), on="iso3").dropna()
    d["lx"] = np.log10(d.gdp)
    return d.reset_index(drop=True)


def stats(d):
    lo = d[d.gdp < d.gdp.quantile(0.2)].agri.median()
    hi = d[d.gdp > d.gdp.quantile(0.8)].agri.median()
    return pd.DataFrame({"stat": ["n", "poorest_fifth_median", "richest_fifth_median"],
                         "value": [len(d), lo, hi]})


if __name__ == "__main__":
    d = table()
    write_table(d, __file__, "agri")
    write_table(stats(d), __file__, "agri_stats")

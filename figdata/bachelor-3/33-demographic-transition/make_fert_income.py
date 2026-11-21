"""Chart 3: total fertility rate against GDP per person (PPP, constant 2021 dollars),
2023 (WDI SP.DYN.TFRT.IN and NY.GDP.PCAP.PP.KD). Writes out/fert_income.csv and
out/fert_income_stats.csv (slope of TFR on log10 income, count, medians)."""
import numpy as np
import pandas as pd
from econdata import wdi
from figout import write_table

Y = 2023


def table():
    f = wdi("SP.DYN.TFRT.IN", since=Y, until=Y, countries_only=True)
    g = wdi("NY.GDP.PCAP.PP.KD", since=Y, until=Y, countries_only=True)
    d = f[["iso3", "value"]].rename(columns={"value": "tfr"}).merge(
        g[["iso3", "value"]].rename(columns={"value": "gdp"}), on="iso3").dropna()
    d["lx"] = np.log10(d.gdp)
    return d.reset_index(drop=True)


def stats(d):
    b = np.polyfit(d.lx, d.tfr, 1)[0]
    lo = d[d.gdp < d.gdp.quantile(0.2)].tfr.median()
    hi = d[d.gdp > d.gdp.quantile(0.8)].tfr.median()
    below = 100 * (d.tfr < 2.1).mean()
    return pd.DataFrame({"stat": ["n", "slope", "poorest_fifth", "richest_fifth",
                                  "below_replacement"],
                         "value": [len(d), b, lo, hi, below]})


if __name__ == "__main__":
    d = table()
    write_table(d, __file__, "fert_income")
    write_table(stats(d), __file__, "fert_income_stats")

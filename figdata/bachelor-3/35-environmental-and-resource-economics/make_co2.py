"""Chart 2: carbon dioxide emissions per person (CEDS, tonnes) against GDP per person
(Maddison Project 2023, 2011 dollars), 2019, all countries with both. Writes
out/co2.csv, out/co2_fit.csv and out/co2_stats.csv (slope of log10 emissions on log10
income, so an elasticity, and the medians of the poorest and richest fifths)."""
import numpy as np
import pandas as pd
from econdata import ceds, maddison
from figout import write_table

Y = 2019


def table():
    c = ceds("co2", since=Y, until=Y)[["iso3", "value"]]
    m = maddison(since=Y, until=Y)[["iso3", "gdppc", "pop"]]
    d = c.merge(m, on="iso3").dropna()
    d = d[d["pop"] > 1000].copy()
    d["t"] = d.value / d["pop"]
    d["lx"], d["ly"] = np.log10(d.gdppc), np.log10(d.t)
    return d.reset_index(drop=True)


if __name__ == "__main__":
    d = table()
    write_table(d[["iso3", "lx", "ly", "t"]], __file__, "co2")
    b, a = np.polyfit(d.lx, d.ly, 1)
    xs = np.array([d.lx.min(), d.lx.max()])
    write_table(pd.DataFrame({"lx": xs, "ly": a + b * xs}), __file__, "co2_fit")
    lo = d[d.gdppc < d.gdppc.quantile(0.2)].t.median()
    hi = d[d.gdppc > d.gdppc.quantile(0.8)].t.median()
    st = pd.DataFrame({"stat": ["n", "elasticity", "poorest_fifth", "richest_fifth"],
                       "value": [len(d), b, lo, hi]})
    write_table(st, __file__, "co2_stats")

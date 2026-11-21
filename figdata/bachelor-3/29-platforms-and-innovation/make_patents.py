"""Chart 2: patent applications by residents per million people against GDP per
person (PPP, constant 2021 dollars), 2019, all countries with both (WDI IP.PAT.RESD,
SP.POP.TOTL, NY.GDP.PCAP.PP.KD). Writes out/patents.csv (log10 of both) and
out/patents_fit.csv (least-squares line in logs, with slope and R^2 in
out/patents_stats.csv)."""
import numpy as np
import pandas as pd
from econdata import wdi
from figout import write_table

YEAR = 2019


def table():
    pat = wdi("IP.PAT.RESD", since=YEAR, until=YEAR, countries_only=True)
    pop = wdi("SP.POP.TOTL", since=YEAR, until=YEAR, countries_only=True)
    gdp = wdi("NY.GDP.PCAP.PP.KD", since=YEAR, until=YEAR, countries_only=True)
    d = (pat[["iso3", "value"]].rename(columns={"value": "pat"})
         .merge(pop[["iso3", "value"]].rename(columns={"value": "pop"}), on="iso3")
         .merge(gdp[["iso3", "value"]].rename(columns={"value": "gdp"}), on="iso3"))
    d = d[(d.pat > 0)].dropna()
    d["per_m"] = d.pat / d["pop"] * 1e6
    d["lx"], d["ly"] = np.log10(d.gdp), np.log10(d.per_m)
    return d[["iso3", "gdp", "per_m", "lx", "ly"]].reset_index(drop=True)


def fit(d):
    b, a = np.polyfit(d.lx, d.ly, 1)
    r2 = np.corrcoef(d.lx, d.ly)[0, 1] ** 2
    xs = np.array([d.lx.min(), d.lx.max()])
    return (pd.DataFrame({"lx": xs, "ly": a + b * xs}),
            pd.DataFrame({"stat": ["slope", "r2", "n"], "value": [b, r2, len(d)]}))


if __name__ == "__main__":
    d = table()
    line, stats = fit(d)
    write_table(d, __file__, "patents")
    write_table(line, __file__, "patents_fit")
    write_table(stats, __file__, "patents_stats")

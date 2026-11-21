"""Chart 4 (the Lucas pattern): net inflows of foreign direct investment (percent of
GDP, WDI BX.KLT.DINV.WD.GD.ZS) against GDP per person (constant 2021 PPP dollars,
NY.GDP.PCAP.PP.KD), country averages 2000--2024, countries with a 2024 population of
at least one million and at least 15 years of both. Also the Lucas calculation with
Penn World Table output per worker in 2019 for India and the United States: with
y = A k^alpha and equal A, MPK_India / MPK_US = (y_US / y_India)^((1 - alpha)/alpha).
Writes out/lucas.csv, out/lucas_bins.csv (medians by quintile of income) and
out/lucas_stats.csv."""
import numpy as np
import pandas as pd
from econdata import pwt, wdi, wdi_countries
from figout import write_table

ALPHA = 0.4


def tables():
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    f = wdi("BX.KLT.DINV.WD.GD.ZS", since=2000, until=2024)
    f = f.rename(columns={"value": "fdi"})
    y = wdi("NY.GDP.PCAP.PP.KD", since=2000, until=2024).rename(columns={"value": "y"})
    d = f.merge(y[["iso3", "year", "y"]], on=["iso3", "year"]).dropna()
    d = d[d.iso3.isin(real)]
    pop = wdi("SP.POP.TOTL", since=2024, until=2024).set_index("iso3").value
    g = d.groupby("iso3").agg(fdi=("fdi", "median"), y=("y", "mean"),
                              years=("y", "size")).reset_index()
    g = g[(g.years >= 15) & g.iso3.map(pop).ge(1e6)].reset_index(drop=True)
    g["q"] = pd.qcut(g.y, 5, labels=False)
    bins = g.groupby("q").agg(y=("y", "median"), fdi=("fdi", "median")).reset_index()
    p = pwt(isos=["USA", "IND"], since=2019, until=2019, cols=["rgdpo", "emp"])
    ypw = (p.rgdpo / p.emp).to_numpy()
    ratio = ypw[list(p.iso3).index("USA")] / ypw[list(p.iso3).index("IND")]
    stats = pd.DataFrame({"stat": ["countries", "ypw_ratio_us_india", "mpk_ratio",
                                   "alpha", "corr_log_y_fdi"],
                          "value": [len(g), ratio, ratio ** ((1 - ALPHA) / ALPHA),
                                    ALPHA,
                                    np.corrcoef(np.log(g.y), g.fdi)[0, 1]]})
    return g[["iso3", "y", "fdi"]], bins, stats


if __name__ == "__main__":
    g, bins, stats = tables()
    write_table(g, __file__, "lucas")
    write_table(bins, __file__, "lucas_bins")
    write_table(stats, __file__, "lucas_stats")

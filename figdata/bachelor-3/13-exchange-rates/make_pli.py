"""Opening chart: price level index (GDP, United States = 100; WDI PA.NUS.GDP.PLI)
against GDP per person (constant 2021 PPP dollars, NY.GDP.PCAP.PP.KD), 2023, countries
only. Writes out/pli.csv, out/pli_fit.csv and out/pli_stats.csv (countries, slope of
log PLI on log income, its standard error, R-squared, and selected countries)."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from econdata import wdi, wdi_countries
from figout import write_table

YEAR = 2023
NAMED = ["CHE", "USA", "DEU", "CHN", "BRA", "IND", "EGY"]


def tables():
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    p = wdi("PA.NUS.GDP.PLI", since=YEAR, until=YEAR).rename(columns={"value": "pli"})
    y = wdi("NY.GDP.PCAP.PP.KD", since=YEAR, until=YEAR).rename(columns={"value": "y"})
    d = p.merge(y[["iso3", "y"]], on="iso3").dropna()
    d = d[d.iso3.isin(real)].reset_index(drop=True)[["iso3", "y", "pli"]]
    r = sm.OLS(np.log(d.pli), sm.add_constant(np.log(d.y))).fit()
    xs = np.exp(np.linspace(np.log(d.y.min()), np.log(d.y.max()), 30))
    a, b = r.params.iloc[0], r.params.iloc[1]
    fit = pd.DataFrame({"y": xs, "pli": np.exp(a) * xs**b})
    stats = [("countries", len(d)), ("slope", r.params.iloc[1]),
             ("slope_se", r.bse.iloc[1]), ("r2", r.rsquared)]
    for iso in NAMED:
        row = d[d.iso3 == iso].iloc[0]
        stats += [(f"pli_{iso}", row.pli), (f"y_{iso}", row.y)]
    return d, fit, pd.DataFrame(stats, columns=["stat", "value"])


if __name__ == "__main__":
    d, fit, stats = tables()
    write_table(d, __file__, "pli")
    write_table(fit, __file__, "pli_fit")
    write_table(stats, __file__, "pli_stats")

"""Chart 2 (Feldstein--Horioka): gross domestic saving and gross capital formation as a
percent of GDP (WDI NY.GNS.ICTR.ZS gross national saving, NE.GDI.TOTL.ZS), country
averages over 2000--2024, for countries with at least 20 years of both and a 2024
population of at least one million. Writes out/fh.csv, out/fh_fit.csv and
out/fh_stats.csv (countries, slope, its standard error, R-squared)."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from econdata import wdi, wdi_countries
from figout import write_table


def tables():
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    s = wdi("NY.GNS.ICTR.ZS", since=2000, until=2024).rename(columns={"value": "s"})
    i = wdi("NE.GDI.TOTL.ZS", since=2000, until=2024).rename(columns={"value": "i"})
    d = s.merge(i[["iso3", "year", "i"]], on=["iso3", "year"]).dropna()
    d = d[d.iso3.isin(real)]
    pop = wdi("SP.POP.TOTL", since=2024, until=2024).set_index("iso3").value
    g = d.groupby("iso3").agg(saving=("s", "mean"), investment=("i", "mean"),
                              years=("s", "size")).reset_index()
    g = g[(g.years >= 20) & g.iso3.map(pop).ge(1e6)].reset_index(drop=True)
    r = sm.OLS(g.investment, sm.add_constant(g.saving)).fit()
    xs = np.array([g.saving.min(), g.saving.max()])
    a, b = r.params.iloc[0], r.params.iloc[1]
    fit = pd.DataFrame({"saving": xs, "investment": a + b * xs})
    stats = pd.DataFrame({"stat": ["countries", "slope", "slope_se", "r2"],
                          "value": [len(g), b, r.bse.iloc[1], r.rsquared]})
    return g, fit, stats


if __name__ == "__main__":
    g, fit, stats = tables()
    write_table(g, __file__, "fh")
    write_table(fit, __file__, "fh_fit")
    write_table(stats, __file__, "fh_stats")

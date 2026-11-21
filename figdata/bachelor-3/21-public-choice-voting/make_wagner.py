"""Chart 2: central-government expense (WDI GC.XPN.TOTL.GD.ZS, percent of GDP)
against GDP per person (NY.GDP.PCAP.PP.KD, PPP, constant dollars), countries,
2019. Writes out/wagner.csv and out/wagner_stats.csv (slope of the share on log
income, heteroskedasticity-robust HC1 errors as in exercise 8; and the slope without
the two countries above 70 % of GDP)."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from econdata import wdi, wdi_countries
from figout import write_table


def tables(year=2019):
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    s = wdi("GC.XPN.TOTL.GD.ZS", since=year, until=year).rename(columns={"value": "s"})
    y = wdi("NY.GDP.PCAP.PP.KD", since=year, until=year).rename(columns={"value": "y"})
    d = s.merge(y[["iso3", "y"]], on="iso3").dropna()
    d = d[d.iso3.isin(real)].reset_index(drop=True)
    r = sm.OLS(d.s, sm.add_constant(np.log(d.y))).fit(cov_type="HC1")
    k = d[d.s <= 70]
    r2 = sm.OLS(k.s, sm.add_constant(np.log(k.y))).fit(cov_type="HC1")
    st = pd.DataFrame({"stat": ["countries", "slope", "slope_se", "r2", "above_70",
                                "slope_wo", "max_s"],
                       "value": [len(d), r.params.iloc[1], r.bse.iloc[1], r.rsquared,
                                 len(d) - len(k), r2.params.iloc[1], d.s.max()]})
    return d[["iso3", "y", "s"]], st


if __name__ == "__main__":
    d, st = tables()
    write_table(d, __file__, "wagner")
    write_table(st, __file__, "wagner_stats")

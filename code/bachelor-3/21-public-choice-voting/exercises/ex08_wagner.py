"""Exercise 8: Wagner's law across countries, 2000 and 2019.

Central-government expense (WDI GC.XPN.TOTL.GD.ZS, percent of GDP) on log GDP per
person (NY.GDP.PCAP.PP.KD), countries only.
"""
import numpy as np
import statsmodels.api as sm
from econdata import wdi, wdi_countries

c = wdi_countries()
real = set(c.loc[c.Region.notna(), "Country Code"])
for year in (2000, 2019):
    s = wdi("GC.XPN.TOTL.GD.ZS", since=year, until=year).rename(columns={"value": "s"})
    y = wdi("NY.GDP.PCAP.PP.KD", since=year, until=year).rename(columns={"value": "y"})
    d = s.merge(y[["iso3", "y"]], on="iso3").dropna()
    d = d[d.iso3.isin(real)]
    r = sm.OLS(d.s, sm.add_constant(np.log(d.y))).fit(cov_type="HC1")
    print(f"{year}: {len(d)} countries, slope {r.params.iloc[1]:.2f} "
          f"(s.e. {r.bse.iloc[1]:.2f}), R-squared {r.rsquared:.2f}")

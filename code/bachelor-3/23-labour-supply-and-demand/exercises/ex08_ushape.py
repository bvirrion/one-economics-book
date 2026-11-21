"""Exercise 8: the U shape of women's relative participation.

Female-to-male participation ratio (WDI SL.TLF.CACT.FM.ZS) on log GDP per person
(NY.GDP.PCAP.PP.KD) and its square, countries, 2000 and 2019; income at the minimum.
"""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from econdata import wdi, wdi_countries

c = wdi_countries()
real = set(c.loc[c.Region.notna(), "Country Code"])
for year in (2000, 2019):
    r = wdi("SL.TLF.CACT.FM.ZS", since=year, until=year).rename(columns={"value": "r"})
    y = wdi("NY.GDP.PCAP.PP.KD", since=year, until=year).rename(columns={"value": "y"})
    d = r.merge(y[["iso3", "y"]], on="iso3").dropna()
    d = d[d.iso3.isin(real)]
    x = np.log(d.y)
    m = sm.OLS(d.r, sm.add_constant(pd.DataFrame({"x": x, "x2": x**2}))).fit(
        cov_type="HC1")
    b1, b2 = m.params["x"], m.params["x2"]
    print(f"{year}: {len(d)} countries, square term {b2:.2f} (s.e. "
          f"{m.bse['x2']:.2f}), minimum at {np.exp(-b1 / (2 * b2)):,.0f} dollars")

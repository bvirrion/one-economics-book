"""Exercise 7: the Feldstein--Horioka regression on WDI data, decade by decade.

Investment rate on saving rate (both percent of GDP), country averages over each
period; countries with data in every year of the period and over a million people.
"""
import statsmodels.api as sm
from econdata import wdi, wdi_countries

c = wdi_countries()
real = set(c.loc[c.Region.notna(), "Country Code"])
pop = wdi("SP.POP.TOTL", since=2024, until=2024).set_index("iso3").value
big = {iso for iso in real if pop.get(iso, 0) >= 1e6}
for a, b in ((1990, 1999), (2000, 2011), (2012, 2024)):
    s = wdi("NY.GNS.ICTR.ZS", since=a, until=b).rename(columns={"value": "s"})
    i = wdi("NE.GDI.TOTL.ZS", since=a, until=b).rename(columns={"value": "i"})
    d = s.merge(i[["iso3", "year", "i"]], on=["iso3", "year"]).dropna()
    d = d[d.iso3.isin(big)]
    g = d.groupby("iso3").agg(s=("s", "mean"), i=("i", "mean"), n=("s", "size"))
    g = g[g.n == b - a + 1]
    r = sm.OLS(g.i, sm.add_constant(g.s)).fit()
    print(f"{a}-{b}: countries {len(g):3d}, slope {r.params['s']:.3f} "
          f"(s.e. {r.bse['s']:.3f}), R-squared {r.rsquared:.2f}")

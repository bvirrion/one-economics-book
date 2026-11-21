"""National saving and investment across countries; two American crises.

Grade 12, chapter 7 (saving, investment and the financial system).
World Development Indicators NY.GNS.ICTR.ZS (gross national saving, % of GDP) and NE.GDI.TOTL.ZS (gross capital
formation, % of GDP), 2010-2019 means, countries only, at least 8 years of each; correlation and fitted slope of
investment on saving.
Jorda-Schularick-Taylor Macrohistory Database, USA: real GDP per person (rgdpmad) as an index (1929 = 100, 2007 = 100) and
the unemployment rate (unemp), 1926-1940 and 2004-2016; nominal house prices (hpnom) 2006 = 100.
Writes:
  out/si.csv          iso3, s, i
  out/si_key.csv      n, corr, slope
  out/crisis1929.csv  year, gdp, unemp
  out/crisis2007.csv  year, gdp, unemp, house
  out/crisis_key.csv  gdp1933, u1929, u1933, gdp2009, u2007, u2010, house2012
"""
import numpy as np
import pandas as pd

from econdata import jst, wdi
from figout import write_table


def saving_investment():
    s = wdi("NY.GNS.ICTR.ZS", since=2010, until=2019, countries_only=True).dropna()
    i = wdi("NE.GDI.TOTL.ZS", since=2010, until=2019, countries_only=True).dropna()
    S = s.groupby("iso3").value.agg(["mean", "size"])
    I = i.groupby("iso3").value.agg(["mean", "size"])
    j = S.add_suffix("_s").join(I.add_suffix("_i"), how="inner")
    j = j[(j.size_s >= 8) & (j.size_i >= 8)]
    t = pd.DataFrame({"iso3": j.index, "s": j.mean_s.round(1).values, "i": j.mean_i.round(1).values})
    key = pd.DataFrame([{"n": len(t), "corr": round(float(np.corrcoef(t.s, t.i)[0, 1]), 3),
                         "slope": round(float(np.polyfit(t.s, t.i, 1)[0]), 3)}])
    return t, key


def crises():
    x = jst(isos=["USA"]).set_index("year")
    a = x.loc[1926:1940]
    c1 = pd.DataFrame({"year": a.index, "gdp": (100 * a.rgdpmad / x.loc[1929, "rgdpmad"]).round(1).values,
                       "unemp": a.unemp.round(1).values})
    b = x.loc[2004:2016]
    c2 = pd.DataFrame({"year": b.index, "gdp": (100 * b.rgdpmad / x.loc[2007, "rgdpmad"]).round(1).values,
                       "unemp": b.unemp.round(1).values, "house": (100 * b.hpnom / x.loc[2006, "hpnom"]).round(1).values})
    g1, g2 = c1.set_index("year"), c2.set_index("year")
    key = pd.DataFrame([{"gdp1933": g1.loc[1933, "gdp"], "u1929": g1.loc[1929, "unemp"], "u1933": g1.loc[1933, "unemp"],
                         "gdp2009": g2.loc[2009, "gdp"], "u2007": g2.loc[2007, "unemp"], "u2010": g2.loc[2010, "unemp"],
                         "house2012": g2.loc[2012, "house"]}])
    return c1, c2, key


if __name__ == "__main__":
    t, key = saving_investment()
    write_table(t, __file__, "si")
    write_table(key, __file__, "si_key")
    c1, c2, ck = crises()
    write_table(c1, __file__, "crisis1929")
    write_table(c2, __file__, "crisis2007")
    write_table(ck, __file__, "crisis_key")

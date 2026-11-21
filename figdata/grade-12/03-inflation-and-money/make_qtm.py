"""Money growth and inflation across countries, 1990-2019; the velocity of money in the United States, 1960-2020.

Grade 12, chapter 3 (inflation and the quantity of money).
World Development Indicators FM.LBL.BMNY.ZG (broad money growth, % a year), FP.CPI.TOTL.ZG (consumer price inflation,
% a year) and NY.GDP.MKTP.KD.ZG (real GDP growth), 1990-2019, countries only; each country's average is the geometric
mean of (1 + rate), kept when both money growth and inflation have at least 25 yearly values.
Jorda-Schularick-Taylor Macrohistory Database, USA: velocity = gdp / money (nominal GDP over broad money), 1960-2020.
Writes:
  out/qtm.csv        iso3, money, infl, gdp   (average % a year)
  out/qtm_key.csv    n, corr, corr_log, slope_log
  out/velocity.csv   year, v
  out/qtm_us.csv     year, gdp, money (billions of dollars), cpi (JST index), for 2007 and 2019 (exercises 6 and 12)
"""
import numpy as np
import pandas as pd

from econdata import jst, wdi
from figout import write_table

CODES = {"money": "FM.LBL.BMNY.ZG", "infl": "FP.CPI.TOTL.ZG", "gdp": "NY.GDP.MKTP.KD.ZG"}


def average(code):
    d = wdi(code, since=1990, until=2019, countries_only=True).dropna(subset=["value"])
    d = d[d.value > -100]
    return d.groupby("iso3").value.agg(n="size", gm=lambda v: 100 * (np.exp(np.mean(np.log1p(v / 100))) - 1))


def cross():
    a = {k: average(c) for k, c in CODES.items()}
    t = pd.DataFrame({"money": a["money"].gm, "n_m": a["money"].n, "infl": a["infl"].gm, "n_p": a["infl"].n,
                      "gdp": a["gdp"].gm})
    t = t[(t.n_m >= 25) & (t.n_p >= 25)].drop(columns=["n_m", "n_p"]).round(2).reset_index()
    lx, ly = np.log1p(t.money / 100), np.log1p(t.infl / 100)
    key = pd.DataFrame([{"n": len(t), "corr": round(float(np.corrcoef(t.money, t.infl)[0, 1]), 3),
                         "corr_log": round(float(np.corrcoef(lx, ly)[0, 1]), 3),
                         "slope_log": round(float(np.polyfit(lx, ly, 1)[0]), 3)}])
    return t, key


def velocity():
    j = jst(isos=["USA"])
    x = j[(j.year >= 1960) & (j.year <= 2020)]
    return pd.DataFrame({"year": x.year.values, "v": (x.gdp / x.money).round(3).values})


def us_two_years():
    j = jst(isos=["USA"])
    x = j[j.year.isin([2007, 2019])]
    return pd.DataFrame({"year": x.year.values, "gdp": x.gdp.round(1).values, "money": x.money.round(2).values,
                         "cpi": x.cpi.round(3).values})


if __name__ == "__main__":
    write_table(us_two_years(), __file__, "qtm_us")
    t, key = cross()
    write_table(t, __file__, "qtm")
    write_table(key, __file__, "qtm_key")
    write_table(velocity(), __file__, "velocity")

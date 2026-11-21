"""Banks and financial crises, chapter 29.

All from the JST Macrohistory Database, 18 countries, 1870-2020.
Opening chart: number of banking-crisis years (crisisJST = 1, the first year of a
systemic crisis) per decade, 1870s to 2010s.
Chart 2: real GDP per person (rgdpmad) in the five years after a business-cycle peak,
log points relative to the peak year, averaged separately over peaks with a banking
crisis within two years either side ("financial") and other peaks ("normal"). A peak is
a year in which rgdpmad is higher than in the year before and the year after. Peaks
whose six-year path (t to t + 5) touches a war year, 1914-1919 or 1939-1947, are
left out.
Chart 3: change in bank loans to the non-financial private sector (tloans) over GDP
(gdp), percentage points, over the five years ending the year before each crisis
(ratio at t - 1 minus ratio at t - 6), against the same window before all other years;
windows that touch a war year, from t - 6 to t, are left out.
Writes
  out/decades.csv      decade, crises
  out/paths.csv        h, financial, normal (h = 0..5)
  out/paths_n.csv      one row: n_financial, n_normal
  out/credit.csv       group (1 crisis, 0 other), mean, median, n
"""

import numpy as np
import pandas as pd
from econdata import jst
from figout import write_table

WAR = set(range(1914, 1920)) | set(range(1939, 1948))


def _data():
    return jst(cols=["crisisJST", "rgdpmad", "tloans", "gdp"]).sort_values(
        ["iso3", "year"]
    )


def decades():
    d = _data()
    c = d[d.crisisJST == 1]
    n = c.groupby(c.year // 10 * 10).size()
    idx = range(1870, 2020, 10)
    return pd.DataFrame(
        {"decade": list(idx), "crises": [int(n.get(k, 0)) for k in idx]}
    )


def _peaks():
    rows = []
    for iso, g in _data().groupby("iso3"):
        g = g.set_index("year")
        y = np.log(g.rgdpmad)
        cr = set(g.index[g.crisisJST == 1])
        for t in g.index:
            if any(t + h in WAR for h in range(6)):  # the whole path outside the wars
                continue
            if t - 1 not in y.index or t + 5 not in y.index:
                continue
            if not (y[t] > y[t - 1] and y[t] > y[t + 1]):
                continue
            fin = any(t + k in cr for k in range(-2, 3))
            path = [100 * (y[t + h] - y[t]) for h in range(6)]
            if np.isnan(path).any():
                continue
            rows.append({"iso3": iso, "year": t, "fin": int(fin), **{f"h{h}": p for h, p
                         in enumerate(path)}})  # fmt: skip
    return pd.DataFrame(rows)


def paths():
    p = _peaks()
    m = p.groupby("fin")[[f"h{h}" for h in range(6)]].mean()
    return pd.DataFrame(
        {"h": range(6), "financial": m.loc[1].round(2).values,
         "normal": m.loc[0].round(2).values}
    )  # fmt: skip


def paths_n():
    p = _peaks()
    return pd.DataFrame(
        [{"n_financial": int(p.fin.sum()), "n_normal": int((1 - p.fin).sum())}]
    )


def credit():
    d = _data()
    d["ratio"] = 100 * d.tloans / d.gdp
    r = d.groupby("iso3").ratio
    d["chg5"] = r.shift(1) - r.shift(6)  # the five years ending the year before t
    d = d.dropna(subset=["chg5"])
    d = d[~d.year.apply(lambda t: any(t - k in WAR for k in range(7)))]
    g = d.groupby(d.crisisJST.astype(int)).chg5
    return pd.DataFrame(
        {"group": g.mean().index, "mean": g.mean().round(2).values,
         "median": g.median().round(2).values, "n": g.count().values}
    )  # fmt: skip


if __name__ == "__main__":
    write_table(decades(), __file__, "decades")
    write_table(paths(), __file__, "paths")
    write_table(paths_n(), __file__, "paths_n")
    write_table(credit(), __file__, "credit")

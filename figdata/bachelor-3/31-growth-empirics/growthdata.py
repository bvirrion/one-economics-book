"""Shared helpers. Levels: PWT expenditure-side real GDP per person (rgdpe / pop),
comparable across countries in a year. Growth: national-accounts real GDP per person
(rgdpna / pop), which PWT recommends for growth over time because rgdpe also moves
with relative prices and the terms of trade."""
import numpy as np
from econdata import pwt


def income(col="rgdpe"):
    p = pwt(cols=[col, "pop"])
    p["y"] = p[col] / p["pop"]
    return p.pivot(index="year", columns="iso3", values="y")


def income_na():
    return income("rgdpna")


def growth(w, start, end):
    """Annual log growth (percent) of every country with data in both years."""
    ok = w.loc[[start, end]].dropna(axis=1)
    return 100 * np.log(ok.loc[end] / ok.loc[start]) / (end - start)

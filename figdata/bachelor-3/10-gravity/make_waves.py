"""Chart 3: trade as a share of GDP, (exports + imports) / 2 / GDP, unweighted mean over
the JST economies with data in each year, 1870--2020 (both in national currency, so
the ratio needs no exchange rate). Writes out/waves.csv (year, share in percent,
countries) and out/waves_points.csv (selected years)."""
import pandas as pd
from econdata import jst
from figout import write_table

POINTS = [1870, 1913, 1932, 1950, 1970, 2008, 2019]


def tables():
    d = jst(cols=["imports", "exports", "gdp"])
    d["share"] = 100 * (d.imports + d.exports) / 2 / d.gdp
    g = d.dropna(subset=["share"]).groupby("year").agg(share=("share", "mean"),
                                                       countries=("share", "size"))
    g = g.reset_index()
    return g, g[g.year.isin(POINTS)].reset_index(drop=True)


if __name__ == "__main__":
    g, p = tables()
    write_table(g, __file__, "waves")
    write_table(p, __file__, "waves_points")

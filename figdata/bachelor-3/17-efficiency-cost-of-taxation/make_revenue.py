"""Opening chart: central-government revenue as a share of GDP, 1870--2020, six
economies (JST revenue / gdp). Sweden's 1996 value (41.8 %, between 22.2 % in 1995 and
31.7 % in 1997) is a one-year spike in the source; it is replaced by the mean of its
neighbours, and the caption says so. Writes out/revenue.csv and out/revenue_points.csv."""
from econdata import jst
from figout import write_table

SHOWN = ["GBR", "USA", "FRA", "SWE", "ITA", "JPN"]


def table():
    j = jst(cols=["revenue", "gdp"], isos=SHOWN)
    j["share"] = 100 * j.revenue / j.gdp
    w = j.pivot(index="year", columns="iso3", values="share")[SHOWN]
    w.loc[1996, "SWE"] = (w.loc[1995, "SWE"] + w.loc[1997, "SWE"]) / 2
    return w.loc[1870:2020].reset_index()


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "revenue")
    pts = t[t.year.isin([1900, 1913, 1950, 2015])].reset_index(drop=True)
    write_table(pts, __file__, "revenue_points")

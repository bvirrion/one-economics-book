"""Opening chart: consumer price level of five economies, 1870--2020, 1870 = 1, for a
logarithmic scale (JST cpi). Writes out/prices.csv and out/prices_points.csv."""
from econdata import jst
from figout import write_table

SHOWN = ["GBR", "USA", "FRA", "ITA", "JPN"]


def table():
    j = jst(cols=["cpi"], isos=SHOWN)
    w = j.pivot(index="year", columns="iso3", values="cpi")[SHOWN]
    return (w / w.loc[1870]).reset_index()


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "prices")
    write_table(t[t.year.isin([1913, 1950, 2020])].reset_index(drop=True), __file__,
                "prices_points")

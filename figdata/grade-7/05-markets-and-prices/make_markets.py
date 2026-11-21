"""g7-05 Markets and Prices.

black_sea_wheat.csv   year, rus, kaz, ukr, world: wheat production in millions of tonnes, 2005-2015 (FAOSTAT crops)
eggs_a.csv / eggs_b.csv  t (year + (month-1)/12), price: US city average price of a dozen grade A large eggs, dollars,
                      monthly, January 2019 to September 2025 and November 2025 on (BLS average prices); October 2025
                      was not collected, so the series is split there
facts.csv             name, value
"""
import pandas as pd

from econdata import bls_ap, faostat_crops
from figout import write_table

AREAS = {"Russian Federation": "rus", "Kazakhstan": "kaz", "Ukraine": "ukr", "World": "world"}


def black_sea_wheat():
    f = faostat_crops("Wheat", "Production")
    p = f[f.Area.isin(list(AREAS)) & f.Year.between(2005, 2015)].pivot(index="Year", columns="Area", values="Value")
    p = (p[list(AREAS)] / 1e6).round(1).rename(columns=AREAS)
    p.index = p.index.astype(int)
    return p.rename_axis("year").reset_index()


def eggs():
    d = bls_ap("Eggs, grade A, large")
    d = d[d.year >= 2019].sort_values(["year", "month"])
    d = d.assign(t=(d.year + (d.month - 1) / 12).round(3), price=d.value.round(2))
    return d[["year", "month", "t", "price"]].reset_index(drop=True)


def split_eggs():
    e = eggs()
    gap = (e.year * 12 + e.month).diff() > 1
    cut = e.index[gap][0]
    return e.loc[: cut - 1, ["t", "price"]], e.loc[cut:, ["t", "price"]]


def facts():
    w = black_sea_wheat().set_index("year")
    e = eggs().set_index(["year", "month"]).price
    peak = e.idxmax()
    rows = [("rus_2009", w.rus[2009]), ("rus_2010", w.rus[2010]), ("rus_2011", w.rus[2011]),
            ("kaz_2009", w.kaz[2009]), ("kaz_2010", w.kaz[2010]), ("ukr_2009", w.ukr[2009]), ("ukr_2010", w.ukr[2010]),
            ("world_2009", w.world[2009]), ("world_2010", w.world[2010]), ("world_2011", w.world[2011]),
            ("eggs_2021_12", e[(2021, 12)]), ("eggs_2023_01", e[(2023, 1)]), ("eggs_2023_08", e[(2023, 8)]),
            ("eggs_peak_year", peak[0]), ("eggs_peak_month", peak[1]), ("eggs_peak", e.max()),
            ("eggs_last_year", e.index[-1][0]), ("eggs_last_month", e.index[-1][1]), ("eggs_last", e.iloc[-1])]
    a = faostat_crops("Wheat", "Area harvested")
    a = a[a.Area == "World"].set_index("Year").Value
    rows += [("world_area_2010", round(a[2010] / 1e6, 1)), ("world_area_2011", round(a[2011] / 1e6, 1))]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(black_sea_wheat(), __file__, "black_sea_wheat")
    a, b = split_eggs()
    write_table(a, __file__, "eggs_a")
    write_table(b, __file__, "eggs_b")
    write_table(facts(), __file__, "facts")

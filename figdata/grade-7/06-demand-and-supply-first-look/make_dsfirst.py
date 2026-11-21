"""g7-06 Demand and Supply: A First Look.

strawberry_months.csv  month, y2022, y2023, y2024: US city average price of a 12-ounce dry pint of strawberries,
                       dollars, each month (BLS average prices)
berry_tables.csv      price, demanded, supplied: the chapter's invented Brenmoor strawberry market (baskets a week),
                       demand 1200 - 200 p and supply 200 p, p = 1..5 dalens per basket
berry_shift.csv       price, demanded_after: demand after a heat wave, 1600 - 200 p
facts.csv              name, value
"""
import pandas as pd

from econdata import bls_ap
from figout import write_table

YEARS = [2022, 2023, 2024]


def strawberry_months():
    d = bls_ap("Strawberries")
    d = d[d.year.isin(YEARS)].pivot(index="month", columns="year", values="value").round(2)
    d.columns = [f"y{c}" for c in d.columns]
    return d.reset_index()


def tables():
    p = pd.Series(range(1, 6), name="price")
    return pd.DataFrame({"price": p, "demanded": 1200 - 200 * p, "supplied": 200 * p})


def shift():
    p = pd.Series(range(1, 6), name="price")
    return pd.DataFrame({"price": p, "demanded_after": 1600 - 200 * p})


def facts():
    m = strawberry_months().set_index("month")
    rows = []
    for y in YEARS:
        c = f"y{y}"
        rows += [(f"{c}_min_month", int(m[c].idxmin())), (f"{c}_min", m[c].min()),
                 (f"{c}_max_month", int(m[c].idxmax())), (f"{c}_max", m[c].max())]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(strawberry_months(), __file__, "strawberry_months")
    write_table(tables(), __file__, "berry_tables")
    write_table(shift(), __file__, "berry_shift")
    write_table(facts(), __file__, "facts")

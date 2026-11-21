"""g9-02 Elasticity: A First Look.

elasticities.csv  good, elasticity, group: published price elasticities of demand, as positive numbers (the percentage
                  fall in the quantity bought for a 1 % rise in the price). Foods: US means 1938-2007 (Andreyeva, Long
                  and Brownell 2010, Table 1); gasoline short and long run (Havranek, Irsova and Janda 2012);
                  cigarettes in rich countries (National Cancer Institute and WHO 2016). Every value is a row of
                  sources/ledger/book1.md (ids in LEDGER); the test checks them against the ledger.
revenue.csv       price, quantity, revenue: an invented demand, quantity = 1200 - 100 x price, prices 0-12
gasoline.csv      year, price: US unleaded regular gasoline, dollars a gallon, annual means 2019-2023 (BLS average
                  price data)
facts.csv         name, value
"""
import pandas as pd

from econdata import bls_ap
from figout import write_table

LEDGER = {  # good: (ledger id, elasticity as a positive number, group)
    "Food away from home": ("g9:andreyeva-2010-food-away", 0.81, "food"),
    "Soft drinks": ("g9:andreyeva-2010-soft-drinks", 0.79, "food"),
    "Juice": ("g9:andreyeva-2010-juice", 0.76, "food"),
    "Beef": ("g9:andreyeva-2010-beef", 0.75, "food"),
    "Pork": ("g9:andreyeva-2010-pork", 0.72, "food"),
    "Fruit": ("g9:andreyeva-2010-fruit", 0.70, "food"),
    "Poultry": ("g9:andreyeva-2010-poultry", 0.68, "food"),
    "Dairy": ("g9:andreyeva-2010-dairy", 0.65, "food"),
    "Cereals": ("g9:andreyeva-2010-cereals", 0.60, "food"),
    "Milk": ("g9:andreyeva-2010-milk", 0.59, "food"),
    "Vegetables": ("g9:andreyeva-2010-vegetables", 0.58, "food"),
    "Fish": ("g9:andreyeva-2010-fish", 0.50, "food"),
    "Fats and oils": ("g9:andreyeva-2010-fats-oils", 0.48, "food"),
    "Cheese": ("g9:andreyeva-2010-cheese", 0.44, "food"),
    "Sweets and sugars": ("g9:andreyeva-2010-sweets-sugars", 0.34, "food"),
    "Eggs": ("g9:andreyeva-2010-eggs", 0.27, "food"),
    "Cigarettes": ("g8:cigarette-tax-elasticity", 0.40, "other"),
    "Gasoline (long run)": ("g9:fuel-elasticity-long", 0.31, "other"),
    "Gasoline (short run)": ("g9:fuel-elasticity-short", 0.09, "other"),
}


def elasticities():
    rows = [(g, v, grp) for g, (_, v, grp) in LEDGER.items()]
    return pd.DataFrame(rows, columns=["good", "elasticity", "group"]).sort_values("elasticity").reset_index(drop=True)


def revenue():
    p = list(range(0, 13))
    return pd.DataFrame({"price": p, "quantity": [1200 - 100 * x for x in p],
                         "revenue": [x * (1200 - 100 * x) for x in p]})


def gasoline():
    g = bls_ap("Gasoline, unleaded regular", annual=True)
    g = g[(g.year >= 2019) & (g.year <= 2023)]
    return pd.DataFrame({"year": g.year.astype(int).values, "price": g.value.round(2).values})


def facts():
    g = gasoline().set_index("year").price
    return pd.DataFrame([("gas_2021", g[2021]), ("gas_2022", g[2022]),
                         ("gas_rise_pct", round(100 * (g[2022] / g[2021] - 1), 1))], columns=["name", "value"])


if __name__ == "__main__":
    write_table(elasticities(), __file__, "elasticities")
    write_table(revenue(), __file__, "revenue")
    write_table(gasoline(), __file__, "gasoline")
    write_table(facts(), __file__, "facts")

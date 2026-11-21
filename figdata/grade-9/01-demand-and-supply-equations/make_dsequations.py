"""g9-01 Demand and Supply with Equations.

phones.csv    year, price, subs: France 2000-2010; real price of mobile telephone equipment (HICP CP08202 / CP00,
              2000 = 100; Eurostat prc_hicp_aind; France is the only country with the series from 2000) and mobile
              subscriptions per 100 people (WDI IT.CEL.SETS.P2); label = the year for every second year, else an empty
              TeX group; pos = the label's anchor
example.csv   price, qd, qs, qs_new: the worked example, demand 120 - 4p, supply 20 + 6p, supply after a cost fall
              40 + 6p, prices 0-20
fish.csv      price, qd, qs, qs_new: the Brenmoor fish market (invented), demand 1000 - 50p, supply 50 + 75p, after the
              new harbour 175 + 75p, prices 0-14 dalens a kilogram
facts.csv     name, value
"""
import pandas as pd

from econdata import eurostat, wdi
from figout import write_table


def phones():
    e = eurostat("prc_hicp_aind")
    e = e[(e.unit == "INX_A_AVG") & (e.geo == "FR") & e.coicop.isin(["CP08202", "CP00"])]
    p = e.pivot(index="time", columns="coicop", values="value").loc[2000:2010]
    r = p.CP08202 / p.CP00
    w = wdi("IT.CEL.SETS.P2", isos=["FRA"], since=2000, until=2010).set_index("year").value
    return pd.DataFrame({"year": r.index, "price": (100 * r / r.loc[2000]).round(1).values,
                         "subs": w.loc[r.index].round(1).values,
                         "label": [str(y) if y % 2 == 0 else "{}" for y in r.index],
                         "pos": ["north east" if y == 2010 else "south west" for y in r.index]})


def example():
    p = list(range(0, 21))
    return pd.DataFrame({"price": p, "qd": [120 - 4 * x for x in p], "qs": [20 + 6 * x for x in p],
                         "qs_new": [40 + 6 * x for x in p]})


def fish():
    p = list(range(0, 15))
    return pd.DataFrame({"price": p, "qd": [1000 - 50 * x for x in p], "qs": [50 + 75 * x for x in p],
                         "qs_new": [175 + 75 * x for x in p]})


def equilibrium(a, b, c, d):
    """Q^d = a - b p, Q^s = c + d p."""
    p = (a - c) / (b + d)
    return p, a - b * p


def facts():
    ph = phones().set_index("year")
    rows = [("price_2010", ph.price[2010]), ("subs_2000", ph.subs[2000]), ("subs_2010", ph.subs[2010])]
    for name, args in {"ex": (120, 4, 20, 6), "ex_new": (120, 4, 40, 6), "fish": (1000, 50, 50, 75),
                       "fish_new": (1000, 50, 175, 75)}.items():
        p, q = equilibrium(*args)
        rows += [(f"{name}_p", round(p, 2)), (f"{name}_q", round(q, 1))]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(phones(), __file__, "phones")
    write_table(example(), __file__, "example")
    write_table(fish(), __file__, "fish")
    write_table(facts(), __file__, "facts")

"""g9-03 Price Controls, Taxes and Subsidies.

rent_control.csv  effect, percent, pos, measured, estimated: three published numbers for San Francisco's 1994
                  extension of rent control (Diamond, McQuade and Qian 2019, abstract); each value is a ledger row
                  (LEDGER). The first two are measured by comparing covered and similar uncovered buildings; the
                  city-wide rent rise is the authors' calculation from those estimates, not a measured effect, so it
                  goes in the `estimated` column (nan elsewhere) and is drawn hatched
example.csv       price, qd, qs, qs_tax, qs_sub: the worked example of g9-01 (demand 120 - 4p, supply 20 + 6p), with a
                  tax of 5 dalens a unit paid by sellers (supply -10 + 6p in the buyer's price) and a subsidy of 5
                  dalens a unit (supply 50 + 6p)
milk.csv          year, demand, supply, unsold, stock: an invented milk market with a floor price of 0.80 dalen a litre;
                  supply grows by 3 % a year at the floor, demand by 1 %; the government buys the unsold milk
facts.csv         name, value
"""
import pandas as pd

from figout import write_table

LEDGER = {  # label: (ledger id, value used in the chart)
    "Renters staying at their address": ("g9:dmq-2019-stay", 20.0),
    "Rental housing offered by covered landlords": ("g9:dmq-2019-supply", -15.0),
    "Rents across the city (authors' calculation)": ("g9:dmq-2019-rents", 5.1),
}


CALCULATED = {"g9:dmq-2019-rents"}


def rent_control():
    rows = []
    for pos, (k, (lid, v)) in enumerate(LEDGER.items()):
        calc = lid in CALCULATED
        rows.append((k, v, pos, "nan" if calc else v, v if calc else "nan"))
    return pd.DataFrame(rows, columns=["effect", "percent", "pos", "measured", "estimated"])


def example():
    p = list(range(0, 21))
    return pd.DataFrame({"price": p, "qd": [120 - 4 * x for x in p], "qs": [20 + 6 * x for x in p],
                         "qs_tax": [-10 + 6 * x for x in p], "qs_sub": [50 + 6 * x for x in p]})


def equilibrium(a, b, c, d):
    p = (a - c) / (b + d)
    return p, a - b * p


def milk():
    rows, stock = [], 0
    for y in range(1, 9):
        dem = round(1000 * 1.01 ** (y - 1))
        sup = round(1100 * 1.03 ** (y - 1))
        stock += sup - dem
        rows.append((y, dem, sup, sup - dem, stock))
    return pd.DataFrame(rows, columns=["year", "demand", "supply", "unsold", "stock"])


def facts():
    rows = []
    for name, args in {"base": (120, 4, 20, 6), "tax5": (120, 4, -10, 6), "sub5": (120, 4, 50, 6),
                       "tax10": (120, 4, -40, 6)}.items():
        p, q = equilibrium(*args)
        rows += [(f"{name}_p", round(p, 2)), (f"{name}_q", round(q, 2))]
    m = milk().set_index("year")
    rows += [("milk_unsold_1", m.unsold[1]), ("milk_unsold_8", m.unsold[8]), ("milk_stock_8", m.stock[8])]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(rent_control(), __file__, "rent_control")
    write_table(example(), __file__, "example")
    write_table(milk(), __file__, "milk")
    write_table(facts(), __file__, "facts")

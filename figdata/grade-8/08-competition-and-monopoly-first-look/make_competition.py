"""g8-08 Competition and Monopoly: A First Look.

telecom.csv  year, de, fr, it: real price of telephone services (HICP CP0830 / all items CP00), 1996 = 100,
             Germany, France, Italy, 1996-2025 (Eurostat prc_hicp_aind, annual average indices)
juice.csv    price, cups, revenue, profit: an invented juice market, demand cups = 1000 - 200 x price a day, cost 1.00
             dalen per cup and no fixed cost
juice_line.csv  cups, price, cost: the same demand drawn from 0 to 1000 cups, with the cost of a cup (1.00)
juice_points.csv cups, price, label: the single seller (M: 3.00, 400) and many sellers (C: 1.00, 800)
ferry.csv    fare, passengers, profit_alone, profit_each_of_two: the ferry to Kestria (invented), passengers =
             500 - 10 x fare a day, cost 10 dalens a passenger and 1000 dalens a day for each company
facts.csv    name, value
"""
import pandas as pd

from econdata import eurostat
from figout import write_table

GEO = {"DE": "de", "FR": "fr", "IT": "it"}


def telecom():
    e = eurostat("prc_hicp_aind")
    e = e[(e.unit == "INX_A_AVG") & e.geo.isin(list(GEO)) & e.coicop.isin(["CP0830", "CP00"])]
    out = {}
    for g, k in GEO.items():
        p = e[e.geo == g].pivot(index="time", columns="coicop", values="value").loc[1996:2025]
        r = p.CP0830 / p.CP00
        out[k] = (100 * r / r.loc[1996]).round(1)
    return pd.DataFrame(out).rename_axis("year").reset_index()


def juice():
    prices = [4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0]
    rows = [(p, 1000 - 200 * p, p * (1000 - 200 * p), (p - 1) * (1000 - 200 * p)) for p in prices]
    return pd.DataFrame(rows, columns=["price", "cups", "revenue", "profit"])


def juice_line():
    cups = list(range(0, 1001, 100))
    return pd.DataFrame({"cups": cups, "price": [5 - c / 200 for c in cups], "cost": [1.0] * len(cups)})


def juice_points():
    j = juice().set_index("price")
    m = j.profit.idxmax()
    return pd.DataFrame({"cups": [j.cups[m], j.cups[1.0]], "price": [m, 1.0], "label": ["M", "C"]})


def ferry():
    rows = []
    for f in [40, 35, 30, 25, 20, 15]:
        q = 500 - 10 * f
        rows.append((f, q, (f - 10) * q - 1000, (f - 10) * q / 2 - 1000))
    return pd.DataFrame(rows, columns=["fare", "passengers", "profit_alone", "profit_each_of_two"])


def facts():
    t = telecom().set_index("year")
    rows = []
    for k in GEO.values():
        d = t[k].diff()
        rows += [(f"{k}_2025", t[k][2025]), (f"{k}_steepest_year", int(d.idxmin())), (f"{k}_steepest", round(d.min(), 1))]
    rows += [("de_1998", t.de[1998]), ("de_1999", t.de[1999]), ("de_2000", t.de[2000]), ("fr_1998", t.fr[1998])]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(telecom(), __file__, "telecom")
    write_table(juice(), __file__, "juice")
    write_table(juice_line(), __file__, "juice_line")
    write_table(juice_points(), __file__, "juice_points")
    write_table(ferry(), __file__, "ferry")
    write_table(facts(), __file__, "facts")

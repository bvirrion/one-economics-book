"""World oil: production against the US real pump price, 2005-2024; US and rest-of-world production.

Grade 10, chapter 6 (market-equilibrium): reading which curve moved from the directions of price
and quantity. Production: EIA international, petroleum and other liquids production, world and
United States (thousand barrels per day, written in millions). Price: as in chapter 4, the BLS
average retail price of regular unleaded gasoline deflated by the CPI-U to 2024 dollars per gallon
(no approved series of the crude oil price; the pump price follows it).
Writes:
  out/world_oil.csv   year, q (world, million barrels a day), price, us, row (rest of world)
  out/world_moves.csv year, dq, dprice (changes on the year before), kind: 1 if price and quantity
                      moved the same way (a demand-led move), 0 if opposite ways (a supply-led move)
  out/world_labels.csv the years labelled on the chart (a subset, to avoid crowding)
"""
import numpy as np
import pandas as pd

from econdata import bls_ap, bls_cpi, eia_energy
from figout import write_table

SINCE, BASE = 2005, 2024
LABELLED = [2005, 2008, 2009, 2012, 2014, 2015, 2016, 2020, 2021, 2022, 2024]


def prod(iso):
    e = eia_energy("Petroleum and other liquids production", units="thousand barrels per day", isos=[iso])
    return e.drop_duplicates("year").set_index("year").value


def tables():
    gas = bls_ap("Gasoline, unleaded regular", annual=True).set_index("year").value
    c = bls_cpi("CUUR0000SA0")
    c = c[c.period.str.match(r"M(0[1-9]|1[0-2])$")].groupby("year").value.agg(["mean", "size"])
    cpi = c[c["size"] == 12]["mean"]
    years = list(range(SINCE, BASE + 1))
    w, us = prod("WLD"), prod("USA")
    d = pd.DataFrame({"year": years,
                      "q": (w.loc[years] / 1000).round(2).values,
                      "price": (gas.loc[years] * cpi.loc[BASE] / cpi.loc[years]).round(2).values,
                      "us": (us.loc[years] / 1000).round(2).values})
    d["row"] = (d.q - d.us).round(2)
    m = pd.DataFrame({"year": d.year[1:].values, "dq": d.q.diff()[1:].round(2).values,
                      "dprice": d.price.diff()[1:].round(2).values})
    m["kind"] = (np.sign(m.dq) == np.sign(m.dprice)).astype(int)
    return d, m


if __name__ == "__main__":
    d, m = tables()
    write_table(d, __file__, "world_oil")
    write_table(m, __file__, "world_moves")
    write_table(d[d.year.isin(LABELLED)][["year", "q", "price"]], __file__, "world_labels")

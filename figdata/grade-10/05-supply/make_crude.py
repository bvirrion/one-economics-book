"""US crude oil production and the US real price of gasoline, 1976-2024.

Grade 10, chapter 5 (supply): the opening chart. Production: EIA international, crude oil
including lease condensate, United States, thousand barrels per day (written in millions).
Price: BLS average retail price of regular unleaded gasoline (annual mean of monthly U.S. city
averages) deflated by the CPI-U all items (annual mean of the twelve months) to 2024 dollars,
as in chapter 4: the price at the pump follows the price of crude oil, for which the series has
no approved source.
Writes out/crude_us.csv: year, mbd (million barrels per day), price (2024 dollars per gallon).
"""
import pandas as pd

from econdata import bls_ap, bls_cpi, eia_energy
from figout import write_table

BASE = 2024


def table():
    gas = bls_ap("Gasoline, unleaded regular", annual=True)[["year", "value"]].rename(columns={"value": "gas"})
    c = bls_cpi("CUUR0000SA0")
    c = c[c.period.str.match(r"M(0[1-9]|1[0-2])$")].groupby("year").value.agg(["mean", "size"])
    cpi = c[c["size"] == 12]["mean"].rename("cpi").reset_index()
    oil = (eia_energy("Crude oil including lease condensate production", units="thousand barrels per day",
                      isos=["USA"]).drop_duplicates("year")[["year", "value"]].rename(columns={"value": "kbd"}))
    d = oil.merge(gas, on="year").merge(cpi, on="year").sort_values("year")
    d = d[d.year <= BASE]
    base = d.loc[d.year == BASE, "cpi"].item()
    return pd.DataFrame({"year": d.year, "mbd": (d.kbd / 1000).round(2),
                         "price": (d.gas * base / d.cpi).round(2)}).reset_index(drop=True)


if __name__ == "__main__":
    write_table(table(), __file__, "crude_us")

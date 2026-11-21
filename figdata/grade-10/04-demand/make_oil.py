"""US real price of gasoline and US consumption of refined oil products per person, 1976-2024.

Grade 10, chapter 4 (demand): the opening chart and the chart of yearly changes.
  real price: BLS average retail price of regular unleaded gasoline (annual mean of the
  monthly U.S. city averages, dollars per gallon), deflated by the CPI-U all items (annual
  mean of the twelve monthly values) to 2024 dollars;
  consumption: EIA, refined petroleum products consumption, United States (thousand barrels
  per day), times 365 and divided by the population (WDI SP.POP.TOTL): barrels per person per year.
Writes:
  out/oil_us.csv      year, price (2024 dollars per gallon), bpp (barrels per person per year)
  out/oil_changes.csv year, dprice, dbpp: percentage changes on the year before
  out/oil_summary.csv n (years of changes), opposite (years in which the two changes have opposite signs)
"""
import numpy as np
import pandas as pd

from econdata import bls_ap, bls_cpi, eia_energy, wdi
from figout import write_table

BASE = 2024


def tables():
    gas = bls_ap("Gasoline, unleaded regular", annual=True)[["year", "value"]].rename(columns={"value": "gas"})
    c = bls_cpi("CUUR0000SA0")
    c = c[c.period.str.match(r"M(0[1-9]|1[0-2])$")].groupby("year").value.agg(["mean", "size"])
    cpi = c[c["size"] == 12]["mean"].rename("cpi").reset_index()
    oil = (eia_energy("Refined petroleum products consumption", units="thousand barrels per day", isos=["USA"])
           .drop_duplicates("year")[["year", "value"]].rename(columns={"value": "kbd"}))
    pop = wdi("SP.POP.TOTL", isos=["USA"])[["year", "value"]].rename(columns={"value": "pop"})
    d = gas.merge(cpi, on="year").merge(oil, on="year").merge(pop, on="year").sort_values("year")
    d = d[d.year <= BASE]
    base = d.loc[d.year == BASE, "cpi"].item()
    out = pd.DataFrame({"year": d.year, "price": (d.gas * base / d.cpi).round(2),
                        "bpp": (d.kbd * 1000 * 365 / d["pop"]).round(2)}).reset_index(drop=True)
    ch = pd.DataFrame({"year": out.year[1:].values,
                       "dprice": (out.price.pct_change() * 100).round(1)[1:].values,
                       "dbpp": (out.bpp.pct_change() * 100).round(1)[1:].values})
    summ = pd.DataFrame({"n": [len(ch)], "opposite": [int((np.sign(ch.dprice) * np.sign(ch.dbpp) < 0).sum())]})
    return out, ch, summ


if __name__ == "__main__":
    out, ch, summ = tables()
    write_table(out, __file__, "oil_us")
    write_table(ch, __file__, "oil_changes")
    write_table(summ, __file__, "oil_summary")

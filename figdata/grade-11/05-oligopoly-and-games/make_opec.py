"""OPEC crude oil output, 1979-1990: Saudi Arabia and the other members; US real gasoline price; cartel overcharges.

Grade 11, chapter 5 (oligopoly-and-games). EIA international, crude oil including lease condensate production,
thousand barrels per day. "Other members": the twelve other OPEC members of the period except Indonesia, for which
the file has no data before 1984 (Algeria, Ecuador, Gabon, Iran, Iraq, Kuwait, Libya, Nigeria, Qatar, United Arab
Emirates, Venezuela). Price: BLS average price of unleaded regular gasoline (US city average, annual), in 2024 dollars
with the CPI-U, as in grade 10 chapter 5 (no approved crude price series). Cited: Connor (2005), src/overcharge.csv.
Writes:
  out/opec.csv        year, sau, others (million barrels a day), gas (2024 dollars a gallon; empty before the series)
  out/opec_points.csv year, sau, others for 1981, 1985, 1986
  out/overcharge.csv  group, median
"""
import pandas as pd

from cited import load_cited
from econdata import bls_ap, bls_cpi, eia_energy
from figout import write_table

OTHERS = ["DZA", "ECU", "GAB", "IRN", "IRQ", "KWT", "LBY", "NGA", "QAT", "ARE", "VEN"]
Y0, Y1, BASE = 1979, 1990, 2024


def opec():
    d = eia_energy("Crude oil including lease condensate production", units="thousand barrels per day",
                   isos=["SAU"] + OTHERS, since=Y0, until=Y1)
    w = d.pivot_table(index="year", columns="iso3", values="value")
    assert w[OTHERS].notna().all().all()
    out = pd.DataFrame({"year": w.index, "sau": (w["SAU"] / 1000).round(2).values,
                        "others": (w[OTHERS].sum(axis=1) / 1000).round(2).values})
    gas = bls_ap("Gasoline, unleaded regular", annual=True)[["year", "value"]].rename(columns={"value": "gas"})
    c = bls_cpi("CUUR0000SA0")
    c = c[c.period.str.match(r"M(0[1-9]|1[0-2])$")].groupby("year").value.agg(["mean", "size"])
    cpi = c[c["size"] == 12]["mean"]
    gas["gas"] = (gas.gas * cpi.loc[BASE] / gas.year.map(cpi)).round(2)
    out = out.merge(gas, on="year", how="left")
    return out


if __name__ == "__main__":
    o = opec()
    write_table(o, __file__, "opec")
    write_table(o[o.year.isin([1981, 1985, 1986])][["year", "sau", "others"]], __file__, "opec_points")
    write_table(load_cited(__file__, "overcharge").drop(columns="ledger"), __file__, "overcharge")

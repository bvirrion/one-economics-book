"""Chart 2: central-government revenue by type, 1972 and 2024, five economies,
percent of revenue (WDI GC.TAX.YPKG.RV.ZS income, profits and capital gains;
GC.TAX.GSRV.RV.ZS goods and services; GC.REV.SOCL.ZS social contributions;
GC.TAX.INTT.RV.ZS international trade; other = the rest). A missing trade value is
counted in `other`. Writes out/composition.csv (one row per economy and year)."""
import pandas as pd
from econdata import wdi
from figout import write_table

CODES = {"income": "GC.TAX.YPKG.RV.ZS", "goods": "GC.TAX.GSRV.RV.ZS",
         "social": "GC.REV.SOCL.ZS", "trade": "GC.TAX.INTT.RV.ZS"}
SHOWN = ["USA", "GBR", "FRA", "DEU", "KOR"]
YEARS = [1972, 2024]


def table():
    d = None
    for k, c in CODES.items():
        x = wdi(c).rename(columns={"value": k})[["iso3", "year", k]]
        d = x if d is None else d.merge(x, on=["iso3", "year"], how="outer")
    d = d[d.iso3.isin(SHOWN) & d.year.isin(YEARS)].fillna({"trade": 0.0})
    d["other"] = 100 - d[list(CODES)].sum(axis=1)
    d["iso3"] = pd.Categorical(d.iso3, SHOWN)
    d = d.sort_values(["iso3", "year"]).reset_index(drop=True)
    d["label"] = d.iso3.astype(str) + "-" + d.year.astype(str)
    d["pos"] = range(len(d))
    return d[["pos", "label", "iso3", "year", *CODES, "other"]]


if __name__ == "__main__":
    write_table(table(), __file__, "composition")

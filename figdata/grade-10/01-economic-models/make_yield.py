"""Cereal yield against fertiliser use across countries, means of 2018-2020 (WDI, from FAO).

Grade 10, chapter 1 (economic-models): a correlation that is not yet a cause.
Countries only, with at least 100,000 hectares under cereals (so that a few fields do not
make a point) and fertiliser use between 1 and 1,000 kg per hectare. Writes:
  out/yield_fert.csv    iso3, fert (kg of nutrients per hectare of arable land), yld (kg of cereal per hectare),
                        gdppc (constant 2015 US dollars, may be empty)
  out/yield_groups.csv  group (1: fert < 10, 2: 10-100, 3: >= 100), n, median_yld
"""
import numpy as np
import pandas as pd

from econdata import wdi
from figout import write_table


def mean(code):
    d = wdi(code, since=2018, until=2020, countries_only=True)
    return d.groupby("iso3").value.mean()


def tables():
    d = pd.DataFrame({"fert": mean("AG.CON.FERT.ZS"), "yld": mean("AG.YLD.CREL.KG"),
                      "area": mean("AG.LND.CREL.HA")}).dropna()
    d = d[(d.area >= 100_000) & (d.fert >= 1) & (d.fert <= 1000)]
    g = mean("NY.GDP.PCAP.KD")
    d = d.join(g.rename("gdppc"), how="left")
    d = d.reset_index().sort_values("iso3").reset_index(drop=True)
    out = d[["iso3"]].assign(fert=d.fert.round(1), yld=d.yld.round(0), gdppc=d.gdppc.round(0))
    grp = pd.cut(d.fert, [0, 10, 100, 1e9], right=False, labels=[1, 2, 3]).astype(int)
    groups = (d.assign(group=grp).groupby("group").yld.agg(["size", "median"]).reset_index()
              .rename(columns={"size": "n", "median": "median_yld"}))
    groups["median_yld"] = groups.median_yld.round(-1)
    return out, groups


if __name__ == "__main__":
    out, groups = tables()
    write_table(out, __file__, "yield_fert")
    write_table(groups, __file__, "yield_groups")

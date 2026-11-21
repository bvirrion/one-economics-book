"""g7-03 Gains from Trade: Comparative Advantage.

exports_size.csv    iso3, pop (millions, SP.POP.TOTL), exports (NE.EXP.GNFS.ZS, % of GDP), 2024
exports_pairs.csv   the same, for the countries quoted in the text
ricardo.csv         good, brenland, kestria: hours of work per unit (the series' invented countries, country/ricardo.csv)
facts.csv           name, value: medians for large and small countries, opportunity costs
"""
import pandas as pd

from country import load
from econdata import wdi
from figout import write_table

YEAR = 2024
QUOTED = ["USA", "CHN", "IND", "JPN", "DEU", "NLD", "BEL", "IRL", "SGP", "LUX", "EST", "ETH", "PAK"]


def exports_size():
    e = wdi("NE.EXP.GNFS.ZS", countries_only=True, since=YEAR, until=YEAR)[["iso3", "value"]]
    p = wdi("SP.POP.TOTL", countries_only=True, since=YEAR, until=YEAR)[["iso3", "value"]]
    d = e.merge(p, on="iso3", suffixes=("_e", "_p")).dropna()
    d = d.assign(pop=(d.value_p / 1e6).round(2), exports=d.value_e.round(1))
    return d[["iso3", "pop", "exports"]].sort_values("iso3").reset_index(drop=True)


def ricardo():
    r = load("ricardo").pivot(index="good", columns="country", values="hours_per_unit")
    r = r.rename(columns={"Brenland": "brenland", "Kestria": "kestria"})[["brenland", "kestria"]]
    return r.loc[["grain", "cloth"]].reset_index()


def facts():
    d = exports_size()
    r = ricardo().set_index("good")
    return pd.DataFrame([
        ("countries", len(d)),
        ("large_n", int((d["pop"] > 100).sum())), ("large_median", d[d["pop"] > 100].exports.median()),
        ("small_n", int((d["pop"] < 2).sum())), ("small_median", d[d["pop"] < 2].exports.median()),
        ("brenland_cloth_in_grain", r.brenland.cloth / r.brenland.grain),
        ("kestria_cloth_in_grain", r.kestria.cloth / r.kestria.grain),
    ], columns=["name", "value"])


if __name__ == "__main__":
    d = exports_size()
    write_table(d, __file__, "exports_size")
    write_table(d[d.iso3.isin(QUOTED)], __file__, "exports_pairs")
    write_table(ricardo(), __file__, "ricardo")
    write_table(facts(), __file__, "facts")

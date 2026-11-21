"""Second chart: bound against applied tariffs (WDI TM.TAX.MRCH.BR.ZS, bound rate, simple
mean, all products; TM.TAX.MRCH.SM.AR.ZS, applied rate, simple mean, all products), each
country's latest year from 2017 to 2021 with both. The European Union's members share one
schedule, so they are one point (France's values, labelled EU). Writes out/bound.csv,
out/bound_labels.csv and out/bound_stats.csv."""
import pandas as pd
from econdata import wdi
from figout import write_table

EU27 = ["AUT", "BEL", "BGR", "HRV", "CYP", "CZE", "DNK", "EST", "FIN", "FRA", "DEU",
        "GRC", "HUN", "IRL", "ITA", "LVA", "LTU", "LUX", "MLT", "NLD", "POL", "PRT",
        "ROU", "SVK", "SVN", "ESP", "SWE"]
LABELS = {"FRA": "EU", "USA": "United States", "CHN": "China", "IND": "India",
          "BRA": "Brazil", "NGA": "Nigeria", "BGD": "Bangladesh", "JPN": "Japan"}
# EU, Japan and the United States sit within one point of each other near the origin:
# the chart names them once, in a note with a pointer (the `near` column is 1)
CLUSTER = {"FRA", "USA", "JPN"}


def table():
    b = wdi("TM.TAX.MRCH.BR.ZS", countries_only=True)
    a = wdi("TM.TAX.MRCH.SM.AR.ZS", countries_only=True)
    m = b.merge(a, on=["iso3", "country", "year"], suffixes=("_b", "_a"))
    m = m[m.year.between(2017, 2021)].sort_values("year").groupby("iso3").tail(1)
    m = m[~m.iso3.isin([e for e in EU27 if e != "FRA"])]
    m = m.rename(columns={"value_b": "bound", "value_a": "applied"})
    m["overhang"] = m.bound - m.applied
    return m.sort_values("iso3")[["iso3", "year", "bound", "applied", "overhang"]]


def stats(m):
    return pd.DataFrame({"item": ["n", "median_bound", "median_applied", "median_overhang",
                                  "share_over_10", "n_below", "max_applied"],
                         "value": [len(m), m.bound.median(), m.applied.median(),
                                   m.overhang.median(), (m.overhang > 10).mean(),
                                   int((m.overhang < 0).sum()), m.applied.max()]})


if __name__ == "__main__":
    m = table()
    write_table(m, __file__, "bound")
    lab = m[m.iso3.isin(LABELS)].assign(label=lambda d: d.iso3.map(LABELS))
    lab["near"] = lab.iso3.isin(CLUSTER).astype(int)
    lab["shown"] = lab.label.where(lab.near == 0, "{}")
    write_table(lab[["iso3", "bound", "applied", "label", "near", "shown"]], __file__,
                "bound_labels")
    write_table(stats(m), __file__, "bound_stats")

"""g8-01 Production and Productivity.

output_per_hour.csv  iso3, oph, ipp: output per hour worked (rgdpo / (emp x avh)) and income per person (rgdpe / pop),
                     2023, PWT 11.0, dollars of 2021; countries PWT flags as outliers dropped
oph_labels.csv       the same for a few named countries, with label and pos (label anchor)
capital_per_worker.csv iso3, kpw, opw: capital stock per worker (rnna / emp) and output per worker (rgdpo / emp), 2023
kpw_labels.csv       the same for a few named countries
brenland_sectors.csv sector, firms, workers, output, capital, opw, kpw: Brenland firm census (thousands of dalens)
facts.csv            name, value
"""
import pandas as pd

from country import load
from econdata import pwt
from figout import write_table

LABELS = {"NER": ("Niger", "south"), "IND": ("India", "north west"), "CHN": ("China", "south east"),
          "BRA": ("Brazil", "south east"), "MEX": ("Mexico", "south east"), "KOR": ("Korea", "south east"),
          "DEU": ("Germany", "north west"), "USA": ("United States", "south east"), "NOR": ("Norway", "north west"),
          "IRL": ("Ireland", "east"), "QAT": ("Qatar", "south east")}


def _pwt():
    d = pwt(since=2023, until=2023)
    d = d[d.i_outlier != "Outlier"].dropna(subset=["rgdpo", "emp"]).copy()
    d["oph"] = d.rgdpo / (d.emp * d.avh)
    d["ipp"] = d.rgdpe / d["pop"]
    d["opw"] = d.rgdpo / d.emp
    d["kpw"] = d.rnna / d.emp
    d["hours"] = d.avh
    d["part"] = 100 * d.emp / d["pop"]
    return d


def output_per_hour():
    d = _pwt().dropna(subset=["oph", "ipp"])
    return pd.DataFrame({"iso3": d.iso3, "oph": d.oph.round(2), "ipp": d.ipp.round(0)})


OPH_LABELS = ["NER", "IND", "CHN", "KOR", "DEU", "USA", "NOR", "IRL", "QAT"]
KPW_LABELS = ["NER", "IND", "CHN", "KOR", "USA"]


def _labels(t, x, y, keep, pos=None):
    """pos: label anchors (the side of the label that touches the dot) overriding LABELS."""
    pos = pos or {}
    t = t[t.iso3.isin(keep)].copy()
    t["label"] = t.iso3.map(lambda c: LABELS[c][0])
    t["pos"] = t.iso3.map(lambda c: pos.get(c, LABELS[c][1]))
    return t[["iso3", x, y, "label", "pos"]]


def capital_per_worker():
    d = _pwt().dropna(subset=["kpw", "opw"])
    return pd.DataFrame({"iso3": d.iso3, "kpw": (d.kpw / 1000).round(2), "opw": (d.opw / 1000).round(2)})


def brenland_sectors():
    f = load("firms")
    g = f.groupby("sector")[["workers", "output", "capital"]].sum()
    g["firms"] = f.groupby("sector").size()
    g["opw"] = (g.output / g.workers).round(1)
    g["kpw"] = (g.capital / g.workers).round(1)
    return g.reset_index()[["sector", "firms", "workers", "output", "capital", "opw", "kpw"]]


def facts():
    d = _pwt().set_index("iso3")
    rows = []
    for c in ["NER", "IND", "CHN", "MEX", "KOR", "DEU", "USA", "NOR", "IRL", "QAT"]:
        rows += [(f"{c}_oph", round(d.oph[c], 1)), (f"{c}_ipp", round(d.ipp[c], -2)),
                 (f"{c}_opw", round(d.opw[c] / 1000, 1)), (f"{c}_kpw", round(d.kpw[c] / 1000, 1)),
                 (f"{c}_hours", round(d.hours[c], 0)), (f"{c}_part", round(d.part[c], 1))]
    o = output_per_hour()
    rows += [("n_oph", len(o)), ("n_kpw", len(capital_per_worker())),
             ("corr_log", round(pd.Series(o.oph).apply(float).pipe(lambda s: s.rank()).corr(o.ipp.rank()), 2))]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    o = output_per_hour()
    write_table(o, __file__, "output_per_hour")
    write_table(_labels(o, "oph", "ipp", OPH_LABELS), __file__, "oph_labels")
    k = capital_per_worker()
    write_table(k, __file__, "capital_per_worker")
    write_table(_labels(k, "kpw", "opw", KPW_LABELS, {"KOR": "north west"}), __file__, "kpw_labels")
    write_table(brenland_sectors(), __file__, "brenland_sectors")
    write_table(facts(), __file__, "facts")

"""Chart 3: Gini coefficients of equivalised household income in European countries,
2024 (each country's latest year from 2022 to 2024 when 2024 is missing): before
social transfers with pensions counted as transfers (Eurostat ilc_di12b), before
social transfers other than pensions (ilc_di12c), and of disposable income (ilc_di12,
all ages). All three are after direct taxes. Writes out/gini_eu.csv (sorted by the
disposable Gini, with a position column) and out/gini_eu_stats.csv."""
import pandas as pd
from econdata import eurostat
from figout import write_table

NAMES = {"AT": "Austria", "BE": "Belgium", "BG": "Bulgaria", "CH": "Switzerland",
         "CY": "Cyprus", "CZ": "Czechia", "DE": "Germany", "DK": "Denmark",
         "EE": "Estonia", "EL": "Greece", "ES": "Spain", "FI": "Finland", "FR": "France",
         "HR": "Croatia", "HU": "Hungary", "IE": "Ireland", "IS": "Iceland", "IT": "Italy",
         "LT": "Lithuania", "LU": "Luxembourg", "LV": "Latvia", "MT": "Malta",
         "NL": "Netherlands", "NO": "Norway", "PL": "Poland", "PT": "Portugal",
         "RO": "Romania", "SE": "Sweden", "SI": "Slovenia", "SK": "Slovakia",
         "RS": "Serbia", "TR": "Turkey", "ME": "Montenegro", "MK": "North Macedonia",
         "AL": "Albania", "XK": "Kosovo", "UK": "United Kingdom"}


def latest(name):
    d = eurostat(name)
    if "age" in d.columns:
        d = d[d.age == "TOTAL"]
    d = d[(d.statinfo == "GINI_HND") & d.time.between(2022, 2024) & d.geo.isin(NAMES)]
    d = d.dropna(subset=["value"]).sort_values("time").groupby("geo").tail(1)
    return d.set_index("geo")[["time", "value"]]


def table():
    b, c, a = latest("ilc_di12b"), latest("ilc_di12c"), latest("ilc_di12")
    t = pd.DataFrame({"before_all": b.value, "before_ex_pensions": c.value,
                      "disposable": a.value, "year": a.time}).dropna()
    t = t[(t.year == b.time.reindex(t.index)) & (t.year == c.time.reindex(t.index))]
    t = t.sort_values("disposable").reset_index(names="geo")
    t["country"] = t.geo.map(NAMES)
    t["pos"] = range(1, len(t) + 1)
    return t[["geo", "country", "pos", "year", "before_all", "before_ex_pensions",
              "disposable"]]


def stats(t):
    cut = t.before_ex_pensions - t.disposable
    cut_all = t.before_all - t.disposable
    return pd.DataFrame({"item": ["countries", "median_disposable", "median_cut",
                                  "median_cut_all", "max_cut", "max_cut_geo",
                                  "min_cut", "min_cut_geo", "not_2024"],
                         "value": [len(t), t.disposable.median(), cut.median(),
                                   cut_all.median(), cut.max(), t.geo[cut.idxmax()],
                                   cut.min(), t.geo[cut.idxmin()], int((t.year != 2024).sum())]})


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "gini_eu")
    write_table(stats(t), __file__, "gini_eu_stats")

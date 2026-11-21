"""Opening chart: mean life satisfaction (0--10, people aged 16 and over; Eurostat
ilc_pw01) against GDP per person (PPP, constant 2021 dollars; WDI NY.GDP.PCAP.PP.KD)
in 2013 and 2024, European countries with both years. Writes out/sat_2013.csv,
out/sat_2024.csv, out/sat_arrows.csv (one row per country: x0 y0 dx dy) and
out/sat_stats.csv (between-country slope per unit of ln income in 2024; within-country
slope of the change in satisfaction on the change in ln income, with and without
Ireland, whose GDP nearly doubled through the accounting of multinational firms; the EU
education gap)."""

import numpy as np
import pandas as pd
from econdata import eurostat, wdi, wdi_countries
from figout import write_table

YEARS = (2013, 2024)
FIX = {"EL": "GR", "UK": "GB"}


def table():
    d = eurostat("ilc_pw01")
    t = d[
        (d.isced11 == "TOTAL")
        & (d.sex == "T")
        & (d.age == "Y_GE16")
        & d.time.isin(YEARS)
    ]
    w = t.pivot(index="geo", columns="time", values="value").dropna()
    w = w[[len(g) == 2 for g in w.index]]
    cc = wdi_countries()[["Country Code", "2-alpha code"]].dropna()
    iso = dict(zip(cc["2-alpha code"], cc["Country Code"]))
    w["iso3"] = [iso.get(FIX.get(g, g)) for g in w.index]
    g = wdi("NY.GDP.PCAP.PP.KD", since=2013, until=2024, countries_only=True)
    g = g[g.year.isin(YEARS)].pivot(index="iso3", columns="year", values="value")
    out = (
        w.reset_index()
        .merge(g, left_on="iso3", right_index=True, suffixes=("_s", "_y"))
        .dropna()
    )
    out = out.rename(
        columns={"2013_s": "s13", "2024_s": "s24", "2013_y": "y13", "2024_y": "y24"}
    )
    out["lx13"], out["lx24"] = np.log10(out.y13), np.log10(out.y24)
    return out[["geo", "iso3", "s13", "s24", "y13", "y24", "lx13", "lx24"]]


def stats(d):
    between = np.polyfit(np.log(d.y24), d.s24, 1)[0]
    within = np.polyfit(np.log(d.y24 / d.y13), d.s24 - d.s13, 1)[0]
    k = d[d.iso3 != "IRL"]
    within_xie = np.polyfit(np.log(k.y24 / k.y13), k.s24 - k.s13, 1)[0]
    e = eurostat("ilc_pw01")
    e = e[
        (e.geo == "EU27_2020") & (e.sex == "T") & (e.age == "Y_GE16") & (e.time == 2024)
    ]
    ed = e.set_index("isced11").value
    rise = (d.s24 > d.s13).mean()
    between13 = np.polyfit(np.log(d.y13), d.s13, 1)[0]
    conv = np.corrcoef(d.s13, d.s24 - d.s13)[0, 1]
    return pd.DataFrame(
        {
            "stat": [
                "n",
                "between",
                "within",
                "ed_low",
                "ed_high",
                "share_rose",
                "mean_dlnY",
                "mean_ds",
                "between13",
                "corr_level_change",
                "within_xie",
            ],
            "value": [
                len(d),
                between,
                within,
                ed["ED0-2"],
                ed["ED5-8"],
                100 * rise,
                np.log(d.y24 / d.y13).mean(),
                (d.s24 - d.s13).mean(),
                between13,
                conv,
                within_xie,
            ],
        }
    )


if __name__ == "__main__":
    d = table()
    write_table(d[["lx13", "s13"]], __file__, "sat_2013")
    write_table(d[["lx24", "s24"]], __file__, "sat_2024")
    a = pd.DataFrame(
        {"x": d.lx13, "y": d.s13, "dx": d.lx24 - d.lx13, "dy": d.s24 - d.s13}
    )
    write_table(a, __file__, "sat_arrows")
    write_table(stats(d), __file__, "sat_stats")
    write_table(d[["geo", "s13", "s24", "y13", "y24"]], __file__, "sat_table")

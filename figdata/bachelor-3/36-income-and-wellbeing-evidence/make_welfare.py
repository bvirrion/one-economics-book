"""Chart 2: consumption-equivalent welfare against GDP per person, both relative to the
United States, 2019 (log scales). Inputs: PWT 11.0 rgdpe, pop, csh_c, avh, emp; WDI
SP.DYN.LE00.IN; WDI SI.POV.GINI, latest year 2010--2019. The WDI Gini comes from
consumption surveys in some countries and income surveys in others; `welfare_type`
takes the survey type of the latest 2010--2019 national survey from the Poverty and
Inequality Platform, so that the table and the text can flag it. Writes out/welfare.csv,
out/welfare_parts.csv (six countries, with the survey type) and out/welfare_stats.csv."""

import numpy as np
import pandas as pd
from econdata import pip_percentiles, pwt, wdi
from figout import write_table
from welfare import YEAR_HOURS, log_lambda, sigma_from_gini, theta

PARTS = ["FRA", "DEU", "JPN", "BRA", "CHN", "IND"]


def inputs():
    p = pwt(
        since=2019, until=2019, cols=["rgdpe", "pop", "csh_c", "avh", "emp"]
    ).dropna()
    p["y"] = p.rgdpe / p["pop"]
    p["c"] = p.y * p.csh_c
    p["h"] = p.avh * p.emp / p["pop"] / YEAR_HOURS
    e = wdi("SP.DYN.LE00.IN", since=2019, until=2019, countries_only=True)
    g = wdi("SI.POV.GINI", since=2010, until=2019, countries_only=True).dropna(
        subset=["value"]
    )
    g = g.sort_values("year").groupby("iso3").tail(1)
    d = p.merge(e[["iso3", "value"]].rename(columns={"value": "e"}), on="iso3")
    d = d.merge(g[["iso3", "value"]].rename(columns={"value": "gini"}), on="iso3")
    d = d.dropna().reset_index(drop=True)
    d["sig"] = sigma_from_gini(d.gini / 100)
    return d


def welfare_type():
    d = pip_percentiles(years=range(2010, 2020))
    d = d[d.reporting_level == "national"][["iso3", "year", "welfare_type"]]
    d = d.drop_duplicates().sort_values(["iso3", "year", "welfare_type"])
    return d.groupby("iso3").tail(1).set_index("iso3").welfare_type


def compute(kappa=5.0):
    d = inputs()
    u = d.set_index("iso3").loc["USA"]
    th = theta(u.y, u.c, u.h)
    ll, parts = log_lambda(d.e, d.c, d.h, d.sig, u.e, u.c, u.h, u.sig, th, kappa)
    d["ll"] = ll
    for k, v in parts.items():
        d[k] = v
    d["ly"] = np.log(d.y / u.y)
    d["survey"] = d.iso3.map(welfare_type()).fillna("unknown")
    return d, th


if __name__ == "__main__":
    d, th = compute()
    write_table(
        pd.DataFrame({"lx": d.ly / np.log(10), "lw": d.ll / np.log(10)}),
        __file__,
        "welfare",
    )
    s = d.set_index("iso3").loc[PARTS]
    write_table(
        s[
            ["y", "e", "h", "gini", "survey", "ly", "ll", "life", "cons", "leisure",
             "ineq"]
        ].reset_index(),
        __file__,
        "welfare_parts",
    )
    below = (d.ll < d.ly).mean()
    write_table(
        pd.DataFrame(
            {
                "stat": ["n", "theta", "corr", "below_share", "n_consumption",
                         "med_gini_cons", "med_gini_inc", "usa_gini"],
                "value": [len(d), th, np.corrcoef(d.ll, d.ly)[0, 1], 100 * below,
                          int((d.survey == "consumption").sum()),
                          d.gini[d.survey == "consumption"].median(),
                          d.gini[d.survey == "income"].median(),
                          d.set_index("iso3").gini["USA"]],
            }
        ),
        __file__,
        "welfare_stats",
    )

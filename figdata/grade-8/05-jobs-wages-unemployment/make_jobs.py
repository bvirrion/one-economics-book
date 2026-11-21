"""g8-05 Jobs, Wages and Unemployment.

unemployment.csv year, usa, gbr, deu, esp, jpn: unemployment rate, percent, 1970-2020 (JST, unemp). JST R6 prints
                 2.0 for the United States in 2019 (a data error: every other year matches the national figure within a
                 tenth); that one value is replaced by WDI SL.UEM.TOTL.NE.ZS (national estimate) for 2019
real_wages.csv   year, w_usa, y_usa, w_gbr, y_gbr, w_swe, y_swe: real wage (wage / cpi) and real GDP per person
                 (rgdpmad), 1870-2020, each 1913 = 100 (JST)
brenland.csv     year, pop, under15, working_age, outside, labour_force, employed, unemployed, unemp_rate, participation:
                 Brenland 2000-2025 (thousands; invented). The accounts have no age split, so the children under 15 are
                 invented here as 16 % of the population, rounded to 10 thousand
schooling.csv    band, households, median_income: Brenland survey 2025, households whose head worked (hours > 0), by
                 the head's years of schooling; median gross household income, dalens a year (rounded to 10)
facts.csv        name, value
"""
import pandas as pd

from country import load
from econdata import jst, wdi
from figout import write_table

U5 = {"USA": "usa", "GBR": "gbr", "DEU": "deu", "ESP": "esp", "JPN": "jpn"}
W3 = {"USA": "usa", "GBR": "gbr", "SWE": "swe"}


def _jst():
    return jst(cols=["unemp", "wage", "cpi", "rgdpmad"])


def unemployment():
    u = _jst().pivot(index="year", columns="iso3", values="unemp").loc[1970:2020, list(U5)]
    w = wdi("SL.UEM.TOTL.NE.ZS", isos=["USA"], since=2019, until=2019)
    u.loc[2019, "USA"] = float(w.value.iloc[0])
    u = u.round(1)
    return u.rename(columns=U5).rename_axis("year").reset_index()


def real_wages():
    d = _jst()
    w = d.pivot(index="year", columns="iso3", values="wage")
    c = d.pivot(index="year", columns="iso3", values="cpi")
    y = d.pivot(index="year", columns="iso3", values="rgdpmad")
    rw = w / c
    out = pd.DataFrame(index=range(1870, 2021))
    for k, v in W3.items():
        out[f"w_{v}"] = (100 * rw[k] / rw.loc[1913, k]).round(1)
        out[f"y_{v}"] = (100 * y[k] / y.loc[1913, k]).round(1)
    return out.rename_axis("year").reset_index()


def brenland():
    a = load("accounts").set_index("year")
    out = a[["pop", "labour_force", "employed", "unemp_rate"]].copy()
    out["unemployed"] = out.labour_force - out.employed
    out["under15"] = (0.16 * out["pop"]).round(-1).astype(int)
    out["working_age"] = out["pop"] - out.under15
    out["outside"] = out.working_age - out.labour_force
    out["participation"] = (100 * out.labour_force / out.working_age).round(1)
    return out.reset_index()[["year", "pop", "under15", "working_age", "outside", "labour_force", "employed",
                              "unemployed", "unemp_rate", "participation"]]


def schooling():
    h = load("households")
    h = h[h.hours > 0].copy()
    h["band"] = pd.cut(h.school_years, [0, 9, 12, 15, 30], labels=["up to 9", "10 to 12", "13 to 15", "16 or more"])
    g = h.groupby("band", observed=True).agg(households=("hh", "size"), median_income=("gross_income", "median"))
    g["median_income"] = g.median_income.round(-1).astype(int)
    return g.reset_index()


def facts():
    u = unemployment().set_index("year")
    r = real_wages().set_index("year")
    b = brenland().set_index("year")
    rows = [(f"{c}_max", u[c].max()) for c in U5.values()]
    rows += [(f"{c}_max_year", int(u[c].idxmax())) for c in U5.values()]
    rows += [("esp_2007", u.esp[2007]), ("jpn_1970", u.jpn[1970]), ("usa_2020", u.usa[2020])]
    for v in W3.values():
        rows += [(f"w_{v}_1870", r[f"w_{v}"][1870]), (f"w_{v}_2020", r[f"w_{v}"][2020]),
                 (f"y_{v}_1870", r[f"y_{v}"][1870]), (f"y_{v}_2020", r[f"y_{v}"][2020])]
    rows += [("b_max_year", int(b.unemp_rate.idxmax())), ("b_max", b.unemp_rate.max()),
             ("b_min_year", int(b.unemp_rate.idxmin())), ("b_min", b.unemp_rate.min())]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(unemployment(), __file__, "unemployment")
    write_table(real_wages(), __file__, "real_wages")
    write_table(brenland(), __file__, "brenland")
    write_table(schooling(), __file__, "schooling")
    write_table(facts(), __file__, "facts")

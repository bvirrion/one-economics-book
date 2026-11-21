"""Opening chart: current-account balances as a percent of world GDP, 1990--2024: the
United States, China, Germany, Japan (from 1996, its first WDI year), all other
countries with data, and the sum over all countries with data (the world
discrepancy). WDI BN.CAB.XOKA.CD over NY.GDP.MKTP.CD for WLD; aggregates excluded.
Writes out/ca_world.csv and out/ca_world_points.csv (selected years), and
out/ca_balanced.csv: the same sum over the countries with data in every year from 2000
(a balanced panel), with their number, so that coverage cannot drive it."""
import pandas as pd
from econdata import wdi, wdi_countries
from figout import write_table

APART = ["USA", "CHN", "DEU", "JPN"]
POINTS = [2006, 2008, 2019, 2024]


def tables():
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    ca = wdi("BN.CAB.XOKA.CD", since=1990, until=2024).dropna()
    ca = ca[ca.iso3.isin(real)]
    world = wdi("NY.GDP.MKTP.CD", isos=["WLD"], since=1990, until=2024)
    world = world.set_index("year").value
    w = ca.pivot(index="year", columns="iso3", values="value")
    out = pd.DataFrame(index=w.index)
    for iso in APART:
        out[iso] = 100 * w[iso] / world
    out["rest"] = 100 * w.drop(columns=APART).sum(axis=1) / world
    out["sum"] = 100 * w.sum(axis=1) / world
    out["countries"] = w.notna().sum(axis=1)
    out = out.reset_index()
    return out, out[out.year.isin(POINTS)].reset_index(drop=True)


def balanced(start=2000):
    c = wdi_countries()
    real = set(c.loc[c.Region.notna(), "Country Code"])
    ca = wdi("BN.CAB.XOKA.CD", since=start, until=2024).dropna()
    ca = ca[ca.iso3.isin(real)]
    world = wdi("NY.GDP.MKTP.CD", isos=["WLD"], since=start, until=2024)
    w = ca.pivot(index="year", columns="iso3", values="value")
    keep = w.columns[w.notna().all()]
    s = 100 * w[keep].sum(axis=1) / world.set_index("year").value
    return pd.DataFrame({"year": s.index, "sum": s.values, "countries": len(keep)})


if __name__ == "__main__":
    t, p = tables()
    write_table(t, __file__, "ca_world")
    write_table(p, __file__, "ca_world_points")
    write_table(balanced(), __file__, "ca_balanced")

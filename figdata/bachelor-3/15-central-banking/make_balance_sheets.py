"""Opening chart: central-bank total assets as a percent of nominal GDP, year ends
2003--2025. Federal Reserve: H.4.1 total assets (RESPPMA_N.WW), last Wednesday of the
year, over U.S. GDP (WDI NY.GDP.MKTP.CD). Eurosystem: consolidated balance sheet total
assets, last week of the year (ECB), over euro-area GDP at current prices (Eurostat
nama_10_gdp, B1GQ, CP_MEUR, geo EA, the area of each year). Writes out/cb_assets.csv
and out/cb_assets_points.csv."""
import pandas as pd
from econdata import ecb_total_assets, eurostat, fed_series, wdi
from figout import write_table

POINTS = [2007, 2014, 2019, 2021, 2025]


def table():
    f = fed_series("h41", "RESPPMA_N.WW")
    f["year"] = f.date.dt.year
    fed = f.sort_values("date").groupby("year").value.last()  # millions of dollars
    us = wdi("NY.GDP.MKTP.CD", isos=["USA"]).set_index("year").value
    e = ecb_total_assets()
    e["year"] = e.week.str[:4].astype(int)
    ecb = e.groupby("year").eur_million.last()
    n = eurostat("nama_10_gdp")
    n = n[(n.na_item == "B1GQ") & (n.unit == "CP_MEUR") & (n.geo == "EA")]
    ea = n.set_index("time").value
    years = range(2003, 2026)
    return pd.DataFrame({"year": list(years),
                         "fed": [100 * fed[y] * 1e6 / us[y] for y in years],
                         "ecb": [100 * ecb[y] / ea[y] for y in years]})


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "cb_assets")
    write_table(t[t.year.isin(POINTS)].reset_index(drop=True), __file__,
                "cb_assets_points")

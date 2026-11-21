"""Chart 4: ten-year breakeven inflation in the United States, monthly, 2003--2025:
the nominal ten-year Treasury yield minus the ten-year inflation-indexed yield
(Federal Reserve H.15: RIFLGFCY10_N.M, RIFLGFCY10_XII_N.M). Writes out/breakeven.csv
and out/breakeven_stats.csv."""
import pandas as pd
from econdata import fed_series
from figout import write_table


def table():
    n = fed_series("h15", "RIFLGFCY10_N.M").rename(columns={"value": "nominal"})
    r = fed_series("h15", "RIFLGFCY10_XII_N.M").rename(columns={"value": "real"})
    d = n.merge(r, on="date")
    d["year"], d["month"] = d.date.dt.year, d.date.dt.month
    d = d[d.year.between(2003, 2025)].reset_index(drop=True)
    d["t"] = d.year + (d.month - 0.5) / 12
    d["breakeven"] = d.nominal - d.real
    return d[["t", "year", "month", "nominal", "real", "breakeven"]]


def stats(d):
    lo, hi = d.breakeven.idxmin(), d.breakeven.idxmax()
    late = d[d.year.between(2021, 2023)]
    return pd.DataFrame({"stat": ["min", "min_year", "min_month", "max", "max_year",
                                  "max_month", "max_2021_2023", "mean_2003_2019"],
                         "value": [d.breakeven[lo], d.year[lo], d.month[lo],
                                   d.breakeven[hi], d.year[hi], d.month[hi],
                                   late.breakeven.max(),
                                   d[d.year <= 2019].breakeven.mean()]})


if __name__ == "__main__":
    d = table()
    write_table(d, __file__, "breakeven")
    write_table(stats(d), __file__, "breakeven_stats")

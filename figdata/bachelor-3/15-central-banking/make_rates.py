"""Chart 2: the federal funds rate and the ten-year Treasury yield, monthly,
2005--2025 (Federal Reserve H.15: RIFSPFF_N.M, RIFLGFCY10_N.M). Writes out/rates.csv
(t = year + (month - 0.5) / 12) and out/rates_points.csv (December of selected
years)."""
from econdata import fed_series
from figout import write_table

POINTS = [2007, 2008, 2012, 2019, 2020, 2023, 2025]


def table():
    f = fed_series("h15", "RIFSPFF_N.M").rename(columns={"value": "ff"})
    t = fed_series("h15", "RIFLGFCY10_N.M").rename(columns={"value": "y10"})
    d = f.merge(t, on="date")
    d["year"], d["month"] = d.date.dt.year, d.date.dt.month
    d = d[d.year.between(2005, 2025)].reset_index(drop=True)
    d["t"] = d.year + (d.month - 0.5) / 12
    d["spread"] = d.y10 - d.ff
    return d[["t", "year", "month", "ff", "y10", "spread"]]


if __name__ == "__main__":
    d = table()
    write_table(d, __file__, "rates")
    pts = d[d.year.isin(POINTS) & (d.month == 12)].reset_index(drop=True)
    write_table(pts, __file__, "rates_points")

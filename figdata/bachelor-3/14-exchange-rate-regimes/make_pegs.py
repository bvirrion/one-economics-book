"""Opening chart: share of the JST economies with a pegged exchange rate (the
database's peg indicator, which counts a base country of a fixed system as pegged),
1870--2020. Writes out/pegs.csv and out/pegs_points.csv (selected years)."""
from econdata import jst
from figout import write_table

POINTS = [1870, 1880, 1913, 1932, 1950, 1970, 1980, 2000, 2020]


def table():
    j = jst(cols=["peg"]).dropna(subset=["peg"])
    g = j.groupby("year").peg.agg(["mean", "count"]).reset_index()
    g["share"] = 100 * g["mean"]
    return g[["year", "share", "count"]]


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "pegs")
    write_table(t[t.year.isin(POINTS)].reset_index(drop=True), __file__, "pegs_points")

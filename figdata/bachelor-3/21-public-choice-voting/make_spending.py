"""Opening chart: central-government expenditure as a share of GDP, 1870--2020, in
the economies of the Jordà-Schularick-Taylor database: median and interquartile
range across the economies with data in each year (at least 12), and the United
Kingdom and the United States. Writes out/spending.csv and out/spending_points.csv."""
from econdata import jst
from figout import write_table


def table():
    j = jst(cols=["expenditure", "gdp"])
    j["s"] = 100 * j.expenditure / j.gdp
    w = j.pivot(index="year", columns="iso3", values="s").loc[1870:2020]
    n = w.notna().sum(axis=1)
    out = w.quantile([0.25, 0.5, 0.75], axis=1).T
    out.columns = ["q25", "median", "q75"]
    out["n"] = n
    out["GBR"], out["USA"] = w.GBR, w.USA
    return out[out.n >= 12].reset_index()


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "spending")
    write_table(t[t.year.isin([1870, 1913, 1938, 1950, 1980, 2020])]
                .reset_index(drop=True), __file__, "spending_points")

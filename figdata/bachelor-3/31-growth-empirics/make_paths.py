"""Chart 3: GDP per person, 1900--2022, Argentina, Japan, South Korea, Venezuela and the
United States (Maddison Project 2023, 2011 dollars). Writes one file per country,
out/paths_<iso3>.csv (years with data only), and out/paths_points.csv."""
from econdata import maddison
from figout import write_table

SHOWN = ["USA", "ARG", "JPN", "KOR", "VEN"]


def table():
    m = maddison(isos=SHOWN, since=1900, until=2022)
    w = m.pivot(index="year", columns="iso3", values="gdppc")[SHOWN]
    return w.reset_index()


if __name__ == "__main__":
    t = table()
    for iso in SHOWN:
        one = t[["year", iso]].dropna().rename(columns={iso: "y"})
        write_table(one, __file__, f"paths_{iso}")
    pts = t[t.year.isin([1900, 1913, 1950, 1980, 2000, 2022])].reset_index(drop=True)
    write_table(pts, __file__, "paths_points")

"""Chart 2: old-age dependency ratio (population 65+ per 100 aged 15--64),
1960--2025, six economies (WDI SP.POP.DPND.OL). Writes out/dependency.csv and
out/dependency_points.csv."""
from econdata import wdi
from figout import write_table

SHOWN = ["JPN", "ITA", "DEU", "USA", "KOR", "CHN"]


def table():
    x = wdi("SP.POP.DPND.OL", since=1960, until=2025)
    x = x[x.iso3.isin(SHOWN)]
    return x.pivot(index="year", columns="iso3", values="value")[SHOWN].reset_index()


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "dependency")
    write_table(t[t.year.isin([1960, 2000, 2025])].reset_index(drop=True), __file__,
                "dependency_points")

"""Opening chart: women's labour-force participation rate (percent of women aged 15
and over; ILO modelled estimates, WDI SL.TLF.CACT.FE.ZS), 1990-2025, six economies.
Writes out/women.csv (wide) and out/women_points.csv (1990 and 2025)."""
from econdata import wdi
from figout import write_table

ISO = ["USA", "SWE", "DEU", "JPN", "KOR", "ITA"]


def table():
    d = wdi("SL.TLF.CACT.FE.ZS", since=1990, until=2025)
    w = d[d.iso3.isin(ISO)].pivot(index="year", columns="iso3", values="value")
    return w[ISO].reset_index()


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "women")
    write_table(t[t.year.isin([1990, 2025])].reset_index(drop=True), __file__,
                "women_points")

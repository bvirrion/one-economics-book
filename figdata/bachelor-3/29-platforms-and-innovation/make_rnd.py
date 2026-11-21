"""Opening chart: research and development spending as a share of GDP, 1996--2023,
six economies (WDI GB.XPD.RSDV.GD.ZS). The U.K. is left out: its series jumps by 0.64
points between 2013 and 2014, a break in measurement. Writes out/rnd.csv and
out/rnd_points.csv (first and last values)."""
from econdata import wdi
from figout import write_table

SHOWN = ["ISR", "KOR", "USA", "DEU", "CHN", "IND"]


def table():
    d = wdi("GB.XPD.RSDV.GD.ZS", isos=SHOWN, since=1996, until=2023)
    return d.pivot(index="year", columns="iso3", values="value")[SHOWN].reset_index()


def points(t):
    rows = []
    for c in SHOWN:
        s = t[["year", c]].dropna()
        rows += [(c, int(s.year.iloc[0]), s[c].iloc[0]),
                 (c, int(s.year.iloc[-1]), s[c].iloc[-1])]
    import pandas as pd
    return pd.DataFrame(rows, columns=["iso3", "year", "value"])


if __name__ == "__main__":
    t = table()
    write_table(t, __file__, "rnd")
    write_table(points(t), __file__, "rnd_points")

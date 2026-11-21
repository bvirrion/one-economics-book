"""Opening chart: applied tariff rate, weighted mean over all products, 1988--2022, for
the United States, the European Union, Japan, China, India and Brazil (WDI
TM.TAX.MRCH.WM.AR.ZS, percent). One value is left out and reported: the United States
in 2019 (13.78), a break in the source series (its primary-products series shows 80.1
the same year). Writes out/tariffs.csv (wide, year by economy, empty where missing),
out/tariffs_dropped.csv and out/tariffs_points.csv (first and last values)."""
import pandas as pd
from econdata import wdi
from figout import write_table

ISOS = ["USA", "EUU", "JPN", "CHN", "IND", "BRA"]


def tables():
    d = wdi("TM.TAX.MRCH.WM.AR.ZS", isos=ISOS).dropna(subset=["value"])
    drop = (d.iso3 == "USA") & (d.year == 2019)
    dropped = d[drop][["iso3", "year", "value"]].reset_index(drop=True)
    w = d[~drop].pivot(index="year", columns="iso3", values="value")[ISOS]
    w = w.reset_index()
    pts = []
    for iso in ISOS:
        s = d[~drop & (d.iso3 == iso)].sort_values("year")
        pts.append({"iso3": iso, "first_year": s.year.iloc[0], "first": s.value.iloc[0],
                    "last_year": s.year.iloc[-1], "last": s.value.iloc[-1]})
    return w, dropped, pd.DataFrame(pts)


if __name__ == "__main__":
    w, dropped, pts = tables()
    write_table(w, __file__, "tariffs")
    write_table(dropped, __file__, "tariffs_dropped")
    write_table(pts, __file__, "tariffs_points")

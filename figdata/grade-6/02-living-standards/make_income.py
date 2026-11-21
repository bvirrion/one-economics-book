"""g6-02 Two Hundred Years of Living Standards: three income charts (Maddison 2023).

long_run_income.csv  year, gbr, nld, world   (2011 dollars per person; blank where no estimate)
income_by_region.csv year + five regions      (Maddison's own regional estimates, blank where none)
six_paths.csv        year + six countries, 1950-2022
"""
import pandas as pd

from econdata import maddison, maddison_regions
from figout import write_table

REGION_COLS = {"Western Offshoots": "western_offshoots", "Western Europe": "western_europe",
               "Latin America": "latin_america", "East Asia": "east_asia",
               "Sub Saharan Africa": "ssa"}
SIX = {"KOR": "kor", "CHN": "chn", "BWA": "bwa", "ARG": "arg", "VEN": "ven", "COD": "cod"}


def long_run():
    d = maddison(["GBR", "NLD"], since=1300).dropna(subset=["gdppc"])
    p = d.pivot(index="year", columns="iso3", values="gdppc").rename(columns={"GBR": "gbr", "NLD": "nld"})
    w = maddison_regions("World").set_index("year")["gdppc"].rename("world")
    out = p.join(w, how="outer").round(0)
    out.index = out.index.astype(int)
    return out.reset_index()


def regions():
    d = maddison_regions(list(REGION_COLS))
    p = d.pivot(index="year", columns="region", values="gdppc")[list(REGION_COLS)]
    p = p.rename(columns=REGION_COLS).round(0)
    p.index = p.index.astype(int)
    return p.reset_index()


def six():
    d = maddison(list(SIX), since=1950)
    p = d.pivot(index="year", columns="iso3", values="gdppc")[list(SIX)].rename(columns=SIX).round(0)
    p.index = p.index.astype(int)
    return p.reset_index()


def tables():
    return long_run(), regions(), six()


if __name__ == "__main__":
    a, b, c = tables()
    write_table(a, __file__, "long_run_income")
    write_table(b, __file__, "income_by_region")
    write_table(c, __file__, "six_paths")

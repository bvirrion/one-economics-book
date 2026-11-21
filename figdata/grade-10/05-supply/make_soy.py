"""Area harvested of soya beans, Brazil and the United States, 1990-2024 (FAOSTAT, crops).

Grade 10, chapter 5 (supply): a long-run supply response that takes decades.
Writes out/soy_area.csv: year, bra, usa (million hectares harvested).
"""
import pandas as pd

from econdata import faostat_crops
from figout import write_table

COUNTRIES = {"Brazil": "bra", "United States of America": "usa"}


def table():
    f = faostat_crops(item="Soya beans", element="Area harvested")
    f = f[f.Area.isin(COUNTRIES) & (f.Year >= 1990)]
    p = f.pivot_table(index="Year", columns="Area", values="Value").rename(columns=COUNTRIES)
    p = (p[list(COUNTRIES.values())] / 1e6).round(2).reset_index().rename(columns={"Year": "year"})
    return p


if __name__ == "__main__":
    write_table(table(), __file__, "soy_area")

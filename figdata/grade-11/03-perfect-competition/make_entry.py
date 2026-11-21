"""Enterprise birth and death rates by industry, 2021: median over the reporting European countries.

Grade 11, chapter 3 (perfect-competition). Eurostat bd_size (business demography by size class), size class
TOTAL, indicators ENT_BRTHR_PC (enterprises born in the year, % of active enterprises) and ENT_DTHR_PC
(enterprises that died in the year, %), year 2021, median across countries reporting both.
Writes:
  out/entry.csv   label, nace, birth, death, n (countries), ordered by birth rate
"""
import pandas as pd

from econdata import eurostat
from figout import write_table

YEAR = 2021
SECTORS = {
    "B-S_X_O_S94": "whole business economy", "C": "manufacturing", "F": "construction", "G47": "retail trade",
    "H49": "land transport", "I56": "restaurants and bars", "J62": "computer programming", "L68": "real estate",
    "M69": "legal and accounting", "Q86": "health care", "S96": "hairdressing and other personal services",
}


def entry():
    d = eurostat("bd_size")
    d = d[(d.sizeclas == "TOTAL") & (d.time == YEAR) & d.nace_r2.isin(SECTORS)
          & d.indic_sbs.isin(["ENT_BRTHR_PC", "ENT_DTHR_PC"])].dropna(subset=["value"])
    w = d.pivot_table(index=["nace_r2", "geo"], columns="indic_sbs", values="value").dropna().reset_index()
    g = w.groupby("nace_r2").agg(birth=("ENT_BRTHR_PC", "median"), death=("ENT_DTHR_PC", "median"), n=("geo", "nunique"))
    g = g.reset_index().rename(columns={"nace_r2": "nace"})
    g["label"] = g.nace.map(SECTORS)
    g["birth"] = g.birth.round(1)
    g["death"] = g.death.round(1)
    return g.sort_values("birth").reset_index(drop=True)[["label", "nace", "birth", "death", "n"]]


if __name__ == "__main__":
    write_table(entry(), __file__, "entry")

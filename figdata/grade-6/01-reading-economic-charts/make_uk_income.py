"""Income per person in the United Kingdom, 1820-2022 (Maddison 2023, 2011 dollars).

Writes out/uk_income.csv (year, gdppc). Drawn twice in grade 6, chapter 1: on an
ordinary scale and on a times-ten scale.
"""
from econdata import maddison
from figout import write_table


def table():
    d = maddison("GBR", since=1820).dropna(subset=["gdppc"]).sort_values("year")
    return d.assign(gdppc=d.gdppc.round(0))[["year", "gdppc"]].reset_index(drop=True)


if __name__ == "__main__":
    write_table(table(), __file__, "uk_income")

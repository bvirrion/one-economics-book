"""Brenland's real GDP per person, 2000-2025 (invented economy, code/shared/country).

Grade 10, chapter 1 (economic-models): the weekend problem "Brenland's trend".
Writes out/brenland_gdppc.csv: year, gdppc (2015 dalens per person, rounded to the dalen)
= real_gdp (millions of 2015 dalens) / pop (thousands) * 1000.
"""
import country
from figout import write_table


def table():
    a = country.load("accounts")
    return a[["year"]].assign(gdppc=(a.real_gdp / a["pop"] * 1000).round(0).astype(int))


if __name__ == "__main__":
    write_table(table(), __file__, "brenland_gdppc")

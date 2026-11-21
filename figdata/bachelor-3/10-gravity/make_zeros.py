"""Chart 4: share of ordered country pairs with no recorded trade, by year, 1996--2020.
The derived file keeps positive flows only; a pair absent from it, between two
countries that each trade with someone that year, is counted as a zero.
Writes out/zeros.csv (year, countries, positive, zero_share in percent)."""
import pandas as pd
from econdata import gravity
from figout import write_table


def table():
    d = gravity(columns=["year", "iso3_o", "iso3_d"])
    rows = []
    for y, g in d.groupby("year"):
        n = len(set(g.iso3_o) | set(g.iso3_d))
        rows.append({"year": y, "countries": n, "positive": len(g),
                     "zero_share": 100 * (1 - len(g) / (n * (n - 1)))})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    write_table(table(), __file__, "zeros")

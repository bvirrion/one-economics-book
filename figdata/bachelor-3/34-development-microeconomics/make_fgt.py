"""Chart 2: headcount, poverty gap and squared poverty gap at 3.00 dollars a day (2021
PPP), eight countries, 2022, computed from the World Bank PIP percentile groups
(national, each group at its mean welfare, so the headcount moves in steps of one
point). Writes out/fgt.csv."""
import pandas as pd
from econdata import pip_percentiles
from fgt import fgt
from figout import write_table

Z, YEAR = 3.0, 2022
SHOWN = ["MOZ", "KEN", "NGA", "ZAF", "IDN", "BGD", "IND", "BRA"]


def table():
    p = pip_percentiles(SHOWN, [YEAR])
    p = p[p.reporting_level == "national"]
    rows = []
    for k, c in enumerate(SHOWN):
        s = p[p.iso3 == c]
        rows.append({"pos": len(SHOWN) - k, "iso3": c,
                     "welfare": s.welfare_type.iloc[0],
                     **{f"p{a}": 100 * fgt(s.avg_welfare, Z, a, s.pop_share)
                        for a in (0, 1, 2)}})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    write_table(table(), __file__, "fgt")

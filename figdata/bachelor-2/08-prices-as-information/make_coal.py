"""China's coal output by type of mine, 1978--1984, Book 4, chapter 8.

Reads src/zhang2018.csv, Table 12.2 of Zhang (2018): shares of national coal
production from centrally allocated mines, local government mines and
non-state mines (ledger b2:zhang2018-t2). Writes
  out/coal.csv          year, central, local, nonstate, total (sum of the printed
                        shares)
  out/coal_summary.csv  change in each share from 1978 to 1984, in points, and the
                        largest gap between a year's total and 100 (rounding)
"""

import pandas as pd
from cited import load_cited
from figout import write_table

COLS = ["central", "local", "nonstate"]


def table():
    d = load_cited(__file__, "zhang2018").drop(columns="ledger")
    d["year"] = d["year"].astype(int)
    for c in COLS:
        d[c] = d[c].astype(float)
    d["total"] = d[COLS].sum(axis=1).round(1)
    return d


def summary():
    d = table()
    first, last = d.iloc[0], d.iloc[-1]
    row = {f"{c}_change": round(last[c] - first[c], 1) for c in COLS}
    row["max_rounding"] = round((d.total - 100).abs().max(), 1)
    return pd.DataFrame([row])


if __name__ == "__main__":
    write_table(table(), __file__, "coal")
    write_table(summary(), __file__, "coal_summary")

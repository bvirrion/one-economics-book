"""Returns to betting on horses by type of bet, Book 4, chapter 8 opening chart.

Reads src/sw2010.csv, the rates of return per dollar bet to win that Snowberg and
Wolfers (2010) print in their text for US races of 1992--2001 (ledger
b2:sw2010-returns). Writes
  out/returns.csv          pos, bet, return (per cent), payback (dollars returned
                           per dollar bet)
  out/returns_summary.csv  the gap between the favourite and the longest odds, in
                           percentage points, and the payback of each end
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "sw2010").drop(columns="ledger")
    d["return"] = d["return"].astype(float)
    d["payback"] = (1 + d["return"] / 100).round(3)
    d.insert(0, "pos", range(1, len(d) + 1))
    return d


def summary():
    d = table()
    fav, longest = d.iloc[0], d.iloc[-1]
    return pd.DataFrame(
        [
            {
                "gap": round(fav["return"] - longest["return"], 1),
                "payback_favourite": fav.payback,
                "payback_longest": longest.payback,
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "returns")
    write_table(summary(), __file__, "returns_summary")

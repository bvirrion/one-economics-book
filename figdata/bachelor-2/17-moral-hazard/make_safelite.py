"""Safelite's switch to piece rates, chapter 17 opening chart.

Reads src/lazear2000.csv: the gains in output per worker per day that Lazear (2000)
reports in per cent, with the numbers behind them: the raw gain (Table 2 and the
text: 3.24 against 2.70 units, 0.54 units, 20 per cent) and the coefficients on the
piece-rate dummy in log output (Table 3, regressions 1 and 2: 0.368, which the paper
evaluates as 44 per cent, and 0.197, 22 per cent, within the same worker).
Writes
  out/safelite.csv          pos, label, pct (the paper's per cent)
  out/safelite_summary.csv  one row: raw, total, within, between (total - within, in
                            percentage points), within_share (within / total)
"""

import pandas as pd
from cited import load_cited
from figout import write_table

HOURLY = 2.70  # Table 2, units per worker per day under hourly wages


def table():
    d = load_cited(__file__, "lazear2000")
    raw = float(d.coef[d.estimate == "raw"].iloc[0])
    assert round(100 * raw / HOURLY) == int(d.pct[d.estimate == "raw"].iloc[0])
    pct = d.pct.astype(int)
    return pd.DataFrame({"pos": range(len(d), 0, -1), "label": d.label, "pct": pct})


def summary():
    t = table().set_index("label").pct
    total, within = t["Month and year controlled"], t["Same worker"]
    return pd.DataFrame(
        [
            {
                "raw": t["Raw means"],
                "total": total,
                "within": within,
                "between": round(total - within, 1),
                "within_share": round(within / total, 2),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "safelite")
    write_table(summary(), __file__, "safelite_summary")

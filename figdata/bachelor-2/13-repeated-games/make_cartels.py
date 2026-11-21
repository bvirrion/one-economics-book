"""Cartel duration in nine cross-section studies, chapter 13 opening chart.

Reads src/ls2006.csv, Table 1 of Levenstein and Suslow (2006): for each sample,
the number of cartels, the average duration in years and, where reported, the
range of durations (ledger b2:ls2006-t1). Writes
  out/cartels.csv          pos, sample, mean, minus, plus (distances from the mean
                           to the ends of the range; 0 where no range is
                           reported), sorted by the mean
  out/cartels_summary.csv  lowest and highest average, the median of the nine
                           averages, the longest reported duration, and the
                           number of studies with a range
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "ls2006").drop(columns="ledger")
    d = d.sort_values("mean_years", kind="stable").reset_index(drop=True)
    lo = pd.to_numeric(d.range_lo, errors="coerce")
    hi = pd.to_numeric(d.range_hi, errors="coerce")
    out = pd.DataFrame(
        {
            "pos": range(1, len(d) + 1),
            "sample": d["sample"],
            "mean": d.mean_years.astype(float),
            "minus": (d.mean_years - lo).fillna(0.0).round(1),
            "plus": (hi - d.mean_years).fillna(0.0).round(1),
        }
    )
    return out


def summary():
    d = load_cited(__file__, "ls2006")
    return pd.DataFrame(
        [
            {
                "lowest": d.mean_years.min(),
                "highest": d.mean_years.max(),
                "median": d.mean_years.median(),
                "longest": pd.to_numeric(d.range_hi, errors="coerce").max(),
                "with_range": int(
                    pd.to_numeric(d.range_hi, errors="coerce").notna().sum()
                ),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "cartels")
    write_table(summary(), __file__, "cartels_summary")

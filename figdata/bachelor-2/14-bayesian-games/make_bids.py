"""Fitted bid per unit of value of 18 subjects, chapter 14 opening chart.

Reads src/bh2003.csv, Table 1 of Bajari and Hortacsu (2003): the risk-aversion
coefficient r estimated for each subject of the Dyer, Kagel and Levin (1989)
first-price auctions, with 3 and with 6 bidders (ledger b2:bh2003-t1). The
estimate comes from the fitted slope of the subject's bids on values, through
slope = (N - 1) / (N - r); this script inverts that relation.
Writes
  out/bids.csv          subject (1 to 18), slope3, slope6
  out/bids_summary.csv  the risk-neutral slopes 2/3 and 5/6, the number of
                        subjects above, at and below each, and the mean slopes
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "bh2003")
    return pd.DataFrame(
        {
            "subject": range(1, len(d) + 1),
            "slope3": (2 / (3 - d.r3.astype(float))).round(4),
            "slope6": (5 / (6 - d.r6.astype(float))).round(4),
        }
    )


def summary():
    d = load_cited(__file__, "bh2003")
    r3, r6 = d.r3.astype(float), d.r6.astype(float)
    t = table()
    return pd.DataFrame(
        [
            {
                "rn3": round(2 / 3, 4),
                "rn6": round(5 / 6, 4),
                "above3": int((r3 > 0).sum()),
                "above6": int((r6 > 0).sum()),
                "at6": int((r6 == 0).sum()),
                "below6": int((r6 < 0).sum()),
                "mean3": round(t.slope3.mean(), 3),
                "mean6": round(t.slope6.mean(), 3),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "bids")
    write_table(summary(), __file__, "bids_summary")

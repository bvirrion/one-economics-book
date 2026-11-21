"""Laboratory markets converge: Smith (1962), Book 4, chapter 6 opening chart.

Reads src/smith1962.csv, Table 1 of Smith (1962): for each test (a laboratory market)
and trading period, the predicted and actual quantity, the predicted price p0, the
average contract price pbar and the coefficient of convergence alpha (ledger rows
b2:smith1962-t*). Rows are in the table's order, so the period is the row's rank within
its test. Writes
  out/smith_wide.csv     period, then <test>_ratio = 100 * pbar / p0 for the six tests
                         charted (T1, T4A, T6A, T7, T9A, T10); nan where a test had
                         fewer periods
  out/smith_alpha.csv    period, then <test>_alpha for the same tests
  out/smith_summary.csv  one row: n_tests (the ten tests of Table 1 with three or more
                         periods), the first and
                         last period's ratio for T6A and T7, the share of tests whose
                         alpha fell from the first to the last period
"""

import pandas as pd
from cited import load_cited
from figout import write_table

CHARTED = ["T1", "T4A", "T6A", "T7", "T9A", "T10"]


def table():
    d = load_cited(__file__, "smith1962").drop(columns="ledger")
    for c in ["x0", "x", "p0", "pbar", "alpha"]:
        d[c] = d[c].astype(float)
    d["period"] = d.groupby("test").cumcount() + 1
    d["ratio"] = (100 * d.pbar / d.p0).round(1)
    return d


def wide(col):
    d = table()
    w = d[d.test.isin(CHARTED)].pivot(index="period", columns="test", values=col)
    w = w[CHARTED]
    w.columns = [f"{c}_{'ratio' if col == 'ratio' else 'alpha'}" for c in w.columns]
    return w.reset_index().astype(object).fillna("nan")


def summary():
    d = table()
    first = d.groupby("test").first()
    last = d.groupby("test").last()
    fell = (last.alpha < first.alpha).mean()
    return pd.DataFrame(
        [
            {
                "n_tests": d.test.nunique(),
                "t6a_first": first.ratio["T6A"],
                "t6a_last": last.ratio["T6A"],
                "t7_first": first.ratio["T7"],
                "t7_last": last.ratio["T7"],
                "t4a_last": last.ratio["T4A"],
                "t9a_last": last.ratio["T9A"],
                "share_alpha_fell": round(100 * fell, 1),
            }
        ]
    )


if __name__ == "__main__":
    write_table(wide("ratio"), __file__, "smith_wide")
    write_table(wide("alpha"), __file__, "smith_alpha")
    write_table(summary(), __file__, "smith_summary")

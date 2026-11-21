"""Original against replication effect sizes, Book 4, chapter 5 opening chart.

Reads src/camerer2016.csv: Table S1 of Camerer et al. (2016), 18 laboratory
experiments published in two economics journals in 2011-2014, each with the original
and the replication effect size as a correlation coefficient r (ledger rows
b2:camerer2016-*). Writes
  out/replication_yes.csv  orig_r, rep_r for the 11 replications significant in the
                           original direction
  out/replication_no.csv   the same for the 7 that were not
  out/replication_summary.csv  one row: n, n_replicated, mean_orig, mean_rep (from
                           the two-decimal table, so within 0.002 of the paper's
                           0.474 and 0.279), n_smaller (replication r below the
                           original), n_negative (replication r below zero),
                           median_ratio (median of rep_r / orig_r)
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def table():
    return load_cited(__file__, "camerer2016").drop(columns="ledger")


def split():
    t = table()
    cols = ["orig_r", "rep_r"]
    return t[t.replicated == "Yes"][cols], t[t.replicated == "No"][cols]


def summary():
    t = table()
    return pd.DataFrame(
        [
            {
                "n": len(t),
                "n_replicated": int((t.replicated == "Yes").sum()),
                "mean_orig": round(t.orig_r.mean(), 3),
                "mean_rep": round(t.rep_r.mean(), 3),
                "n_smaller": int((t.rep_r < t.orig_r).sum()),
                "n_negative": int((t.rep_r < 0).sum()),
                "median_ratio": round((t.rep_r / t.orig_r).median(), 2),
            }
        ]
    )


if __name__ == "__main__":
    yes, no = split()
    write_table(yes, __file__, "replication_yes")
    write_table(no, __file__, "replication_no")
    write_table(summary(), __file__, "replication_summary")

"""Automatic enrolment in a 401(k) plan: Madrian and Shea (2000), Book 4, chapter 5.

Reads src/ms2000.csv (typed from the working paper's text; ledger rows b2:ms2000-*)
and writes out/defaults.csv: pos, window, new (per cent), one row per measure:
pos 1 = participating at 3-15 months of tenure, pos 2 = contributing at both
defaults (3 % of pay, all in the money market fund).
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "ms2000").drop(columns="ledger")
    return pd.DataFrame({"pos": [1, 2], "window": d.window.values, "new": d.new.values})


if __name__ == "__main__":
    write_table(table(), __file__, "defaults")

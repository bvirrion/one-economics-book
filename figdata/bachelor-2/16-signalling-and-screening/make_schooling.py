"""Mean 1975 earnings by years of schooling, men of the survey comparison sample of the
NSW job-training study (Dehejia and Wahba's files; 15,992 men aged 16 to 55).

Writes
  out/schooling.csv   education, mean (thousands of dollars), n, diploma and other (the
                      mean again, split into years 12 and 16 and the rest, for two
                      bar colours; nan elsewhere)
  out/summary.csv     one row: n, the jumps 11->12 and 15->16, and the largest other
                      year-to-year rise among years 9 to 18 (thousands of dollars),
                      the means at 11, 12, 15 and 16 in whole dollars, the top-code
                      (dollars) and the
                      number of men at it, and the number with zero earnings.
Book 4, chapter 16: opening chart.
"""

import pandas as pd
from econdata import nsw
from figout import write_table


def table():
    d = nsw("cps_controls")
    g = d.groupby("education").re75.agg(["mean", "count"]).reset_index()
    g.columns = ["education", "mean", "n"]
    g["mean"] = g["mean"] / 1000
    diploma = g.education.isin([12, 16])
    g["diploma"] = g["mean"].where(diploma)
    g["other"] = g["mean"].where(~diploma)
    return g


def summary():
    d = nsw("cps_controls")
    top = d.re75.max()
    t = table().set_index("education")["mean"]
    steps = t.diff()
    other = steps.loc[9:18].drop([12, 16])
    return pd.DataFrame(
        [
            {
                "n": int(table().n.sum()),
                "jump12": round(steps[12], 2),
                "jump16": round(steps[16], 2),
                "max_other": round(other.max(), 2),
                "dollars11": int(round(t[11] * 1000)),
                "dollars12": int(round(t[12] * 1000)),
                "dollars15": int(round(t[15] * 1000)),
                "dollars16": int(round(t[16] * 1000)),
                "topcode": round(top, 1),
                "n_top": int((d.re75 == top).sum()),
                "n_zero": int((d.re75 == 0).sum()),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "schooling")
    write_table(summary(), __file__, "summary")

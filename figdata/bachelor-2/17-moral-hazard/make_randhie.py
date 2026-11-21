"""Doctor visits by coinsurance rate in the RAND Health Insurance Experiment,
chapter 17 chart 2.

statsmodels' bundled randhie data (public domain; a subset of the experiment's
person-years, as distributed by Cameron and Trivedi): mdvis, outpatient visits to a
doctor in the year; lncoins = ln(coinsurance + 1). Only plans without an individual
deductible (idp = 0) are kept, so that the coinsurance rate describes the plan.
Writes
  out/randhie.csv          coins (per cent), mean, se, n, any (share with a visit)
  out/randhie_summary.csv  one row: free and 95-per-cent means, the fall in per cent,
                           and the number of person-years
"""

import numpy as np
import pandas as pd
from econdata import sm_dataset
from figout import write_table


def table():
    d = sm_dataset("randhie")
    d = d[d.idp == 0].copy()
    d["coins"] = np.round(np.exp(d.lncoins) - 1).astype(int)
    g = d.groupby("coins").mdvis
    out = pd.DataFrame(
        {
            "mean": g.mean(),
            "se": g.sem(),
            "n": g.size(),
            "any": g.apply(lambda x: (x > 0).mean()),
        }
    ).reset_index()
    return out.round(3)


def summary():
    t = table().set_index("coins")
    free, high = t.loc[0, "mean"], t.loc[95, "mean"]
    return pd.DataFrame(
        [
            {
                "free": free,
                "c25": t.loc[25, "mean"],
                "c50": t.loc[50, "mean"],
                "c95": high,
                "fall_pct": round(100 * (1 - high / free), 1),
                "n": int(t.n.sum()),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "randhie")
    write_table(summary(), __file__, "randhie_summary")

"""The estimated return to schooling as controls are added, chapter 30.

Data: the CPS comparison sample of LaLonde (1986) as distributed by Dehejia and
Wahba (`nsw("cps_controls")`, 15,992 men). Sample: men with positive earnings in
1975 and 1978. Outcome: log 1978 earnings. Controls added one at a time, in this
order: age, age squared, black, hispanic, married, log 1975 earnings.
Writes
  out/steps.csv    step, label, b, lo, hi (education coefficient, per cent, 95 % CI)
  out/sample.csv   one row: n, share_capped (share of all 15,992 men at the maximum
                   1978 earnings), cap
"""

import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from econdata import nsw
from figout import write_table

CONTROLS = ["age", "age2", "black", "hispanic", "married", "lre75"]
LABELS = ["none", "+ age", "+ age sq.", "+ black", "+ hispanic", "+ married",
          "+ log earn. 1975"]  # fmt: skip


def sample():
    d = nsw("cps_controls")
    d = d[(d.re78 > 0) & (d.re75 > 0)].copy()
    d["lre78"] = np.log(d.re78)
    d["lre75"] = np.log(d.re75)
    d["age2"] = d.age**2
    return d


def steps():
    d = sample()
    rows = []
    for k in range(len(CONTROLS) + 1):
        f = "lre78 ~ " + " + ".join(["education"] + CONTROLS[:k])
        m = smf.ols(f, d).fit()
        lo, hi = m.conf_int().loc["education"]
        b = m.params.education
        rows.append({"step": k, "label": LABELS[k], "b": round(100 * b, 2),
                     "lo": round(100 * lo, 2), "hi": round(100 * hi, 2)})  # fmt: skip
    return pd.DataFrame(rows)


def sample_summary():
    full = nsw("cps_controls")
    cap = full.re78.max()
    share = round((full.re78 == cap).mean(), 3)
    return pd.DataFrame(
        [{"n": len(sample()), "share_capped": share, "cap": round(cap, 1)}]
    )


if __name__ == "__main__":
    write_table(steps(), __file__, "steps")
    write_table(sample_summary(), __file__, "sample")

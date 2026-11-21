"""The National Supported Work experiment: mean 1978 earnings by group, chapter 33.

Data: Dehejia-Wahba subsample of LaLonde's NSW men (`nsw("nsw_dw")`, 185 treated, 260
controls). Mean re78 with a 95 % interval (mean +/- 1.96 s.e., s.e. = s.d. / sqrt(n)).
Writes
  out/means.csv   group (0 control, 1 treated), label, mean, se, lo, hi, n
"""

import numpy as np
import pandas as pd
from econdata import nsw
from figout import write_table


def means():
    d = nsw("nsw_dw")
    g = d.groupby("treat").re78.agg(["mean", "std", "count"])
    se = g["std"] / np.sqrt(g["count"])
    return pd.DataFrame(
        {
            "group": g.index,
            "label": ["control", "treated"],
            "mean": g["mean"].round(0).values,
            "se": se.round(0).values,
            "lo": (g["mean"] - 1.96 * se).round(0).values,
            "hi": (g["mean"] + 1.96 * se).round(0).values,
            "n": g["count"].values,
        }
    )


if __name__ == "__main__":
    write_table(means(), __file__, "means")

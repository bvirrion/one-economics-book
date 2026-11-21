"""Opening chart and chart 2: marginal effective tax rate and net income of a
single parent with two children, United States, 2024 (federal taxes and credits).
Writes out/mtr.csv (earnings, net income, rate over the preceding 100 dollars,
plotted at the midpoint), out/mtr_points.csv and out/mtr_stats.csv."""
import numpy as np
import pandas as pd
from figout import write_table
from us2024 import PHASE_IN, PHASE_OUT, net_income, schedule


def tables():
    e, n, mtr = schedule()
    t = pd.DataFrame({"earnings": e, "net": n, "mtr": mtr, "mid": e - 50})
    pts = pd.DataFrame({"earnings": [0, 10_000, 20_000, 30_000, 40_000, 50_000,
                                     60_000]})
    pts["net"] = [net_income(x) for x in pts.earnings]
    pts["ptr"] = [np.nan] + [100 * (1 - (net_income(x) - net_income(0)) / x)
                             for x in pts.earnings[1:]]
    flat = t.dropna()
    stats = pd.DataFrame({"stat": ["phase_in", "phase_out", "mtr_min", "mtr_max",
                                   "mtr_at_40000"],
                          "value": [100 * PHASE_IN, 100 * PHASE_OUT, flat.mtr.min(),
                                    flat.mtr.max(),
                                    t.loc[t.earnings == 40_000, "mtr"].iloc[0]]})
    return t[["mid", "earnings", "net", "mtr"]], pts, stats


if __name__ == "__main__":
    t, p, s = tables()
    write_table(t.iloc[1:].reset_index(drop=True), __file__, "mtr")
    write_table(p, __file__, "mtr_points")
    write_table(s, __file__, "mtr_stats")

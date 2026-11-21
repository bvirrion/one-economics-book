"""Chart 2: the window trade-off. 300 simulated samples of the opening chart's elections
(seeds 0-299; true jump 0.077); for each window, the mean estimate and its standard
deviation, for a local constant (difference of means) and a local linear fit.
Writes out/bandwidth.csv (h, const_mean, const_sd, lin_mean, lin_sd).
Book 5, chapter 4, chart 2.
"""
import numpy as np
import pandas as pd
from figout import write_table
from rdsim import draw, jump

WINDOWS = [0.02, 0.03, 0.05, 0.075, 0.1, 0.15, 0.2, 0.25, 0.35, 0.5]


def table():
    est = {(d, h): [] for d in (0, 1) for h in WINDOWS}
    for s in range(300):
        m, y, _ = draw(seed=s)
        for d in (0, 1):
            for h in WINDOWS:
                est[d, h].append(jump(m, y, 0, h, degree=d))
    rows = [(h, np.mean(est[0, h]), np.std(est[0, h]), np.mean(est[1, h]),
             np.std(est[1, h])) for h in WINDOWS]
    return pd.DataFrame(rows, columns=["h", "const_mean", "const_sd", "lin_mean", "lin_sd"])


if __name__ == "__main__":
    write_table(table(), __file__, "bandwidth")

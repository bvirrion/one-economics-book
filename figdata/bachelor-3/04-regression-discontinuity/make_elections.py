"""Opening chart: simulated close elections, calibrated on a published jump of 0.077 in
the next vote share (ledger b3rd:lee08.vote). 6,000 elections; bins of 0.02 in the
margin; local linear fits on each side with a window of 0.25.
Writes out/elections_bins.csv (margin, share, n) and out/elections_fit.csv (side, margin,
fit). Book 5, chapter 4, opening chart.
"""
import numpy as np
import pandas as pd
from figout import write_table
from rdsim import draw, side_fit

H = 0.25


def tables():
    m, y, _ = draw()
    b = np.floor(m / 0.02)
    bins = (pd.DataFrame({"bin": b, "m": m, "y": y}).groupby("bin")
            .agg(margin=("m", "mean"), share=("y", "mean"), n=("y", "size"))
            .reset_index(drop=True))
    rows = []
    for side, mask, ends in (("left", m < 0, (-H, 0)), ("right", m >= 0, (0, H))):
        a, s = side_fit(m[mask], y[mask], H)
        for e in ends:
            rows.append((side, e, a + s * e))
    return bins, pd.DataFrame(rows, columns=["side", "margin", "fit"])


if __name__ == "__main__":
    bins, fit = tables()
    write_table(bins, __file__, "elections_bins")
    write_table(fit[fit.side == "left"].drop(columns="side"), __file__, "elections_fit_left")
    write_table(fit[fit.side == "right"].drop(columns="side"), __file__, "elections_fit_right")

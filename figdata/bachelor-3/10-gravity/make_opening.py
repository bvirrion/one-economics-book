"""Opening chart: bilateral trade in 2019 against GDP_o x GDP_d / distance, binned into
50 groups of equal size by the x variable (means of natural logs within each bin;
GDPs and trade in millions of dollars, distance in km), plus the
least-squares line on all pairs. Writes out/opening_bins.csv, out/opening_fit.csv and
out/opening_stats.csv (pairs, slope, R-squared on all pairs)."""
import numpy as np
import pandas as pd
from econdata import gravity
from figout import write_table

COLS = ["year", "iso3_o", "iso3_d", "tradeflow_baci", "gdp_o", "gdp_d", "dist"]


def tables():
    d = gravity(since=2019, until=2019, columns=COLS).dropna()
    # trade in millions of dollars; GDP in millions of dollars squared per km, in logs
    x = np.log(d.gdp_o / 1e3) + np.log(d.gdp_d / 1e3) - np.log(d.dist)
    y = np.log(d.tradeflow_baci / 1e3)
    b, a = np.polyfit(x, y, 1)
    r2 = np.corrcoef(x, y)[0, 1] ** 2
    bins = pd.qcut(x.rank(method="first"), 50, labels=False)
    g = pd.DataFrame({"x": x, "y": y, "bin": bins}).groupby("bin").mean()
    binned = pd.DataFrame({"lx": g.x.values, "ly": g.y.values})
    xs = np.array([g.x.min(), g.x.max()])  # the line over the range of the bins
    fit = pd.DataFrame({"lx": xs, "ly": a + b * xs})
    stats = pd.DataFrame({"stat": ["pairs", "slope", "r2"], "value": [len(d), b, r2]})
    return binned, fit, stats


if __name__ == "__main__":
    binned, fit, stats = tables()
    write_table(binned, __file__, "opening_bins")
    write_table(fit, __file__, "opening_fit")
    write_table(stats, __file__, "opening_stats")

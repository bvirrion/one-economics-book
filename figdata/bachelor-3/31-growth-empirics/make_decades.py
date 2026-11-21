"""Opening chart: annual growth of real GDP per person by country, decade by decade,
1960s to 2010s (PWT 11.0 rgdpna / pop, the series PWT recommends for growth; the 2010s
are 2010--2019). Each country with
data at both ends of a decade is a dot; dots are spread horizontally by rank. Writes
out/decades.csv (pos, growth), out/decades_median.csv and out/decades_stats.csv
(count, median, interquartile range and the share below zero per decade, and the mean
correlation between successive decades)."""
import numpy as np
import pandas as pd
from figout import write_table
from growthdata import growth, income_na

DECADES = [(1960, 1970), (1970, 1980), (1980, 1990), (1990, 2000), (2000, 2010),
           (2010, 2019)]


def tables():
    w = income_na()
    dots, stats, gs = [], [], []
    for k, (a, b) in enumerate(DECADES):
        g = growth(w, a, b)
        gs.append(g)
        r = g.rank(method="first").to_numpy()
        dots.append(pd.DataFrame({"pos": k + 0.6 * (r / len(g) - 0.5),
                                  "growth": g.clip(-8, 12).to_numpy()}))
        q = g.quantile([0.25, 0.5, 0.75])
        stats.append({"decade": f"{a}s", "n": len(g), "median": q[0.5],
                      "iqr": q[0.75] - q[0.25], "below0": 100 * (g < 0).mean(),
                      "clipped": int(((g < -8) | (g > 12)).sum())})
    corrs = [pd.concat([gs[i], gs[i + 1]], axis=1).dropna().corr().iloc[0, 1]
             for i in range(len(gs) - 1)]
    st = pd.DataFrame(stats)
    st["corr_next"] = corrs + [np.nan]
    med = pd.DataFrame({"pos": range(len(DECADES)), "median": st["median"]})
    return pd.concat(dots, ignore_index=True), med, st


if __name__ == "__main__":
    d, m, s = tables()
    write_table(d, __file__, "decades")
    write_table(m, __file__, "decades_median")
    write_table(s, __file__, "decades_stats")

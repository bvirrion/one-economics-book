"""Charts of b1 ch. 32.

school: PSID comparison sample, men with positive 1978 earnings: mean log earnings by
years of schooling (8 to 17 years, with counts) and the least-squares line fitted on all
2,204 men. fit: the slope, intercept, R^2, n.
toward: PSID, mean 1975 and mean 1978 earnings by bins of 1975 earnings (5,000 dollars wide, bins with
at least 20 men), and the 45-degree line.
omitted: slopes from 1,000 simulated samples of 500 (the simulation of listing
omitted.py, same seed and steps), as densities over bins of 0.002.
"""
import numpy as np
import pandas as pd
from econdata import nsw
from figout import write_table

d = nsw("psid_controls").query("re78 > 0")
y = np.log(d.re78)
b1, b0 = np.polyfit(d.education, y, 1)
r2 = np.corrcoef(d.education, y)[0, 1] ** 2
write_table(pd.DataFrame([{"n": len(d), "slope": round(b1, 4), "intercept": round(b0, 4),
                           "r2": round(r2, 4)}]), __file__, "fit")
g = d.assign(ly=y).query("8 <= education <= 17").groupby("education").ly.agg(["count", "mean"])
g = g.reset_index().round(4)
g["line"] = (b0 + b1 * g.education).round(4)
write_table(g, __file__, "school")

p = nsw("psid_controls")
p["bin"] = (p.re75 // 5_000) * 5_000 + 2_500
t = p.groupby("bin").agg(n=("re78", "size"), re75=("re75", "mean"), re78=("re78", "mean")).reset_index()
t = t[t.n >= 20].round(0)
write_table(t, __file__, "toward")

rng = np.random.default_rng(2026)
short, long_ = [], []
for _ in range(1_000):
    ability = rng.standard_normal(500)
    school = 12 + 1.5 * ability + rng.normal(0, 2, 500)
    log_y = 9 + 0.06 * school + 0.10 * ability + rng.normal(0, 0.5, 500)
    short.append(np.polyfit(school, log_y, 1)[0])
    X = np.column_stack([np.ones(500), school, ability])
    long_.append(np.linalg.lstsq(X, log_y, rcond=None)[0][1])
edges = np.arange(0.03, 0.1101, 0.002)
hs, _ = np.histogram(short, bins=edges)
hl, _ = np.histogram(long_, bins=edges)
write_table(pd.DataFrame({"mid": (edges[:-1] + 0.001).round(4), "short": hs / 1_000 / 0.002,
                          "long": hl / 1_000 / 0.002}).round(3), __file__, "omitted")
write_table(pd.DataFrame([{"short": round(np.mean(short), 4), "long": round(np.mean(long_), 4)}]),
            __file__, "omitted_means")

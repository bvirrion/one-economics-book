"""Charts of b1 ch. 30.

means: 10,000 sample means of 1978 earnings (PSID comparison sample, 2,490 men, drawn with
replacement, seed 2026) for n = 5, 30 and 200, as densities over bins of 1,000 dollars.
means_stats: the standard deviation of the means against sigma/sqrt(n).
cef: PSID mean earnings by years of schooling (8-17) and the least-squares line.
"""
import numpy as np
import pandas as pd
from econdata import nsw
from figout import write_table

y = nsw("psid_controls").re78.to_numpy()
sigma = y.std()
rng = np.random.default_rng(2026)
edges = np.arange(0, 50_001, 1_000)
out = {"mid": edges[:-1] + 500}
st = []
for n in (5, 30, 200):
    m = rng.choice(y, size=(10_000, n)).mean(axis=1)
    c, _ = np.histogram(m, bins=edges)
    out[f"n{n}"] = (c / (10_000 * 1_000) * 1e4).round(4)  # density per 10,000 dollars
    st.append({"n": n, "sd": round(m.std(), 1), "se": round(sigma / np.sqrt(n), 1)})
write_table(pd.DataFrame(out), __file__, "means")
write_table(pd.DataFrame(st), __file__, "means_stats")
write_table(pd.DataFrame([{"mu": round(y.mean(), 1), "sigma": round(sigma, 1)}]), __file__, "pop")

d = nsw("psid_controls")
d = d[d.education.between(8, 17)]
g = d.groupby("education").re78.mean().round(0).reset_index()
b, a = np.polyfit(d.education, d.re78, 1)
g["line"] = (a + b * g.education).round(0)
write_table(g, __file__, "cef")

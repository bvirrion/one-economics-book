"""Exercise 12: a Mariel-style difference in differences on an invented panel.

Two cities, 1975-1986. Wages of low-skilled workers have a true effect of zero from
the shock in 1980. Workers are of two kinds whose wages differ by 0.30 log points;
in the treated city the share of the lower-paid kind in the survey sample rises
from 0.3 to 0.6 after 1980 for reasons unrelated to the shock. Compare the DiD on
raw means with the DiD within kinds.
"""
import numpy as np
import pandas as pd

rng = np.random.default_rng(1980)
rows = []
for city in ("treated", "control"):
    for year in range(1975, 1987):
        share = 0.6 if (city == "treated" and year >= 1980) else 0.3
        n = 60
        low = rng.random(n) < share
        lw = 2.0 + 0.01 * (year - 1975) - 0.30 * low + rng.normal(0, 0.2, n)
        rows += [(city, year, int(k), v) for k, v in zip(low, lw)]
d = pd.DataFrame(rows, columns=["city", "year", "low", "lw"])
d["post"] = d.year >= 1980


def did(x):
    m = x.groupby(["city", "post"]).lw.mean()
    return (m["treated", True] - m["treated", False]) - (
        m["control", True] - m["control", False])


print(f"DiD on raw means: {did(d):.3f}")
within = np.mean([did(d[d.low == k]) for k in (0, 1)])
print(f"DiD within kinds (average of the two): {within:.3f}")

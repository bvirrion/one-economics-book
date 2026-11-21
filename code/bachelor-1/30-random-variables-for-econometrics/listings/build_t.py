"""Student's t built from normal variables, against scipy's."""

import numpy as np
from scipy import stats

rng = np.random.default_rng(2026)
k, draws = 5, 200_000
z = rng.standard_normal(draws)
v = (rng.standard_normal((draws, k)) ** 2).sum(axis=1)  # chi-square with k degrees
t = z / np.sqrt(v / k)
for p in (0.9, 0.95, 0.975, 0.99):
    print(
        f"{p:5.3f}  simulated {np.quantile(t, p):6.3f}  exact {stats.t.ppf(p, k):6.3f}"
    )

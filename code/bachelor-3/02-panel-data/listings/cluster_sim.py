"""Placebo laws: 50 states, 20 years, errors that persist within a state.
How often does a law with no effect look significant at 5 %?"""
import numpy as np
from paneltools import ols_cluster

rng = np.random.default_rng(8)
states, years, reps, rho = 50, 20, 500, 0.8
unit = np.repeat(np.arange(states), years)
reject = {"se_iid": 0, "se_hc1": 0, "se_cluster": 0}


def two_way(m):
    """Remove state and year means (exact for a balanced panel)."""
    return m - m.mean(1, keepdims=True) - m.mean(0) + m.mean()


for _ in range(reps):
    e = np.zeros((states, years))
    e[:, 0] = rng.normal(size=states)
    for s in range(1, years):                       # AR(1) inside each state
        e[:, s] = rho * e[:, s - 1] + np.sqrt(1 - rho**2) * rng.normal(size=states)
    treated = rng.permutation(states) < states // 2
    start = rng.integers(5, 16)
    law = (treated[:, None] & (np.arange(years) >= start)).astype(float)
    y, x = two_way(e).ravel(), two_way(law).ravel()
    r = ols_cluster(y, x, unit)
    for k in reject:
        reject[k] += abs(r["beta"][0] / r[k][0]) > 1.96
for k, v in reject.items():
    print(f"{k:11s} rejects the true zero in {v / reps:.3f} of the samples")

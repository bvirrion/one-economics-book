"""Exercise 11: extreme bounds on an invented cross-country table. Growth of 80
invented countries depends on investment and on one of six other candidates; the
others are noise correlated with investment. For each candidate, regress growth on it
with every combination of up to three of the others and print the lowest and highest
estimate (each less or plus two standard errors). A variable is robust if the bounds
keep one sign."""
from itertools import combinations

import numpy as np

rng = np.random.default_rng(11)
n = 80
inv = rng.normal(0, 1, n)
z = {"investment": inv, "schooling": 0.5 * inv + rng.normal(0, 1, n)}
for k in ("openness", "inflation", "religion", "latitude", "war"):
    z[k] = 0.4 * inv + rng.normal(0, 1, n)
growth = 1.0 * inv + 0.3 * z["schooling"] + rng.normal(0, 1, n)
names = list(z)
for v in names:
    others = [o for o in names if o != v]
    lo, hi = np.inf, -np.inf
    for k in range(4):
        for extra in combinations(others, k):
            X = np.column_stack([np.ones(n), z[v]] + [z[o] for o in extra])
            b, *_ = np.linalg.lstsq(X, growth, rcond=None)
            e = growth - X @ b
            se = np.sqrt(e @ e / (n - X.shape[1]) * np.linalg.inv(X.T @ X)[1, 1])
            lo, hi = min(lo, b[1] - 2 * se), max(hi, b[1] + 2 * se)
    verdict = "robust" if lo > 0 or hi < 0 else "fragile"
    print(f"{v:10s} bounds [{lo:+.2f}, {hi:+.2f}] {verdict}")

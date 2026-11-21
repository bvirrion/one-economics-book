"""Twenty unrelated regressors; keep the best one. How often is it 'significant'?"""

import numpy as np
from scipy import stats

rng = np.random.default_rng(32)
n, k, reps = 100, 20, 5000
naive = bonferroni = 0
for _ in range(reps):
    y = rng.standard_normal(n)
    X = rng.standard_normal((n, k))  # none of them is related to y
    r = np.array([np.corrcoef(X[:, j], y)[0, 1] for j in range(k)])
    t = r * np.sqrt((n - 2) / (1 - r**2))
    p = 2 * stats.t.sf(np.abs(t), n - 2)
    naive += p.min() < 0.05
    bonferroni += p.min() < 0.05 / k

print(f"best of {k} significant at 5 %:        {naive / reps:.3f}")
print(f"formula 1 - 0.95^{k}:                  {1 - 0.95**k:.3f}")
print(f"best of {k} below 0.05 / {k} (Bonferroni): {bonferroni / reps:.3f}")

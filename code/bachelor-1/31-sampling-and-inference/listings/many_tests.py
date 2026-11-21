"""Twenty placebo tests: random halves of the PSID sample compared."""

import numpy as np
from econdata import nsw
from scipy import stats

y = nsw("psid_controls").re78.to_numpy()
rng = np.random.default_rng(7)
p = []
for _ in range(20):
    mask = rng.permutation(len(y)) < len(y) // 2  # a random half, no treatment at all
    p.append(stats.ttest_ind(y[mask], y[~mask], equal_var=False).pvalue)
p = np.array(p)
print("smallest p-values:", np.round(np.sort(p)[:3], 4))
print(f"rejections at 5%: {(p < 0.05).sum()} of 20; expected 1")
print(f"Bonferroni threshold 0.05/20 = {0.05 / 20}; rejections: {(p < 0.0025).sum()}")

"""The experiment's estimate: treated against controls, 1978 earnings."""

import numpy as np
from econdata import nsw
from scipy import stats

d = nsw("nsw_dw")
t1, t0 = d.re78[d.treat == 1], d.re78[d.treat == 0]
diff = t1.mean() - t0.mean()
se = np.sqrt(t1.var() / len(t1) + t0.var() / len(t0))
t = diff / se
p_normal = 2 * stats.norm.sf(abs(t))
print(f"treated {len(t1)}, mean {t1.mean():,.0f}", end="; ")
print(f"controls {len(t0)}, mean {t0.mean():,.0f}")
print(f"difference {diff:,.1f}, standard error {se:,.1f}, t {t:.3f}")
print(f"p-value (normal) {p_normal:.4f}")
r = stats.ttest_ind(t1, t0, equal_var=False)
print(f"scipy (Welch):   t {r.statistic:.3f}, p-value {r.pvalue:.4f}")
print(f"95% interval: {diff - 1.96 * se:,.0f} to {diff + 1.96 * se:,.0f}")
for v in ("re74", "re75"):  # a check of the random assignment: earnings before
    a1, a0 = d[v][d.treat == 1], d[v][d.treat == 0]
    b = stats.ttest_ind(a1, a0, equal_var=False)
    print(f"{v}: treated {a1.mean():,.0f}, controls {a0.mean():,.0f}, p {b.pvalue:.2f}")

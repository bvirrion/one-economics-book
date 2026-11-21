"""Power to detect a 1,000-dollar effect with the experiment's sample sizes."""

import numpy as np
from econdata import nsw
from scipy import stats

d = nsw("nsw_dw")
y0 = d.re78[d.treat == 0].to_numpy()
n1, n0, effect = 185, 260, 1_000
se = np.sqrt(y0.var(ddof=1) * (1 / n1 + 1 / n0))  # one sd for both groups
power = stats.norm.sf(1.96 - effect / se) + stats.norm.cdf(-1.96 - effect / se)
print(f"standard error {se:,.0f}; power by the formula {power:.3f}")
rng = np.random.default_rng(2026)
reject = 0
for _ in range(4_000):  # draws from the control earnings, shifted by the effect
    a, b = rng.choice(y0, n1) + effect, rng.choice(y0, n0)
    reject += stats.ttest_ind(a, b, equal_var=False).pvalue < 0.05
print(f"power by simulation {reject / 4_000:.3f}")

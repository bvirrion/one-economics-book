"""Mean 1978 earnings of the experiment's control group, with a 95% interval."""

import numpy as np
from econdata import nsw
from scipy import stats

y = nsw("nsw_dw").query("treat == 0").re78
n, mean, s = len(y), y.mean(), y.std()  # pandas divides by n - 1
se = s / np.sqrt(n)
c = stats.t.ppf(0.975, n - 1)
print(f"n {n}, mean {mean:,.0f}, s {s:,.0f}, standard error {se:,.0f}")
print(
    f"95% interval: {mean - c * se:,.0f} to {mean + c * se:,.0f} (t quantile {c:.3f})"
)

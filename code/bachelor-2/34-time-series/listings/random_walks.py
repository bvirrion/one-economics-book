"""Spurious regression: independent random walks, regressed on each other."""

import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(34)
n, reps = 200, 2000
levels = diffs = 0
r2 = []
for _ in range(reps):
    x = rng.standard_normal(n).cumsum()
    y = rng.standard_normal(n).cumsum()  # independent of x
    fit = sm.OLS(y, sm.add_constant(x)).fit()
    levels += abs(fit.tvalues[1]) > 1.96
    r2.append(fit.rsquared)
    fit_d = sm.OLS(np.diff(y), sm.add_constant(np.diff(x))).fit()
    diffs += abs(fit_d.tvalues[1]) > 1.96

print(f"levels:      |t| > 1.96 in {levels / reps:.3f} of samples")
print(f"             median R2 {np.median(r2):.3f}")
print(f"differences: |t| > 1.96 in {diffs / reps:.3f} of samples")

"""Least squares by hand: log earnings on years of schooling, PSID sample."""

import numpy as np
from econdata import nsw

d = nsw("psid_controls").query("re78 > 0")  # the log needs positive earnings
x, y = d.education.to_numpy(float), np.log(d.re78.to_numpy())
b1 = ((x - x.mean()) * (y - y.mean())).sum() / ((x - x.mean()) ** 2).sum()
b0 = y.mean() - b1 * x.mean()
resid = y - (b0 + b1 * x)
print(f"n {len(y)}; slope {b1:.4f}; intercept {b0:.4f}")
print(f"sum of residuals {resid.sum():.2e}")
print(f"sum of x times residuals {(x * resid).sum():.2e}")

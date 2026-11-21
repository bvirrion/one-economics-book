"""Covariance and correlation: earnings in 1975 and 1978, and a parabola."""

import numpy as np
from econdata import nsw

d = nsw("psid_controls")
x, y = d.re75, d.re78
n = len(d)
cov = ((x - x.mean()) * (y - y.mean())).sum() / (n - 1)
r = cov / (x.std() * y.std())  # pandas' std divides by n - 1 too
print(f"by hand:     cov {cov:,.0f}  r {r:.4f}")
print(f"with pandas: cov {x.cov(y):,.0f}  r {x.corr(y):.4f}")

rng = np.random.default_rng(2026)
u = rng.uniform(-1, 1, 1000)
v = u**2  # v is a function of u, yet ...
print(f"parabola:    r {np.corrcoef(u, v)[0, 1]:.4f}")

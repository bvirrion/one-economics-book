"""Least squares by the normal equations, against statsmodels."""

import numpy as np
import statsmodels.api as sm
from econdata import nsw

d = nsw("cps_controls")
d = d[(d.re78 > 0) & (d.re75 > 0)]
y = np.log(d.re78).to_numpy()
names = ["const", "education", "age", "age2", "black", "hispanic", "married"]
cols = [np.ones(len(d)), d.education, d.age, d.age**2, d.black, d.hispanic, d.married]
X = np.column_stack(cols)
n, k = X.shape

beta = np.linalg.solve(X.T @ X, X.T @ y)  # the normal equations X'X b = X'y
fit = sm.OLS(y, X).fit()
for name, b, b_sm in zip(names, beta, fit.params):
    print(f"{name:10s} {b:12.6f} {b_sm:12.6f}")
print("same coefficients to 1e-8:", np.allclose(beta, fit.params, rtol=0, atol=1e-8))

e = y - X @ beta
print("residuals orthogonal to every column:", np.allclose(X.T @ e, 0, atol=1e-5))
r2 = 1 - (e @ e) / ((y - y.mean()) @ (y - y.mean()))
adj = 1 - (1 - r2) * (n - 1) / (n - k)
print(f"R2 {r2:.4f} ({fit.rsquared:.4f}), adjusted {adj:.4f} ({fit.rsquared_adj:.4f})")

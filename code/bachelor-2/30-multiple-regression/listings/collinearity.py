"""Near-collinear regressors: the standard error of b1 as the correlation rises."""

import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(30)
n = 500
print("  rho   corr in sample   b1     se(b1)    VIF")
for rho in (0.0, 0.5, 0.9, 0.99):
    x1 = rng.standard_normal(n)
    x2 = rho * x1 + np.sqrt(1 - rho**2) * rng.standard_normal(n)
    y = 1 + x1 + x2 + rng.standard_normal(n)
    fit = sm.OLS(y, sm.add_constant(np.column_stack([x1, x2]))).fit()
    r = np.corrcoef(x1, x2)[0, 1]
    vif = 1 / (1 - r**2)
    print(f"{rho:5.2f}  {r:14.3f}  {fit.params[1]:6.3f}  {fit.bse[1]:7.3f}  {vif:6.1f}")

x1 = rng.standard_normal(n)
X = np.column_stack([np.ones(n), x1, 2 * x1])
print(f"rank of X with x2 = 2 x1: {np.linalg.matrix_rank(X)} of {X.shape[1]} columns")

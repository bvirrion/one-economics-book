"""Least squares against another linear unbiased estimator of the slope."""

import numpy as np

rng = np.random.default_rng(31)
n, sigma = 40, 2.0
x = np.linspace(0, 10, n)  # fixed regressor
low, high = x < np.median(x), x >= np.median(x)


def ols_slope(y):
    xd = x - x.mean()
    return xd @ y / (xd @ xd)


def group_slope(y):
    """Difference of group means: linear in y and unbiased, but not least squares."""
    return (y[high].mean() - y[low].mean()) / (x[high].mean() - x[low].mean())


samples = 1 + 0.5 * x + sigma * rng.standard_normal((20000, n))
draws = np.array([[ols_slope(y), group_slope(y)] for y in samples])
print("            mean    variance (simulated)   variance (formula)")
var_ols = sigma**2 / ((x - x.mean()) @ (x - x.mean()))
gap = x[high].mean() - x[low].mean()
var_group = sigma**2 * (1 / high.sum() + 1 / low.sum()) / gap**2
for name, col, v in (("OLS", 0, var_ols), ("groups", 1, var_group)):
    print(f"{name:8s} {draws[:, col].mean():7.4f}  {draws[:, col].var():12.5f}"
          f"  {v:20.5f}")  # fmt: skip

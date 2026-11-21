"""Measurement error in the regressor and in the outcome."""

import numpy as np

rng = np.random.default_rng(32)
n, beta = 100_000, 2.0
x_true = rng.standard_normal(n)
y_true = 1 + beta * x_true + rng.standard_normal(n)


def slope(x, y):
    return np.cov(x, y)[0, 1] / np.var(x, ddof=1)


print("error variance   slope (x noisy)   lambda * beta   slope (y noisy)")
for s2 in (0.0, 0.25, 1.0, 4.0):
    x = x_true + np.sqrt(s2) * rng.standard_normal(n)
    y = y_true + np.sqrt(s2) * rng.standard_normal(n)
    lam = 1 / (1 + s2)
    print(f"{s2:14.2f}  {slope(x, y_true):16.3f}  {lam * beta:14.3f}"
          f"  {slope(x_true, y):15.3f}")  # fmt: skip

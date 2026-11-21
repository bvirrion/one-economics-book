"""What share of consumers spend their current income? Campbell and Mankiw's test on
United States quarterly data, 1959-2009 (statsmodels' bundled macrodata).

Regress consumption growth on income growth, using as instruments what was known two
to four quarters earlier: lagged growth of income and of consumption.
"""

import numpy as np
from statsmodels.datasets import macrodata

d = macrodata.load_pandas().data
dc = 100 * np.diff(np.log(d.realcons.to_numpy()))
dy = 100 * np.diff(np.log(d.realdpi.to_numpy()))
t = np.arange(4, len(dc))  # quarters with four lags available
lags = [x[t - k] for x in (dy, dc) for k in (2, 3, 4)]
z = np.column_stack([np.ones(len(t))] + lags)


def ols(y, x):
    return np.linalg.lstsq(x, y, rcond=None)[0]


fitted = z @ ols(dy[t], z)  # first stage: predictable income growth
r2 = 1 - np.var(dy[t] - fitted) / np.var(dy[t])
f_stat = (r2 / 6) / ((1 - r2) / (len(t) - 7))
x_hat = np.column_stack([np.ones(len(t)), fitted])
b = ols(dc[t], x_hat)
resid = dc[t] - np.column_stack([np.ones(len(t)), dy[t]]) @ b
se = np.sqrt(resid @ resid / (len(t) - 2) * np.linalg.inv(x_hat.T @ x_hat)[1, 1])
b_ols = ols(dc[t], np.column_stack([np.ones(len(t)), dy[t]]))
print(f"quarters used {len(t)}; first-stage R2 {r2:.3f}, F {f_stat:.2f}")
print(f"OLS slope {b_ols[1]:.3f}")
print(f"lambda (instrumented) {b[1]:.3f}, standard error {se:.3f}")

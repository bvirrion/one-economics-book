"""Four-quarter inflation forecasts, 1986-2009: a regression against a random walk."""

import numpy as np
from econdata import sm_dataset

d = sm_dataset("macrodata")
t = (d.year + (d.quarter - 1) / 4).to_numpy()
p = np.log(d.cpi.to_numpy())
pi4 = np.full(len(d), np.nan)
pi4[4:] = 100 * (p[4:] - p[:-4])  # inflation over the past four quarters

err_ar, err_rw = [], []
for i in range(len(d) - 4):
    if t[i] < 1985:
        continue
    j = np.arange(8, i - 3)  # past pairs (j -> j + 4) known at quarter i
    A = np.column_stack([np.ones(len(j)), pi4[j], pi4[j - 4]])
    b = np.linalg.lstsq(A, pi4[j + 4], rcond=None)[0]  # refitted every quarter
    forecast = b @ [1, pi4[i], pi4[i - 4]]
    err_ar.append(pi4[i + 4] - forecast)
    err_rw.append(pi4[i + 4] - pi4[i])  # random walk: no change

for name, e in (("regression", err_ar), ("random walk", err_rw)):
    e = np.array(e)
    print(f"{name:12s} RMSE {np.sqrt(np.mean(e**2)):.3f}, mean error {e.mean():.3f}")
print(f"forecasts: {len(err_ar)}")

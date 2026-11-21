"""Two estimators of mean earnings from samples of 10: bias, variance, MSE."""

import numpy as np
from econdata import nsw

y = nsw("psid_controls").re78.to_numpy()
mu = y.mean()
rng = np.random.default_rng(2026)
samples = rng.choice(y, size=(20_000, 10))
estimators = {
    "sample mean": samples.mean(axis=1),
    "0.8 x mean": 0.8 * samples.mean(axis=1),
}
print(f"population mean {mu:,.0f}")
for name, est in estimators.items():
    bias, var = est.mean() - mu, est.var()
    print(
        f"{name:12s} bias {bias:7,.0f}  sd {np.sqrt(var):6,.0f}"
        f"  root MSE {np.sqrt(bias**2 + var):6,.0f}"
    )

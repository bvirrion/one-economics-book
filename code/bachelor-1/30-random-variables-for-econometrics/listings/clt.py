"""Sample means of earnings for n = 5, 30, 200: spread and shape."""

import numpy as np
from econdata import nsw
from scipy.stats import skew

y = nsw("psid_controls").re78.to_numpy()
sigma = y.std()  # the population is the sample of 2,490: divide by N
rng = np.random.default_rng(2026)
print(f"population: mean {y.mean():,.0f}  sd {sigma:,.0f}  skewness {skew(y):.2f}")
for n in (5, 30, 200):
    means = rng.choice(y, size=(10_000, n)).mean(axis=1)
    se = sigma / np.sqrt(n)
    print(
        f"n = {n:3d}: sd of means {means.std():6,.0f}  sigma/sqrt(n) {se:6,.0f}", end=""
    )
    print(f"  skewness {skew(means):.2f}")

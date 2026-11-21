"""Dividing by n or by n - 1: the average of the sample variance, n = 5."""

import numpy as np
from econdata import nsw

y = nsw("psid_controls").re78.to_numpy()
rng = np.random.default_rng(2026)
samples = rng.choice(y, size=(200_000, 5))
print(f"population variance       {y.var() / 1e6:7.1f} million")
for ddof in (0, 1):
    v = samples.var(axis=1, ddof=ddof).mean()
    print(f"average, divided by n - {ddof} {v / 1e6:7.1f} million")

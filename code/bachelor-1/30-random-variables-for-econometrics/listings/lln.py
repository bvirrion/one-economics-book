"""The law of large numbers: a running mean of earnings drawn at random."""

import numpy as np
from econdata import nsw

y = nsw("psid_controls").re78.to_numpy()
rng = np.random.default_rng(2026)
draws = rng.choice(y, size=100_000)  # with replacement
running = draws.cumsum() / np.arange(1, len(draws) + 1)
for n in (10, 100, 1_000, 10_000, 100_000):
    print(f"n = {n:>7,}: mean {running[n - 1]:9,.0f}")
print(f"population mean {y.mean():9,.0f}")

"""Earnings in 1978 of 2,490 American men (PSID sample): a histogram and quantiles."""

import numpy as np
from econdata import nsw

earn = nsw("psid_controls").re78  # dollars of 1982
counts, edges = np.histogram(earn, bins=np.arange(0, 130_001, 10_000))
width = edges[1] - edges[0]
density = counts / (len(earn) * width)  # the bars' areas sum to 1
for lo, n, d in zip(edges[:-1], counts, density):
    print(f"{lo:>7,.0f} to {lo + width:>7,.0f}: {n:5d}  density {d:.2e}")

q = earn.quantile([0.1, 0.25, 0.5, 0.75, 0.9]).round(0)
print(q.to_string())
print(
    f"mean {earn.mean():,.0f}; share below the mean {(earn < earn.mean()).mean():.3f}"
)

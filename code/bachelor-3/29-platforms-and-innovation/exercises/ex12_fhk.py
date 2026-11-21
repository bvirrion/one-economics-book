"""Exercise 12: a Foster-Haltiwanger-Krizan decomposition on an invented two-year
panel. Year 0 is Brenland's manufacturing firms in the 2025 census. In year 2 the
fifth of firms with the lowest output per worker exit; continuing firms keep their
output per worker but those above the median hire 20 % more workers; 15 entrants each
have 10 workers and the year-0 employment-weighted mean output per worker."""
import numpy as np
from country import load

f = load("firms")
m = f[f.sector == "manufacturing"]
w0 = m.workers.to_numpy(float)
p0 = m.output.to_numpy(float) / w0
stay = p0 >= np.quantile(p0, 0.2)
P0 = (w0 * p0).sum() / w0.sum()
w1c = np.where(p0 > np.median(p0), 1.2 * w0, w0)[stay]
w_all1 = w1c.sum() + 15 * 10
s0, s1 = w0 / w0.sum(), w1c / w_all1
within = 0.0
between = ((s1 - s0[stay]) * (p0[stay] - P0)).sum()
entry = 15 * 10 / w_all1 * (P0 - P0)
exit_ = -(s0[~stay] * (p0[~stay] - P0)).sum()
P1 = (w1c * p0[stay]).sum() / w_all1 + 15 * 10 / w_all1 * P0
print(f"P0 {P0:.2f}, P1 {P1:.2f}, change {P1 - P0:.2f} (thousand dalens per worker)")
print(f"within {within:.2f}, between {between:.2f}, entry {entry:.2f}, "
      f"exit {exit_:.2f}")

"""Exercise 11: how often does the 95 % interval of a local linear fit cover the true
jump (0.077)? 500 samples of the chapter's simulated elections."""
import numpy as np
from rdtools import local_linear

from elections import draw

windows = (0.02, 0.10, 0.25, 0.50)
hits = {h: [] for h in windows}
for s in range(500):
    m, y, _ = draw(seed=1000 + s)
    for h in windows:
        r = local_linear(m, y, 0, h)
        hits[h].append(abs(r["jump"] - 0.077) < 1.96 * r["se"])
for h in windows:
    print(f"window {h:4.2f}  coverage {np.mean(hits[h]):.3f}")

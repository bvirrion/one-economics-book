"""Bias and noise against the window: 500 simulated samples, true jump 0.077,
local constant (difference of means) against local linear."""
import numpy as np
from elections import draw
from rdtools import local_linear

windows = (0.02, 0.05, 0.10, 0.25, 0.50)
est = {(d, h): [] for d in (0, 1) for h in windows}
for s in range(500):
    margin, share, _ = draw(seed=s)
    for d in (0, 1):
        for h in windows:
            est[d, h].append(local_linear(margin, share, 0, h, degree=d)["jump"])

print("fit       window    bias   s.d.   root mean squared error")
for d, name in ((0, "constant"), (1, "linear")):
    for h in windows:
        e = np.array(est[d, h]) - 0.077
        rmse = np.sqrt(np.mean(e**2))
        bias = round(e.mean(), 3) + 0.0          # + 0.0 prints -0.000 as 0.000
        print(f"{name:9s} {h:5.2f}   {bias:6.3f} {e.std():6.3f}   {rmse:6.3f}")

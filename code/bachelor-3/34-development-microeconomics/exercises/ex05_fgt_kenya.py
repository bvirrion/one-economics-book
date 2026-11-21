"""Exercise 5: the FGT poverty measures for Kenya, 2022, from the World Bank PIP
percentile groups (national consumption, each group at its mean, 2021 PPP), at
three lines: 3.00, 4.20 and 8.30 dollars a day."""
import numpy as np
from econdata import pip_percentiles

p = pip_percentiles(["KEN"], [2022])
p = p[p.reporting_level == "national"]
y, w = p.avg_welfare.to_numpy(), p.pop_share.to_numpy()
for z in (3.00, 4.20, 8.30):
    g = np.where(y < z, (z - y) / z, 0.0)
    p0, p1, p2 = ((w * (y < z) * g ** a).sum() / w.sum() for a in (0, 1, 2))
    print(f"line {z:.2f}: headcount {100 * p0:4.1f} %, gap {100 * p1:4.1f} %, "
          f"squared gap {100 * p2:4.1f} %")

"""Mean, standard deviation and skewness of earnings and of their logarithm."""

import numpy as np
from econdata import nsw
from scipy.stats import skew

earn = nsw("psid_controls").re78
pos = earn[earn > 0]  # the logarithm needs positive earnings
print("zero earnings:", (earn == 0).sum())
for name, x in [("earnings", pos), ("log earnings", np.log(pos))]:
    print(
        f"{name:13s} mean {x.mean():10.3f}  sd {x.std():10.3f}  skewness {skew(x):6.3f}"
    )

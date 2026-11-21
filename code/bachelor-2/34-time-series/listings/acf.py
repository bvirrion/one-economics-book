"""Sample autocorrelations of US inflation and unemployment, 1959-2009."""

import numpy as np
from econdata import sm_dataset
from statsmodels.tsa.stattools import acf

d = sm_dataset("macrodata")
for name in ("infl", "unemp"):
    x = d[name].to_numpy()
    r = acf(x, nlags=4)
    xd = x - x.mean()
    r1 = (xd[1:] @ xd[:-1]) / (xd @ xd)  # lag 1 by hand
    print(f"{name:6s} lags 1-4: {np.round(r[1:], 3)}   lag 1 by hand {r1:.3f}")
print(f"band for white noise: +/- {1.96 / np.sqrt(len(d)):.3f}")

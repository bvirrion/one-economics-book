"""Dickey-Fuller tests: log real GDP (with a trend) and its growth rate."""

import numpy as np
from econdata import sm_dataset
from statsmodels.tsa.stattools import adfuller

d = sm_dataset("macrodata")
lgdp = np.log(d.realgdp.to_numpy())
growth = 400 * np.diff(lgdp)  # annualised, per cent

for name, x, trend in (("log real GDP", lgdp, "ct"), ("GDP growth", growth, "c")):
    stat, p, lags, nobs, crit, _ = adfuller(
        x, regression=trend, autolag="AIC", result_object=False
    )
    print(f"{name:13s} ADF {stat:6.2f}, 5 % critical value {crit['5%']:.2f},"
          f" p-value {p:.3f}, lags {lags}")  # fmt: skip

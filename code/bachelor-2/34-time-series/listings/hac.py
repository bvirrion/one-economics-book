"""Overlapping four-quarter changes: classical and Newey-West standard errors."""

import numpy as np
import statsmodels.api as sm
from econdata import sm_dataset

d = sm_dataset("macrodata")
p = np.log(d.cpi.to_numpy())
pi4 = 100 * (p[4:] - p[:-4])  # four-quarter inflation from 1960Q1
u = d.unemp.to_numpy()[4:]
change = pi4[4:] - pi4[:-4]  # change in inflation over the next four quarters
X = sm.add_constant(u[:-4])  # unemployment at the start

classical = sm.OLS(change, X).fit()
hac = sm.OLS(change, X).fit(cov_type="HAC", cov_kwds={"maxlags": 4})
res = classical.resid
r1 = (res[1:] @ res[:-1]) / (res @ res)
print(f"slope on unemployment {classical.params[1]:.3f}")
print(f"classical s.e. {classical.bse[1]:.3f}, Newey-West s.e. {hac.bse[1]:.3f}")
print(f"first autocorrelation of the residuals {r1:.3f}")

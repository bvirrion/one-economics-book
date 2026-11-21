"""AR(1) and AR(2) for US unemployment: least squares by hand, and AutoReg."""

import numpy as np
import statsmodels.api as sm
from econdata import sm_dataset
from statsmodels.tsa.ar_model import AutoReg

u = sm_dataset("macrodata").unemp.to_numpy()

ols1 = sm.OLS(u[1:], sm.add_constant(u[:-1])).fit()
ar1 = AutoReg(u, lags=1).fit()
print(f"AR(1) by OLS:     c {ols1.params[0]:.4f}, phi {ols1.params[1]:.4f}")
print(f"AR(1) by AutoReg: c {ar1.params[0]:.4f}, phi {ar1.params[1]:.4f}")
c, phi = ols1.params
half_life = np.log(0.5) / np.log(phi)
print(f"implied mean {c / (1 - phi):.2f}; half-life {half_life:.1f} quarters")

X2 = sm.add_constant(np.column_stack([u[1:-1], u[:-2]]))
ols2 = sm.OLS(u[2:], X2).fit()
ar2 = AutoReg(u, lags=2).fit()
print(f"AR(2) by OLS:     {np.round(ols2.params, 4)}")
print(f"AR(2) by AutoReg: {np.round(ar2.params, 4)}")
print(f"t of the second lag {ols2.tvalues[2]:.2f}")

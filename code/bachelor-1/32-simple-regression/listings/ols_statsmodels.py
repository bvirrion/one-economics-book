"""The same regression with statsmodels."""

import numpy as np  # noqa: F401 -- np.log is used inside the formula strings
import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("psid_controls").query("re78 > 0")
fit = smf.ols("np.log(re78) ~ education", data=d).fit()
print(fit.summary().tables[1])
print(f"R-squared {fit.rsquared:.4f}; observations {int(fit.nobs)}")

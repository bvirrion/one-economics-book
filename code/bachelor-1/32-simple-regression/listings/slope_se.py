"""The standard error of the slope by the formula, and a t test of the slope."""

import numpy as np
import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("psid_controls").query("re78 > 0")
fit = smf.ols("np.log(re78) ~ education", data=d).fit()
x, n = d.education, len(d)
s2 = (fit.resid**2).sum() / (n - 2)  # the error variance, n - 2 degrees of freedom
se = np.sqrt(s2 / ((x - x.mean()) ** 2).sum())
print(f"formula {se:.6f}; statsmodels {fit.bse['education']:.6f}")
print(f"t for slope = 0: {fit.params['education'] / se:.1f}")
print(f"t for slope = 0.10: {(fit.params['education'] - 0.10) / se:.2f}")

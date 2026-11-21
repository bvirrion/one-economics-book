"""R-squared three ways."""

import numpy as np
import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("psid_controls").query("re78 > 0")
y = np.log(d.re78)
fit = smf.ols("np.log(re78) ~ education", data=d).fit()
tss = ((y - y.mean()) ** 2).sum()
print(f"squared correlation      {np.corrcoef(d.education, y)[0, 1] ** 2:.6f}")
print(
    f"explained / total        {((fit.fittedvalues - y.mean()) ** 2).sum() / tss:.6f}"
)
print(f"1 - residual / total     {1 - (fit.resid**2).sum() / tss:.6f}")

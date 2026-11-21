"""Exercise 11: earnings-age profiles by schooling group, CPS comparison sample.

For each group, log 1978 earnings (positive only) on age and age squared; the age at
which the fitted profile peaks.
"""
import numpy as np
import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("cps_controls")
d = d[d.re78 > 0].copy()
d["lw"] = np.log(d.re78)
groups = {"fewer than 12 years": d.education < 12, "12 years": d.education == 12,
          "13-15 years": d.education.between(13, 15), "16 or more": d.education >= 16}
for name, m in groups.items():
    r = smf.ols("lw ~ age + I(age**2)", d[m]).fit()
    peak = -r.params["age"] / (2 * r.params["I(age ** 2)"])
    print(f"{name}: {m.sum()} men, peak at age {peak:.1f}")

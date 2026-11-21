"""Four functional forms on one pair of variables, and how to read each slope."""

import numpy as np  # noqa: F401 -- np.log is used inside the formula strings
import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("psid_controls").query("re78 > 0 and education > 0")
forms = {
    "re78 ~ education": "dollars per year of schooling",
    "np.log(re78) ~ education": "x 100: per cent per year of schooling",
    "re78 ~ np.log(education)": "/ 100: dollars per 1% more schooling",
    "np.log(re78) ~ np.log(education)": "elasticity: % per 1% more schooling",
}
for formula, reading in forms.items():
    slope = smf.ols(formula, data=d).fit().params.iloc[1]
    print(f"{formula:34s} {slope:10.4f}  {reading}")

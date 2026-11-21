"""The same regression on the top-coded CPS sample."""

import numpy as np  # noqa: F401 -- np.log is used inside the formula strings
import statsmodels.formula.api as smf
from econdata import nsw

for name in ("psid_controls", "cps_controls"):
    d = nsw(name).query("re78 > 0")
    b = smf.ols("np.log(re78) ~ education", data=d).fit().params["education"]
    at_cap = (d.re78 == d.re78.max()).mean()
    print(f"{name:14s} n {len(d):6d}  slope {b:.4f}  share at the maximum {at_cap:.3f}")

# The cap alone, in one sample: cap the PSID men at the CPS maximum.
cap = nsw("cps_controls").re78.max()
p = (
    nsw("psid_controls")
    .query("re78 > 0")
    .assign(capped=lambda x: x.re78.clip(upper=cap))
)
b = smf.ols("np.log(capped) ~ education", data=p).fit().params["education"]
share = (p.re78 > cap).mean()
print(f"PSID capped at {cap:,.2f}: slope {b:.4f}, share capped {share:.3f}")

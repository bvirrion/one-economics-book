"""Exercise 5: a Mincer regression on the CPS comparison sample of the NSW data.

Log 1978 earnings (positive earnings only) on schooling, experience and its square,
then with indicators for black, Hispanic and married; robust standard errors.
"""
import numpy as np
import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("cps_controls")
d = d[d.re78 > 0].copy()
d["lw"] = np.log(d.re78)
d["exp"] = (d.age - d.education - 6).clip(lower=0)
for f in ("lw ~ education + exp + I(exp**2)",
          "lw ~ education + exp + I(exp**2) + black + hispanic + married"):
    r = smf.ols(f, d).fit(cov_type="HC1")
    b, se = r.params["education"], r.bse["education"]
    print(f"{len(d)} men: schooling {b:.4f} (s.e. {se:.4f}), "
          f"premium {100 * (np.exp(b) - 1):.1f} % a year")

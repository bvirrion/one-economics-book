"""Maximum likelihood by hand: Newton--Raphson for the logit of the previous listing,
printing the log-likelihood at each step, then checking against statsmodels."""
import numpy as np
import statsmodels.formula.api as smf
from choicetools import logit_newton
from econdata import nsw

d = nsw("cps_controls")
d["work"] = (d.re78 > 0).astype(float)
d["earn75"] = d.re75 / 1000
X = np.column_stack([np.ones(len(d)), d[["earn75", "age", "education", "married"]]])

r = logit_newton(d.work.values, X)
for it, ll, b in r["history"]:
    print(f"step {it}: log-likelihood {ll:12.4f}   coefficient on earn75 {b[1]:.6f}")

check = smf.logit("work ~ earn75 + age + education + married", d).fit(disp=0)
print(f"statsmodels:       {check.llf:12.4f}   coefficient on earn75"
      f" {check.params['earn75']:.6f}")
print(f"standard error on earn75: by hand {r['se'][1]:.6f},"
      f" statsmodels {check.bse['earn75']:.6f}")

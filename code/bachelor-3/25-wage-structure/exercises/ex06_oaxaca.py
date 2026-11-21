"""Exercise 6: the Oaxaca-Blinder decomposition and the index-number problem.

Gap in log 1978 earnings between white and black men, CPS comparison sample of the
NSW data (positive earnings, Hispanic men excluded), with the explained part split
by characteristic, using first white and then black coefficients.
"""
import numpy as np
import statsmodels.formula.api as smf
from econdata import nsw

d = nsw("cps_controls")
d = d[(d.re78 > 0) & (d.hispanic == 0)].copy()
d["lw"] = np.log(d.re78)
d["age2"] = d.age**2
f = "lw ~ education + age + age2 + married"
w, b = d[d.black == 0], d[d.black == 1]
fits = {"white": smf.ols(f, w).fit(), "black": smf.ols(f, b).fit()}
gap = w.lw.mean() - b.lw.mean()
print(f"gap in mean log earnings: {gap:.3f}")
for ref, r in fits.items():
    parts = {v: r.params[v] * (w[v].mean() - b[v].mean())
             for v in ("education", "age", "age2", "married")}
    explained = sum(parts.values())
    detail = ", ".join(f"{k} {v:.3f}" for k, v in parts.items())
    print(f"{ref} coefficients: explained {explained:.3f} ({detail}), "
          f"unexplained {gap - explained:.3f}")

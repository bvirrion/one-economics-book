"""A local projection of U.S. output and prices on a policy-rate shock, 1960--2007.
The shock is the part of the Treasury-bill rate not explained by this quarter's
output growth and inflation and four lags of all three (a recursive ordering)."""
import numpy as np
import statsmodels.api as sm
from econdata import sm_dataset

d = sm_dataset("macrodata")
d = d.assign(y=100 * np.log(d.realgdp), p=100 * np.log(d.cpi), i=d.tbilrate)
d["dy"], d["dp"] = d.y.diff(), d.p.diff()
lags = {f"{v}{k}": d[v].shift(k) for v in ("dy", "dp", "i") for k in range(1, 5)}
for name, col in lags.items():
    d[name] = col
d = d[(d.year >= 1960) & (d.year <= 2007)].dropna()   # before the zero bound
L = list(lags)

first = sm.OLS(d.i, sm.add_constant(d[["dy", "dp"] + L])).fit()
d["shock"] = first.resid                               # surprise, in points
print(f"quarters {len(d)}; shock s.d. {d.shock.std():.2f} points")

for h in (0, 4, 8, 12, 16):
    resp = {}
    for v in ("y", "p"):
        lhs = (d[v].shift(-h) - d[v].shift(1)).rename("lhs")
        rhs = sm.add_constant(d[["shock", "dy", "dp"] + L])
        ok = lhs.notna()
        fit = sm.OLS(lhs[ok], rhs[ok]).fit(cov_type="HAC", cov_kwds={"maxlags": h + 1})
        resp[v] = (fit.params["shock"], fit.bse["shock"])
    print(f"h = {h:2d}: output {resp['y'][0]:+.2f} ({resp['y'][1]:.2f}), "
          f"prices {resp['p'][0]:+.2f} ({resp['p'][1]:.2f})")

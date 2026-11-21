"""Brenland's households: dummy variables and an interaction in a food regression."""

import numpy as np
import statsmodels.formula.api as smf
from country import load

h = load("households")
h["lfood"] = np.log(h.food)
h["linc"] = np.log(h.disposable)

plain = smf.ols("lfood ~ linc", h).fit()
sizes = smf.ols("lfood ~ linc + C(size) + owner", h).fit()
inter = smf.ols("lfood ~ linc * owner + C(size)", h).fit()

print(f"no controls:     elasticity {plain.params.linc:.3f}")
print(f"size dummies:    elasticity {sizes.params.linc:.3f}, R2 {sizes.rsquared:.3f}")
for k in range(2, 6):
    name = f"C(size)[T.{k}]"
    print(f"  size {k} against size 1: {sizes.params[name]:+.3f}")
print(f"  owner: {sizes.params.owner:+.3f} (s.e. {sizes.bse.owner:.3f})")
b, g = inter.params["linc"], inter.params["linc:owner"]
print(f"interaction: tenants {b:.3f}, owners {b + g:.3f}, difference {g:+.3f}"
      f" (s.e. {inter.bse['linc:owner']:.3f})")  # fmt: skip

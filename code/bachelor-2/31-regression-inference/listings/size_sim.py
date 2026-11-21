"""How often a nominal 5 % test rejects a true null, with unequal error variances."""

import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(31)
n, reps = 200, 4000
reject = {"classical": 0, "robust": 0}
for _ in range(reps):
    x = rng.standard_normal(n)
    u = np.abs(x) * rng.standard_normal(n)  # error spread grows with |x|
    y = 1 + 0 * x + u  # the true slope is zero
    model = sm.OLS(y, sm.add_constant(x))
    reject["classical"] += abs(model.fit().tvalues[1]) > 1.96
    reject["robust"] += abs(model.fit(cov_type="HC1").tvalues[1]) > 1.96

for name, count in reject.items():
    print(f"{name:9s} rejection rate {count / reps:.3f}")

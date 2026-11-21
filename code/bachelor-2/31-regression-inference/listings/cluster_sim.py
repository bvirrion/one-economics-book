"""Grouped data: classical, robust and cluster-robust standard errors."""

import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(31)
G, m, rho = 50, 20, 0.2  # groups, members per group, error correlation within group
group = np.repeat(np.arange(G), m)
slopes, se = [], {"classical": [], "robust": [], "cluster": []}
for _ in range(500):
    x = rng.standard_normal(G)[group]  # the regressor is the same within a group
    u = np.sqrt(rho) * rng.standard_normal(G)[group]
    u += np.sqrt(1 - rho) * rng.standard_normal(G * m)
    model = sm.OLS(1 + 0.5 * x + u, sm.add_constant(x))
    slopes.append(model.fit().params[1])
    se["classical"].append(model.fit().bse[1])
    se["robust"].append(model.fit(cov_type="HC1").bse[1])
    fit = model.fit(cov_type="cluster", cov_kwds={"groups": group})
    se["cluster"].append(fit.bse[1])

print(f"true s.d. of the slope across samples: {np.std(slopes):.4f}")
for name, values in se.items():
    print(f"mean {name:9s} standard error: {np.mean(values):.4f}")
print(f"Moulton factor sqrt(1 + (m - 1) rho): {np.sqrt(1 + (m - 1) * rho):.3f}")
ratio = np.mean(se["cluster"]) / np.mean(se["classical"])
print(f"cluster over classical: {ratio:.3f}")

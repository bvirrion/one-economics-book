"""Doctor visits in the RAND experiment: t statistics, and an F test by hand."""

import numpy as np
import statsmodels.api as sm
from scipy import stats
from econdata import sm_dataset

d = sm_dataset("randhie")
y = d.mdvis
X = sm.add_constant(d.drop(columns="mdvis"))
fit = sm.OLS(y, X).fit()
table = np.column_stack([fit.params, fit.bse, fit.tvalues])
for name, (b, se, t) in zip(X.columns, table):
    print(f"{name:8s} {b:8.4f} {se:7.4f} {t:7.2f}")

# H0: the three self-rated health dummies have zero coefficients
health = ["hlthg", "hlthf", "hlthp"]
restricted = sm.OLS(y, X.drop(columns=health)).fit()
n, k, q = len(y), X.shape[1], len(health)
ssr_u, ssr_r = fit.ssr, restricted.ssr
F = ((ssr_r - ssr_u) / q) / (ssr_u / (n - k))
print(f"SSR restricted {ssr_r:.1f}, unrestricted {ssr_u:.1f}")
F_sm = fit.f_test(" = ".join(health) + " = 0").fvalue
print(f"F by hand {F:.3f}; statsmodels {F_sm:.3f}")
print(f"5 % critical value F({q}, {n - k}): {stats.f.ppf(0.95, q, n - k):.3f}")

"""Heteroskedasticity-robust standard errors by hand, against statsmodels."""

import numpy as np
import statsmodels.api as sm
from econdata import sm_dataset

d = sm_dataset("randhie")
y = d.mdvis.to_numpy(float)
X = sm.add_constant(d.drop(columns="mdvis")).to_numpy(float)
n, k = X.shape

A = np.linalg.inv(X.T @ X)
b = A @ X.T @ y
e = y - X @ b
classical = A * (e @ e) / (n - k)
meat = (X * e[:, None] ** 2).T @ X  # sum of e_i^2 x_i x_i'
hc0 = A @ meat @ A  # the sandwich
hc1 = hc0 * n / (n - k)

sm_hc1 = sm.OLS(y, X).fit(cov_type="HC1").cov_params()
print("same HC1 as statsmodels:", np.allclose(hc1, sm_hc1))
names = ["const", "lncoins", "idp", "lpi", "fmde", "physlm", "disea", "hlthg", "hlthf"]
names.append("hlthp")
print("term      classical   HC0      HC1    ratio")
for j, name in enumerate(names):
    se = [np.sqrt(v[j, j]) for v in (classical, hc0, hc1)]
    print(f"{name:8s} {se[0]:8.4f} {se[1]:8.4f} {se[2]:8.4f} {se[2] / se[0]:6.2f}")

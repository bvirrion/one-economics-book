"""Exercise 12: OLS on logs against PPML when the error's variance depends on size.

y = exp(1 + x) * eta, E[eta | x] = 1, with Var(log eta) = 0.5 + x: the true
elasticity is 1. Repeated 200 times with 2,000 observations each.
"""
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(12)
ols, ppml = [], []
for _ in range(200):
    x = rng.uniform(0, 1, 2_000)
    s2 = 0.5 + x
    y = np.exp(1 + x) * np.exp(rng.normal(-s2 / 2, np.sqrt(s2)))  # mean one
    X = sm.add_constant(x)
    ols.append(sm.OLS(np.log(y), X).fit().params[1])
    ppml.append(sm.GLM(y, X, family=sm.families.Poisson()).fit().params[1])
print(f"true elasticity 1.000; mean OLS on logs {np.mean(ols):.3f}, "
      f"mean PPML {np.mean(ppml):.3f}")
print(f"spread (s.d.): OLS {np.std(ols):.3f}, PPML {np.std(ppml):.3f}")

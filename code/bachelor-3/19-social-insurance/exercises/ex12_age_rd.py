"""Exercise 12: a regression discontinuity at an age threshold (simulated).

20,000 job losers aged 40 to 60; potential duration 12 months below 50 and 18 from
50; non-employment duration 5 + 0.05 (age - 50) + 0.15 x entitlement beyond 12
months + noise. Local linear regressions on each side, bandwidth 5 years.
"""
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(19)
n = 20_000
age = rng.uniform(40, 60, n)
above = age >= 50
entitlement = np.where(above, 18, 12)
duration = 5 + 0.05 * (age - 50) + 0.15 * (entitlement - 12) + rng.normal(0, 3, n)

h = 5.0
sel = np.abs(age - 50) < h
x = age[sel] - 50
X = sm.add_constant(np.column_stack([above[sel], x, x * above[sel]]).astype(float))
fit = sm.OLS(duration[sel], X).fit(cov_type="HC1")
jump, se = fit.params[1], fit.bse[1]
print(f"observations within {h:.0f} years: {sel.sum()}")
print(f"jump at 50: {jump:.3f} months (s.e. {se:.3f})")
print(f"per month of entitlement: {jump / 6:.3f} (true 0.150)")

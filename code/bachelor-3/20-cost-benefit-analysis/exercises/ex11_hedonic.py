"""Exercise 11: a hedonic wage regression on simulated job data.

5,000 workers; log wage = a + 0.08 schooling + 0.03 experience + 0.02 risk + noise,
risk in deaths per 10,000 a year; mean wage about 30,000 dalens. Then an
unrecorded attribute (unpleasant work, worth 0.05 log points per unit) correlated
with risk is added and left out of the regression.
"""
import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(20)
n = 5_000
school = rng.normal(12, 2, n)
exper = rng.uniform(0, 30, n)
risk = rng.exponential(1.0, n)  # deaths per 10,000 a year
unpleasant = 0.8 * risk + rng.normal(0, 1, n)
base = 0.08 * school + 0.03 * exper + rng.normal(0, 0.3, n)
const = np.log(30_000) - base.mean() - 0.02 * risk.mean()


def vsl(premium, wage=30_000):
    """Log-point premium per 1 in 10,000 risk -> value of a statistical life."""
    return premium * wage * 10_000


for label, extra in (("no omitted attribute", 0.0), ("omitted attribute", 0.05)):
    logw = const + base + 0.02 * risk + extra * unpleasant
    X = sm.add_constant(np.column_stack([school, exper, risk]))
    fit = sm.OLS(logw, X).fit(cov_type="HC1")
    b, se = fit.params[3], fit.bse[3]
    print(f"{label}: premium {b:.4f} (s.e. {se:.4f}), "
          f"VSL {vsl(b) / 1e6:.2f} million")

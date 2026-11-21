"""An unobserved ability, a noisy test score as its proxy, and the schooling slope."""

import numpy as np
import statsmodels.api as sm

rng = np.random.default_rng(32)
n = 100_000
ability = rng.standard_normal(n)
school = 12 + 1.5 * ability + 2 * rng.standard_normal(n)
lwage = 1 + 0.08 * school + 0.10 * ability + 0.4 * rng.standard_normal(n)
score = ability + 0.7 * rng.standard_normal(n)  # the proxy


def coef(*cols):
    X = sm.add_constant(np.column_stack(cols))
    return sm.OLS(lwage, X).fit().params[1]


print("true return to schooling      0.080")
print(f"no control for ability        {coef(school):.3f}")
print(f"test score as a proxy         {coef(school, score):.3f}")
print(f"ability itself (unobservable) {coef(school, ability):.3f}")

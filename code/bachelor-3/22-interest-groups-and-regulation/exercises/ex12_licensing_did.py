"""Exercise 12: a difference-in-differences estimate on invented state reforms.

Forty invented states, 2012-2023; fifteen loosen the licence for a trade in 2018.
The log price of the service has state effects, year effects, noise and a true
reform effect of -0.06. The regression has state and year fixed effects, with
standard errors clustered by state.
"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

rng = np.random.default_rng(22)
states, years = np.arange(40), np.arange(2012, 2024)
reform = states < 15
state_fx = rng.normal(4.0, 0.15, len(states))
year_fx = 0.02 * (years - 2012) + rng.normal(0, 0.01, len(years))
rows = []
for s in states:
    for i, y in enumerate(years):
        treated = reform[s] and y >= 2018
        lp = state_fx[s] + year_fx[i] - 0.06 * treated + rng.normal(0, 0.04)
        rows.append((s, y, int(treated), int(reform[s]), lp))
d = pd.DataFrame(rows, columns=["state", "year", "treated", "reform", "lp"])

naive = (d[(d.reform == 1) & (d.year >= 2018)].lp.mean()
         - d[(d.reform == 1) & (d.year < 2018)].lp.mean())
r = smf.ols("lp ~ treated + C(state) + C(year)", d).fit(
    cov_type="cluster", cov_kwds={"groups": d.state})
print(f"before-after change in reforming states: {naive:.3f}")
print(f"difference-in-differences: {r.params['treated']:.3f} "
      f"(s.e. {r.bse['treated']:.3f})")

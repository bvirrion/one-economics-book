"""The Lucas critique: a Phillips curve estimated under one policy, used under another.

Unemployment follows u = 5 - 2 * (inflation - expected inflation) + noise. Inflation is
the policy target plus a policy surprise; people know the target and expect it.
"""

import numpy as np

rng = np.random.default_rng(25)


def regime(target, years=40):
    surprise = rng.normal(0, 1, years)
    inflation = target + surprise
    unemployment = 5 - 2 * (inflation - target) + rng.normal(0, 0.3, years)
    return inflation, unemployment


infl, unemp = regime(target=2)
slope, intercept = np.polyfit(infl, unemp, 1)
print(f"estimated under a 2% target: u = {intercept:.2f} {slope:+.2f} x inflation")
print(f"the estimate promises u = {intercept + slope * 4:.2f} at 4% inflation")

infl, unemp = regime(target=4)
print(
    f"with a 4% target: inflation {infl.mean():.2f}%, unemployment {unemp.mean():.2f}%"
)
slope, intercept = np.polyfit(infl, unemp, 1)
print(f"re-estimated: u = {intercept:.2f} {slope:+.2f} x inflation")

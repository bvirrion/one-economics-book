"""Ability bias: OLS overstates the return to schooling when ability is unseen."""
import numpy as np
from schooling_data import draw


def slope(x, y):
    return np.cov(x, y)[0, 1] / np.var(x, ddof=1)


d = draw(n=10_000, seed=1)
school, log_wage = d["school"], d["log_wage"]

print(f"true return to a year      {0.08:.4f}")
print(f"OLS slope                  {slope(school, log_wage):.4f}")
# the omitted-variable formula: beta + gamma * (slope of ability on school)
print(f"0.08 + 0.10 * slope(a, s)  {0.08 + 0.10 * slope(school, d['ability']):.4f}")

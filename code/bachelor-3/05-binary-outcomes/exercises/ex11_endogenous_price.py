"""Exercise 11: logit demand when prices respond to the quality the economist does
not see. OLS of the log-share difference on price is biased; a cost shifter is an
instrument."""
import numpy as np
from ivtools import ols, tsls

rng = np.random.default_rng(11)
T, J, alpha = 300, 4, -2.0
x = rng.uniform(0, 2, (T, J))
xi = rng.normal(0, 0.3, (T, J))
cost = rng.uniform(0, 0.5, (T, J))                  # shifts price, not demand
p = 1 + 0.3 * x + cost + 0.8 * xi                   # firms price their hidden quality
delta = 1 + 0.5 * x + alpha * p + xi
s = np.exp(delta) / (1 + np.exp(delta).sum(1, keepdims=True))
y = (np.log(s) - np.log(1 - s.sum(1))[:, None]).ravel()

const = np.ones(T * J)
X = np.column_stack([const, x.ravel(), p.ravel()])
Z = np.column_stack([const, x.ravel(), cost.ravel()])
print(f"true price coefficient {alpha}")
print(f"OLS   {ols(y, X)['beta'][2]:7.3f}")
r = tsls(y, X, Z)
print(f"2SLS  {r['beta'][2]:7.3f} (s.e. {r['se'][2]:.3f})")

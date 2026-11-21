"""The omitted-variable bias formula, short = long + gamma delta."""

import numpy as np
from econdata import nsw

d = nsw("cps_controls")
d = d[(d.re78 > 0) & (d.re75 > 0)]
y = np.log(d.re78).to_numpy()
z = np.log(d.re75).to_numpy()  # the variable left out of the short regression
W = np.column_stack([np.ones(len(d)), d.education, d.age, d.age**2, d.black,
                     d.hispanic, d.married])  # fmt: skip


def ols(target, M):
    return np.linalg.lstsq(M, target, rcond=None)[0]


short = ols(y, W)[1]
full = ols(y, np.column_stack([W, z]))
long, gamma = full[1], full[-1]
delta = ols(z, W)[1]

print(f"short regression (no 1975 earnings): {short:.6f}")
print(f"long regression:                     {long:.6f}")
print(f"gamma, effect of log 1975 earnings:  {gamma:.6f}")
print(f"delta, 1975 earnings on education:   {delta:.6f}")
print(f"long + gamma * delta:                {long + gamma * delta:.6f}")
print("equal to 1e-12:", abs(short - long - gamma * delta) < 1e-12)

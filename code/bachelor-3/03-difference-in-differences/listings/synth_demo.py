"""Synthetic control on a simulated region and twenty donors: weights, fit before
the policy, the estimated effect after it, and the placebo rank."""
import numpy as np
from synth import rmspe, synth_weights

rng = np.random.default_rng(12)
T, T0, J = 30, 20, 20                       # periods, pre-periods, donors
f = rng.normal(size=(T, 2)).cumsum(0)       # two common factors
load = rng.uniform(0, 1, size=(J + 1, 2))
Y = 10 + f @ load.T + rng.normal(0, 0.3, size=(T, J + 1))
Y[T0:, 0] -= 2.0                            # unit 0 is treated: effect -2

y1, Y0 = Y[:, 0], Y[:, 1:]
w = synth_weights(y1[:T0], Y0[:T0])
top = np.argsort(w)[::-1][:4]
print("largest weights:", ", ".join(f"donor {j + 1} {w[j]:.2f}" for j in top))
print(f"pre-period RMSPE     {rmspe(y1[:T0], Y0[:T0], w):.3f}")
print(f"mean gap after       {np.mean(y1[T0:] - Y0[T0:] @ w):.3f}")


def ratio(unit):
    others = [k for k in range(J + 1) if k != unit]
    wk = synth_weights(Y[:T0, unit], Y[:T0, others])
    return rmspe(Y[T0:, unit], Y[T0:, others], wk) / rmspe(
        Y[:T0, unit], Y[:T0, others], wk)


ratios = [ratio(k) for k in range(J + 1)]
rank = 1 + sum(r > ratios[0] for r in ratios[1:])
print(f"post/pre RMSPE ratio {ratios[0]:.1f}, rank {rank} of {J + 1}")

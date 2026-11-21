"""Exercise 11: which merger raises prices most? Four products with logit demand
(alpha = 1, cost 1), mean utilities 3.0, 2.8, 2.0 and 1.0. Simulate the merger of
products 1 and 2 and of products 1 and 4, and compare each with the upward pricing
pressure on product 1 at pre-merger prices."""
import numpy as np

ALPHA, COST = 1.0, np.ones(4)
DELTA = np.array([3.0, 2.8, 2.0, 1.0])


def shares(p):
    e = np.exp(DELTA - ALPHA * p)
    return e / (1 + e.sum())


def equilibrium(owner):
    p = COST + 1 / ALPHA
    for _ in range(10_000):
        s, new = shares(p), p.copy()
        for o in set(owner):
            idx = [j for j, k in enumerate(owner) if k == o]
            new[idx] = COST[idx] + 1 / (ALPHA * (1 - s[idx].sum()))
        if np.max(np.abs(new - p)) < 1e-12:
            return new
        p = 0.5 * p + 0.5 * new
    raise RuntimeError("no convergence")


p0 = equilibrium([0, 1, 2, 3])
s0 = shares(p0)
print("pre-merger prices:", np.round(p0, 3))
for j, owner in [(1, [0, 0, 2, 3]), (3, [0, 1, 2, 0])]:
    upp = s0[j] / (1 - s0[0]) * (p0[j] - COST[j])
    rise = equilibrium(owner)[0] - p0[0]
    print(f"merge 1 with {j + 1}: UPP on 1 = {upp:.3f}, price rise of 1 = {rise:.3f}")

"""Bertrand competition with logit demand. Product j has mean utility delta_j and
cost c_j; consumers get delta_j - alpha p_j plus a logit shock, or 0 from the outside
option. Owners set prices to maximise joint profit of the products they own."""
import numpy as np


def shares(p, delta, alpha):
    e = np.exp(delta - alpha * p)
    return e / (1 + e.sum())


def equilibrium(delta, cost, alpha, owner, tol=1e-12):
    """Prices from the first-order conditions: for each owner, the markup on its
    products is 1 / (alpha (1 - sum of its shares))."""
    p = cost + 1 / alpha
    for _ in range(10_000):
        s = shares(p, delta, alpha)
        new = p.copy()
        for o in set(owner):
            idx = [j for j, k in enumerate(owner) if k == o]
            new[idx] = cost[idx] + 1 / (alpha * (1 - s[idx].sum()))
        if np.max(np.abs(new - p)) < tol:
            return new
        p = 0.5 * p + 0.5 * new
    raise RuntimeError("no convergence")


def surplus(p, delta, alpha, market=1.0):
    return market * np.log(1 + np.exp(delta - alpha * p).sum()) / alpha


def upp(p, cost, s, i, j, efficiency=0.0):
    """Upward pricing pressure on product i from merging with j."""
    diversion = s[j] / (1 - s[i])
    return diversion * (p[j] - cost[j]) - efficiency * cost[i]

"""Independent private values, uniform on [0, 1], risk-neutral bidders."""
import numpy as np


def revenue_reserve(r, n):
    """Expected revenue of a second-price (or English) auction with reserve r:
    n times the integral from r to 1 of (2v - 1) v^(n-1) dv."""
    return (n - 1) / (n + 1) + r**n - 2 * n * r ** (n + 1) / (n + 1)


def optimal_reserve(v0=0.0):
    """Solves r - (1 - r) = v0 for uniform values."""
    return (1 + v0) / 2


def simulate_revenue(r, n, draws=200_000, seed=28):
    rng = np.random.default_rng(seed)
    v = np.sort(rng.uniform(size=(draws, n)), axis=1)
    top, second = v[:, -1], v[:, -2]
    pay = np.where(top < r, 0.0, np.maximum(second, r))
    return pay.mean()

"""An invented world of 20 countries for the weekend problem (no real data in it).

Structural gravity with symmetric trade costs (Anderson--van Wincoop): with income
shares theta and cost terms T_ij = t_ij^(1 - sigma) = dist^-delta exp(b U_ij - border), the
resistance terms A_i = P_i^(1 - sigma) solve A_j = sum_i theta_i T_ij / A_i, and
X_ij = Y_i Y_j / Y_w * T_ij / (A_i A_j). Domestic sales use an internal distance,
and every border crossing multiplies T by exp(-BORDER).
"""
import numpy as np
import pandas as pd

N, SEED = 20, 2003
DELTA, UNION = 1.0, 0.5  # true distance elasticity (minus) and union coefficient
INTERNAL = 0.4  # internal distance, thousands of km
BORDER = 1.5  # crossing a border divides T by exp(1.5)


def countries():
    """Names, positions (thousands of km), GDPs (billions of dalens) and members."""
    rng = np.random.default_rng(SEED)
    xy = rng.uniform(0, 10, size=(N, 2))
    xy[0], xy[1] = (4.0, 5.0), (4.9, 5.6)  # Brenland and Kestria, neighbours
    gdp = np.round(np.exp(rng.normal(5.0, 1.0, N)), 0)
    gdp[0], gdp[1] = 120.0, 300.0
    names = ["Brenland", "Kestria"] + [f"N{i:02d}" for i in range(1, N - 1)]
    d0 = np.hypot(*(xy - xy[0]).T)
    members = set(np.argsort(d0)[:5])  # Brenland and its four nearest neighbours
    return pd.DataFrame({"name": names, "x": xy[:, 0], "y": xy[:, 1], "gdp": gdp,
                         "member": [int(i in members) for i in range(N)]})


def distances(c):
    """Pair distances, with the internal distance on the diagonal."""
    xy = c[["x", "y"]].to_numpy()
    d = np.hypot(*(xy[:, None, :] - xy[None, :, :]).transpose(2, 0, 1))
    np.fill_diagonal(d, INTERNAL)
    return d


def flows(c, delta=DELTA, union=UNION, with_union=True):
    """Expected flows X_ij (billions of dalens) under structural gravity."""
    m = c.member.to_numpy()
    u = np.outer(m, m) * (1 - np.eye(N)) if with_union else np.zeros((N, N))
    T = distances(c) ** -delta * np.exp(union * u - BORDER * (1 - np.eye(N)))
    y = c.gdp.to_numpy()
    theta = y / y.sum()
    A = np.ones(N)
    for _ in range(2000):
        new = (theta / A) @ T
        A = np.sqrt(A * new)  # damped fixed-point step
    return np.outer(y, y) / y.sum() * T / np.outer(A, A)

"""Theory helpers. Rohlfs network demand: residents with taste theta uniform on
[0, 1] value the service at V theta n when a share n subscribes. Two-sided monopoly
platform with linear participation n_i = a_i + alpha_i n_j - p_i and cost f_i per
participant on each side."""
import numpy as np


def rohlfs_equilibria(p, value):
    """Interior shares n with value n (1 - n) = p, low root first."""
    disc = 1 - 4 * p / value
    if disc < 0:
        return []
    r = np.sqrt(disc)
    return [(1 - r) / 2, (1 + r) / 2]


def two_sided(a, alpha, f):
    s = alpha[0] + alpha[1]
    A = np.array([[2.0, -s], [-s, 2.0]])
    n = np.linalg.solve(A, np.array([a[0] - f[0], a[1] - f[1]]))
    p = np.array([a[0] + alpha[0] * n[1] - n[0], a[1] + alpha[1] * n[0] - n[1]])
    return n, p, float(((p - np.array(f)) * n).sum())


def fhk(p0, s0, p1, s1, status):
    """Foster-Haltiwanger-Krizan decomposition of the change in share-weighted
    productivity. status: 'c' continuing, 'x' exiting, 'n' entering."""
    status = np.asarray(status)
    P0, P1 = (s0 * p0)[status != "n"].sum(), (s1 * p1)[status != "x"].sum()
    c, n, x = status == "c", status == "n", status == "x"
    within = (s0[c] * (p1[c] - p0[c])).sum()
    between = ((s1[c] - s0[c]) * (p0[c] - P0)).sum()
    cross = ((s1[c] - s0[c]) * (p1[c] - p0[c])).sum()
    entry = (s1[n] * (p1[n] - P0)).sum()
    exit_ = -(s0[x] * (p0[x] - P0)).sum()
    return {"P0": P0, "P1": P1, "within": within, "between": between,
            "cross": cross, "entry": entry, "exit": exit_}

"""Helpers shared by this chapter's chart scripts: the simulated close elections of the
chapter's listings (code/bachelor-3/04-regression-discontinuity/listings/elections.py,
same formula and seeds) and a local linear fit with triangular weights (the code
library's rdtools.local_linear, inlined because chart scripts cannot import it)."""
import numpy as np


def draw(n=6000, seed=2024, jump=0.077):
    rng = np.random.default_rng(seed)
    margin = np.clip(rng.normal(0, 0.2, n), -0.5, 0.5)
    win = margin >= 0
    past = 0.47 + 0.40 * margin + 1.0 * margin**3 + rng.normal(0, 0.08, n)
    share = (0.46 + 0.45 * margin + 1.2 * margin**3 + jump * win
             + rng.normal(0, 0.08, n))
    return margin, share, past


def side_fit(x, y, h, degree=1):
    """Intercept and slope at 0 of a triangular-weighted fit of y on x, |x| < h."""
    w = np.clip(1 - np.abs(x) / h, 0, None)
    k = w > 0
    x, y, w = x[k], y[k], w[k]
    X = np.column_stack([np.ones_like(x)] + ([x] if degree == 1 else []))
    b = np.linalg.solve((X.T * w) @ X, (X.T * w) @ y)
    return b[0], (b[1] if degree == 1 else 0.0)


def jump(x, y, c, h, degree=1):
    x = np.asarray(x, float) - c
    r, left = x >= 0, x < 0
    return side_fit(x[r], y[r], h, degree)[0] - side_fit(x[left], y[left], h, degree)[0]

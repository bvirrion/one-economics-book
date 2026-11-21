"""Regression-discontinuity helpers for Book 5 (never printed).

    from rdtools import local_linear, density_test
    r = local_linear(x, y, cutoff=0, h=0.1)      # dict: jump, se, n, left, right
    r = local_linear(x, y, 0, 0.1, degree=0)     # local constant (difference of means)
    r = density_test(x, cutoff=70, h=10, bin=1)  # dict: theta (log jump), se, ...

local_linear fits, on each side of the cutoff and within h of it, a weighted
least-squares line (degree 1) or constant (degree 0) with triangular weights
1 - |x - c|/h (or uniform weights, kernel="uniform"); the jump is the difference of the
two fitted values at the cutoff, with a heteroskedasticity-robust standard error.
Units exactly at the cutoff count as treated (x >= c).

density_test is a McCrary-style test: bin the running variable, fit a local linear
regression of the bin heights on each side with triangular weights, and report the
log difference of the two estimated densities at the cutoff. Its standard error is
McCrary's (2008) approximation sqrt((24/5) (1/f_right + 1/f_left) / (n h)).
"""
from __future__ import annotations

import numpy as np


def _side(x, y, h, degree, kernel):
    w = np.clip(1 - np.abs(x) / h, 0, None) if kernel == "triangular" else (
        (np.abs(x) <= h).astype(float))
    keep = w > 0
    x, y, w = x[keep], y[keep], w[keep]
    X = np.column_stack([np.ones_like(x)] + ([x] if degree == 1 else []))
    XtW = X.T * w
    A = np.linalg.inv(XtW @ X)
    b = A @ (XtW @ y)
    e = y - X @ b
    n, k = X.shape
    V = A @ (X.T * (w**2 * e**2)) @ X @ A * n / (n - k)
    return b[0], V[0, 0], n


def local_linear(x, y, cutoff, h, degree=1, kernel="triangular"):
    x = np.asarray(x, float) - cutoff
    y = np.asarray(y, float)
    right, left = x >= 0, x < 0
    a1, v1, n1 = _side(x[right], y[right], h, degree, kernel)
    a0, v0, n0 = _side(x[left], y[left], h, degree, kernel)
    return {"jump": a1 - a0, "se": float(np.sqrt(v1 + v0)), "n": n1 + n0,
            "left": a0, "right": a1}


def density_test(x, cutoff, h, bin=1.0):
    x = np.asarray(x, float)
    n = len(x)
    lo = cutoff - bin * np.ceil((cutoff - x.min()) / bin)
    edges = np.arange(lo, x.max() + bin, bin)
    counts, edges = np.histogram(x, edges)
    mids = (edges[:-1] + edges[1:]) / 2 - cutoff
    f = counts / (n * bin)
    right, left = mids > 0, mids < 0
    fr, _, _ = _side(mids[right], f[right], h, 1, "triangular")
    fl, _, _ = _side(mids[left], f[left], h, 1, "triangular")
    theta = np.log(fr) - np.log(fl)
    se = np.sqrt(24 / 5 * (1 / fr + 1 / fl) / (n * h))
    return {"theta": float(theta), "se": float(se), "f_left": float(fl),
            "f_right": float(fr)}

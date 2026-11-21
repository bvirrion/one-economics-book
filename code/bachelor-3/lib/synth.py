"""Synthetic-control weights for Book 5 (never printed).

    from synth import synth_weights
    w = synth_weights(y1_pre, Y0_pre)   # y1_pre: (T0,), Y0_pre: (T0, J) donors

The weights minimise the squared distance between the treated unit's pre-period
path and the weighted donors' paths, subject to w >= 0 and sum(w) = 1 (a point of
the donors' convex hull). Solved by scipy's SLSQP from equal weights.
"""
from __future__ import annotations

import numpy as np
from scipy.optimize import minimize


def synth_weights(y1_pre, Y0_pre):
    y1, Y0 = np.asarray(y1_pre, float), np.asarray(Y0_pre, float)
    J = Y0.shape[1]

    def loss(w):
        r = y1 - Y0 @ w
        return r @ r

    def grad(w):
        return -2 * Y0.T @ (y1 - Y0 @ w)

    res = minimize(loss, np.full(J, 1 / J), jac=grad, method="SLSQP",
                   bounds=[(0, 1)] * J,
                   constraints=[{"type": "eq", "fun": lambda w: w.sum() - 1,
                                 "jac": lambda w: np.ones(J)}],
                   options={"ftol": 1e-12, "maxiter": 500})
    w = np.clip(res.x, 0, None)
    return w / w.sum()


def rmspe(y1, Y0, w):
    """Root mean squared prediction error of the synthetic path."""
    r = np.asarray(y1, float) - np.asarray(Y0, float) @ w
    return float(np.sqrt(np.mean(r**2)))

"""Small, tested estimators for Book 5 (University Year 3). Never printed in the book.

The chapters build each estimator by hand first (Part I); later chapters and the
exercise solutions call these helpers so that a listing stays short.

    from ivtools import ols, tsls, first_stage_f

All arrays are numpy; a design matrix includes its own constant column.
"""
from __future__ import annotations

import numpy as np


def _cov(XtX_inv, A, u, kind):
    """Variance matrix: 'classical' s^2 (A'A)^-1 or 'HC1' sandwich (A = regressors)."""
    n, k = A.shape
    if kind == "classical":
        return XtX_inv * (u @ u) / (n - k)
    if kind == "HC1":
        meat = (A * (u**2)[:, None]).T @ A
        return XtX_inv @ meat @ XtX_inv * n / (n - k)
    raise ValueError(kind)


def ols(y, X, se="classical"):
    """OLS of y on X. Returns dict(beta, se, resid)."""
    y, X = np.asarray(y, float), np.asarray(X, float)
    XtX_inv = np.linalg.inv(X.T @ X)
    beta = XtX_inv @ X.T @ y
    u = y - X @ beta
    V = _cov(XtX_inv, X, u, se)
    return {"beta": beta, "se": np.sqrt(np.diag(V)), "resid": u}


def first_stage_f(x, Z, W):
    """F statistic of the excluded instruments Z in the regression of x on [W, Z]
    (classical errors). W holds the included exogenous regressors, with the constant."""
    x, Z, W = (np.asarray(a, float) for a in (x, Z, W))
    Z = Z.reshape(len(x), -1)
    full = np.column_stack([W, Z])
    u_full = x - full @ np.linalg.lstsq(full, x, rcond=None)[0]
    u_short = x - W @ np.linalg.lstsq(W, x, rcond=None)[0]
    q, n, k = Z.shape[1], len(x), full.shape[1]
    return ((u_short @ u_short - u_full @ u_full) / q) / (u_full @ u_full / (n - k))


def tsls(y, X, Z, se="classical"):
    """Two-stage least squares. X: all regressors (exogenous and endogenous);
    Z: all instruments (the exogenous regressors again, plus the excluded instruments).
    Residuals use the actual X, never the fitted one. Returns dict(beta, se, resid)."""
    y, X, Z = (np.asarray(a, float) for a in (y, X, Z))
    Xhat = Z @ np.linalg.solve(Z.T @ Z, Z.T @ X)
    A_inv = np.linalg.inv(Xhat.T @ Xhat)
    beta = A_inv @ Xhat.T @ y
    u = y - X @ beta
    V = _cov(A_inv, Xhat, u, se)
    return {"beta": beta, "se": np.sqrt(np.diag(V)), "resid": u}

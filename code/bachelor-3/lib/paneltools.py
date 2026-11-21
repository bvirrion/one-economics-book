"""Panel helpers for Book 5 (never printed): within transforms and clustered errors.

    from paneltools import demean, twoway_demean, ols_cluster
"""
from __future__ import annotations

import numpy as np
import pandas as pd


def demean(df: pd.DataFrame, cols, by) -> pd.DataFrame:
    """Each column minus its mean within the groups `by` (the within transform)."""
    return df[cols] - df.groupby(by)[cols].transform("mean")


def twoway_demean(df: pd.DataFrame, cols, unit, time, iters=200, tol=1e-12):
    """Remove unit and time means (exact in one pass for a balanced panel; iterated
    alternating projections otherwise)."""
    out = df[cols].astype(float).copy()
    for _ in range(iters):
        before = out.copy()
        out = out - out.groupby(df[unit]).transform("mean")
        out = out - out.groupby(df[time]).transform("mean")
        if np.abs((out - before).to_numpy()).max() < tol:
            break
    return out


def ols_cluster(y, X, groups, df_adjust=True):
    """OLS with classical, HC1 and cluster-robust (CR1) standard errors.
    Returns dict(beta, se_iid, se_hc1, se_cluster)."""
    y, X = np.asarray(y, float), np.asarray(X, float)
    X = X.reshape(len(y), -1)
    g = pd.factorize(np.asarray(groups))[0]
    n, k = X.shape
    G = g.max() + 1
    A = np.linalg.inv(X.T @ X)
    beta = A @ X.T @ y
    u = y - X @ beta
    se_iid = np.sqrt(np.diag(A) * (u @ u) / (n - k))
    meat = (X * (u**2)[:, None]).T @ X
    se_hc1 = np.sqrt(np.diag(A @ meat @ A) * n / (n - k))
    sums = np.zeros((G, k))
    np.add.at(sums, g, X * u[:, None])
    c = (G / (G - 1)) * ((n - 1) / (n - k)) if df_adjust else 1.0
    se_cl = np.sqrt(np.diag(A @ (sums.T @ sums) @ A) * c)
    return {"beta": beta, "se_iid": se_iid, "se_hc1": se_hc1, "se_cluster": se_cl}

"""Logit models by Newton--Raphson, for Book 5 (never printed).

    from choicetools import logit_newton, clogit
    r = logit_newton(y, X)            # binary logit; X includes a constant column
    r["beta"], r["se"], r["loglik"], r["history"]   # history: (iteration, loglik, beta)
    r = clogit(chosen, X, groups)     # conditional (McFadden) logit: one row per
                                      # alternative, chosen = 1 for the chosen one
    r["beta"], r["se"], r["loglik"], r["prob"]

Both maximise the log-likelihood by Newton steps from beta = 0, stopping when the
largest step is below tol. Standard errors are the square roots of the diagonal of
the inverse of minus the Hessian at the maximum (the inverse information).
"""
from __future__ import annotations

import numpy as np


def logit_newton(y, X, tol=1e-10, max_iter=50):
    y, X = np.asarray(y, float), np.asarray(X, float)
    b = np.zeros(X.shape[1])
    history = []
    step = np.full_like(b, np.inf)
    for it in range(max_iter):
        xb = X @ b
        p = 1 / (1 + np.exp(-xb))
        ll = float(np.sum(y * xb - np.logaddexp(0, xb)))
        history.append((it, ll, b.copy()))
        H = -(X.T * (p * (1 - p))) @ X
        if np.max(np.abs(step)) < tol:
            break
        step = np.linalg.solve(H, -(X.T @ (y - p)))
        b = b + step
    return {"beta": b, "se": np.sqrt(np.diag(np.linalg.inv(-H))), "loglik": ll,
            "history": history, "prob": p}


def _clogit_parts(b, chosen, X, idx):
    v = X @ b
    v = v - np.maximum.reduceat(v, idx)[np.repeat(np.arange(len(idx)), np.diff(
        np.append(idx, len(v))))]
    e = np.exp(v)
    denom = np.add.reduceat(e, idx)
    sizes = np.diff(np.append(idx, len(v)))
    p = e / np.repeat(denom, sizes)
    return v, p, sizes


def clogit(chosen, X, groups, tol=1e-10, max_iter=100):
    chosen, X = np.asarray(chosen, float), np.asarray(X, float)
    groups = np.asarray(groups)
    order = np.argsort(groups, kind="stable")
    chosen, X, groups = chosen[order], X[order], groups[order]
    idx = np.flatnonzero(np.r_[True, groups[1:] != groups[:-1]])
    b = np.zeros(X.shape[1])
    for _ in range(max_iter):
        v, p, sizes = _clogit_parts(b, chosen, X, idx)
        xbar = np.add.reduceat(X * p[:, None], idx)          # per group
        dev = X - np.repeat(xbar, sizes, axis=0)
        grad = dev.T @ chosen
        H = -(dev.T * p) @ dev
        step = np.linalg.solve(H, -grad)
        b = b + step
        if np.max(np.abs(step)) < tol:
            break
    v, p, sizes = _clogit_parts(b, chosen, X, idx)
    xbar = np.add.reduceat(X * p[:, None], idx)
    dev = X - np.repeat(xbar, sizes, axis=0)
    H = -(dev.T * p) @ dev
    ll = float(np.sum(chosen * np.log(p)))
    prob = np.empty_like(p)
    prob[order] = p
    return {"beta": b, "se": np.sqrt(np.diag(np.linalg.inv(-H))), "loglik": ll,
            "prob": prob}

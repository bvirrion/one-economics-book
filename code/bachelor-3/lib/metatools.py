"""Tools for Book 5, chapter 6: power, the significance filter and meta-analysis.

    power(beta, s, c=1.96)          probability that beta_hat / s exceeds c
    filtered_mean(beta, s, c=1.96)  mean of beta_hat ~ N(beta, s^2) when beta_hat/s > c
    fixed_effect(est, se)           inverse-variance mean and its standard error
    dersimonian_laird(est, se)      random-effects mean, its s.e., tau^2 and Q
    fat_pet(est, se)                WLS of est on (1, se) with weights 1/se^2:
                                    (pet, pet_se, fat, fat_se)

The filter is one-sided (publish when the estimate is significantly positive); the
other tail has negligible probability when the true effect is positive.
"""
import numpy as np
from scipy.stats import norm


def power(beta, s, c=1.96):
    return norm.sf(c - beta / s)


def filtered_mean(beta, s, c=1.96):
    a = c - beta / s
    return beta + s * norm.pdf(a) / norm.sf(a)


def fixed_effect(est, se):
    est, w = np.asarray(est, float), 1 / np.asarray(se, float) ** 2
    return (w @ est) / w.sum(), 1 / np.sqrt(w.sum())


def dersimonian_laird(est, se):
    est, v = np.asarray(est, float), np.asarray(se, float) ** 2
    w = 1 / v
    mean_fe = (w @ est) / w.sum()
    q = w @ (est - mean_fe) ** 2
    tau2 = max(0.0, (q - (len(est) - 1)) / (w.sum() - (w @ w) / w.sum()))
    wr = 1 / (v + tau2)
    return (wr @ est) / wr.sum(), 1 / np.sqrt(wr.sum()), tau2, q


def fat_pet(est, se):
    est, se = np.asarray(est, float), np.asarray(se, float)
    X = np.column_stack([np.ones_like(se), se])
    w = 1 / se**2
    XtW = X.T * w
    b = np.linalg.solve(XtW @ X, XtW @ est)
    resid = est - X @ b
    sigma2 = (w @ resid**2) / (len(est) - 2)
    cov = sigma2 * np.linalg.inv(XtW @ X)
    return b[0], np.sqrt(cov[0, 0]), b[1], np.sqrt(cov[1, 1])

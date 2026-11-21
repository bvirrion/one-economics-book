"""Worked numbers for Book 4, chapter 34 (exercises and the weekend problem)."""

import numpy as np
import statsmodels.api as sm
from country import load
from econdata import sm_dataset
from statsmodels.tsa.stattools import acf, adfuller


def brenland_inflation():
    """Annual CPI inflation, per cent (log changes), 2001-2025."""
    a = load("accounts")
    pi = 100 * np.diff(np.log(a.cpi.to_numpy()))
    return a.year.to_numpy()[1:], pi


def brenland():
    years, pi = brenland_inflation()
    fit = sm.OLS(pi[1:], sm.add_constant(pi[:-1])).fit()
    c, phi = fit.params
    s = np.sqrt(fit.scale)
    mean = c / (1 - phi)
    f1 = c + phi * pi[-1]
    f2 = c + phi * f1
    se2 = s * np.sqrt(1 + phi**2)
    stat, p, *_ = adfuller(
        pi, regression="c", maxlag=0, autolag=None, result_object=False
    )
    return {"mean_pi": pi.mean(), "sd_pi": pi.std(ddof=1), "last": pi[-1],
            "acf1": acf(pi, nlags=1)[1], "c": c, "phi": phi, "se_phi": fit.bse[1],
            "s": s, "mean": mean, "half_life": np.log(0.5) / np.log(phi),
            "f1": f1, "f2": f2, "se1": s, "se2": se2,
            "lo2": f2 - 1.96 * se2, "hi2": f2 + 1.96 * se2,
            "df": stat, "df_p": p, "n": len(pi), "max_year": years[pi.argmax()],
            "max": pi.max()}  # fmt: skip


def ar1_acf(phi, k):
    return phi**k


def long_run_multiplier(betas):
    return sum(betas)


def unemp_ar1():
    u = sm_dataset("macrodata").unemp.to_numpy()
    fit = sm.OLS(u[1:], sm.add_constant(u[:-1])).fit()
    return fit.params, fit.bse


def phillips_forecast():
    """D exercise: the forecasting regression plus unemployment, rolling, 1986-2009."""
    d = sm_dataset("macrodata")
    t = (d.year + (d.quarter - 1) / 4).to_numpy()
    p = np.log(d.cpi.to_numpy())
    u = d.unemp.to_numpy()
    pi4 = np.full(len(d), np.nan)
    pi4[4:] = 100 * (p[4:] - p[:-4])
    err = {"ar": [], "ar+u": [], "rw": []}
    for i in range(len(d) - 4):
        if t[i] < 1985:
            continue
        j = np.arange(8, i - 3)
        for name, cols in (
            ("ar", [pi4[j], pi4[j - 4]]),
            ("ar+u", [pi4[j], pi4[j - 4], u[j]]),
        ):
            A = np.column_stack([np.ones(len(j))] + cols)
            b = np.linalg.lstsq(A, pi4[j + 4], rcond=None)[0]
            x = [1, pi4[i], pi4[i - 4]] + ([u[i]] if name == "ar+u" else [])
            err[name].append(pi4[i + 4] - b @ x)
        err["rw"].append(pi4[i + 4] - pi4[i])
    return {k: float(np.sqrt(np.mean(np.square(v)))) for k, v in err.items()}


def brenland_df_critical():
    _, pi = brenland_inflation()
    return adfuller(pi, regression="c", maxlag=0, autolag=None, result_object=False)[4]


def surge():
    """Part I.12: the 2022 residual and the AR(1)'s one-step forecasts for 2023-2024."""
    years, pi = brenland_inflation()
    r = brenland()
    k = list(years).index(2022)
    resid = pi[k] - r["c"] - r["phi"] * pi[k - 1]
    f23 = r["c"] + r["phi"] * pi[k]
    f24 = r["c"] + r["phi"] * pi[k + 1]
    return {"resid": resid, "z": resid / r["s"], "f23": f23, "a23": pi[k + 1],
            "f24": f24, "a24": pi[k + 2]}  # fmt: skip


def unemp_mean_se():
    """Exercise 6: delta-method standard error of the implied mean c / (1 - phi)."""
    u = sm_dataset("macrodata").unemp.to_numpy()
    fit = sm.OLS(u[1:], sm.add_constant(u[:-1])).fit()
    c, phi = fit.params
    g = np.array([1 / (1 - phi), c / (1 - phi) ** 2])
    return float(np.sqrt(g @ fit.cov_params() @ g))

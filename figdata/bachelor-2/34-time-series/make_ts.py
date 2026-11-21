"""Time series, chapter 34.

Opening chart (illustrative): two independent Gaussian random walks of 200 steps
(seed 36, chosen to show a pair that looks related; the listing random_walks.py
measures how often that happens), and the R2 and t statistic of the regression of one
on the other.
ACF chart: sample autocorrelations, lags 1-12, of US quarterly inflation (infl,
annualised) and the unemployment rate, statsmodels macrodata 1959Q1-2009Q3.
Forecast chart: four-quarter inflation pi4 = 100 ln(cpi_t / cpi_{t-4}); at each
quarter t from 1985Q1, a direct forecast of pi4 four quarters ahead from a regression
of pi4_{s+4} on (1, pi4_s, pi4_{s-4}) fitted on data available at t, against the
random-walk forecast pi4_t.
Writes
  out/walks.csv     step, a, b
  out/walks_fit.csv r2, t, slope
  out/acf.csv       lag, infl, unemp
  out/fcst.csv      t, actual, ar, rw   (t = year + (quarter - 1) / 4 of the target)
  out/rmse.csv      model, rmse, n
"""

import numpy as np
import pandas as pd
from econdata import sm_dataset
from figout import write_table
from statsmodels.tsa.stattools import acf


def walks(n=200, seed=36):
    rng = np.random.default_rng(seed)
    e = rng.standard_normal((n, 2))
    w = e.cumsum(axis=0)
    return pd.DataFrame(
        {"step": range(1, n + 1), "a": w[:, 0].round(3), "b": w[:, 1].round(3)}
    )


def walks_fit():
    w = walks()
    x, y = w.a.to_numpy(), w.b.to_numpy()
    X = np.column_stack([np.ones(len(x)), x])
    b, res = np.linalg.lstsq(X, y, rcond=None)[:2]
    s2 = res[0] / (len(x) - 2)
    se = np.sqrt(s2 * np.linalg.inv(X.T @ X)[1, 1])
    r2 = 1 - res[0] / ((y - y.mean()) @ (y - y.mean()))
    return pd.DataFrame(
        [{"r2": round(r2, 3), "t": round(b[1] / se, 2), "slope": round(b[1], 3)}]
    )


def acf_table(nlags=12):
    d = sm_dataset("macrodata")
    return pd.DataFrame({"lag": range(1, nlags + 1),
                         "infl": acf(d.infl, nlags=nlags)[1:].round(3),
                         "unemp": acf(d.unemp, nlags=nlags)[1:].round(3)})  # fmt: skip


def forecasts():
    d = sm_dataset("macrodata")
    t = (d.year + (d.quarter - 1) / 4).to_numpy()
    p = np.log(d.cpi.to_numpy())
    pi4 = np.full(len(d), np.nan)
    pi4[4:] = 100 * (p[4:] - p[:-4])
    rows = []
    for i in range(len(d) - 4):
        if t[i] < 1985:
            continue
        j = np.arange(8, i - 3)  # pairs (j -> j + 4) known at i
        A = np.column_stack([np.ones(len(j)), pi4[j], pi4[j - 4]])
        b = np.linalg.lstsq(A, pi4[j + 4], rcond=None)[0]
        ar = b @ [1, pi4[i], pi4[i - 4]]
        rows.append({"t": t[i + 4], "actual": pi4[i + 4], "ar": ar, "rw": pi4[i]})
    return pd.DataFrame(rows).round(3)


def rmse():
    f = forecasts()
    out = []
    for m in ("ar", "rw"):
        r = float(np.sqrt(((f.actual - f[m]) ** 2).mean()))
        out.append({"model": m, "rmse": round(r, 3), "n": len(f)})
    return pd.DataFrame(out)


if __name__ == "__main__":
    write_table(walks(), __file__, "walks")
    write_table(walks_fit(), __file__, "walks_fit")
    write_table(acf_table(), __file__, "acf")
    write_table(forecasts(), __file__, "fcst")
    write_table(rmse(), __file__, "rmse")

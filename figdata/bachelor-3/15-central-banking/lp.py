"""Local projections with a recursively identified policy shock (the method of the
chapter's listing). `prepare` builds the variables from macrodata; `shock` is the
first-stage residual; `irf` estimates the response at each horizon with HAC errors."""
import numpy as np
import pandas as pd
import statsmodels.api as sm

VARS = ("dy", "dp", "i")


def add_lags(d: pd.DataFrame, n=4) -> list[str]:
    names = []
    for v in VARS:
        for k in range(1, n + 1):
            d[f"{v}{k}"] = d[v].shift(k)
            names.append(f"{v}{k}")
    return names


def prepare(m: pd.DataFrame, since=1960, until=2007):
    d = m.assign(y=100 * np.log(m.realgdp), p=100 * np.log(m.cpi), i=m.tbilrate)
    d["dy"], d["dp"] = d.y.diff(), d.p.diff()
    lags = add_lags(d)
    d = d[(d.year >= since) & (d.year <= until)].dropna().reset_index(drop=True)
    return d, lags


def shock(d, lags):
    return sm.OLS(d.i, sm.add_constant(d[["dy", "dp"] + lags])).fit().resid


def irf(d, lags, outcome, H=16):
    rows = []
    for h in range(H + 1):
        lhs = d[outcome].shift(-h) - d[outcome].shift(1)
        rhs = sm.add_constant(d[["shock", "dy", "dp"] + lags])
        ok = lhs.notna()
        f = sm.OLS(lhs[ok], rhs[ok]).fit(cov_type="HAC", cov_kwds={"maxlags": h + 1})
        rows.append({"h": h, "b": f.params["shock"], "se": f.bse["shock"]})
    r = pd.DataFrame(rows)
    r["lo"], r["hi"] = r.b - 1.645 * r.se, r.b + 1.645 * r.se
    return r

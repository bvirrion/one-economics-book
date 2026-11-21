"""The weekend problem's invented panel: 300 Brenland firms, 2011-2025 (seeded).

Model (Brenland is invented; nothing here is real data):
  management quality m_i ~ N(0, 1), unseen by the economist;
  log capital k_it = 3 + 0.8 m_i + 0.03 (t - 2011) + e_it, e an AR(1) with persistence 0.7;
  a training subsidy from 2018 for the 100 firms with the highest m_i + noise;
  log output y_it = 1 + 0.5 m_i + 0.30 k_it + 0.10 s_it + g_t + u_it, u an AR(1) with
  persistence 0.6 and standard deviation 0.2; g_t a common shock per year.
Writes
  out/firms_results.csv  one row per estimate: model, coefficient, estimate, se_iid,
                         se_cluster (clustered by firm)
  out/firms_facts.csv    n_firms, years, rows, treated, var_k, cov_km, sd_y
Book 5, chapter 2, weekend problem.
"""
import numpy as np
import pandas as pd
from figout import write_table

FIRMS, YEARS = 300, np.arange(2011, 2026)


def ols_cluster(y, X, groups):
    """OLS with classical and firm-clustered (CR1) standard errors (as paneltools)."""
    y, X = np.asarray(y, float), np.asarray(X, float).reshape(len(y), -1)
    g = pd.factorize(np.asarray(groups))[0]
    n, k = X.shape
    G = g.max() + 1
    A = np.linalg.inv(X.T @ X)
    beta = A @ X.T @ y
    u = y - X @ beta
    sums = np.zeros((G, k))
    np.add.at(sums, g, X * u[:, None])
    c = (G / (G - 1)) * ((n - 1) / (n - k))
    return {"beta": beta, "se_iid": np.sqrt(np.diag(A) * (u @ u) / (n - k)),
            "se_cluster": np.sqrt(np.diag(A @ (sums.T @ sums) @ A) * c)}


def ar1(rng, n, t, rho, sd):
    e = np.zeros((n, t))
    e[:, 0] = rng.normal(0, sd, n)
    for s in range(1, t):
        e[:, s] = rho * e[:, s - 1] + np.sqrt(1 - rho**2) * rng.normal(0, sd, n)
    return e


def panel():
    rng = np.random.default_rng(2025)
    T = len(YEARS)
    m = rng.normal(size=FIRMS)
    k = 3 + 0.8 * m[:, None] + 0.03 * (YEARS - 2011) + ar1(rng, FIRMS, T, 0.7, 0.3)
    score = m + rng.normal(0, 0.5, FIRMS)
    treated = score >= np.sort(score)[-100]
    s = treated[:, None] & (YEARS >= 2018)
    g = rng.normal(0, 0.05, T)
    y = 1 + 0.5 * m[:, None] + 0.30 * k + 0.10 * s + g + ar1(rng, FIRMS, T, 0.6, 0.2)
    return pd.DataFrame({"firm": np.repeat(np.arange(FIRMS), T),
                         "year": np.tile(YEARS, FIRMS), "y": y.ravel(), "k": k.ravel(),
                         "s": s.ravel().astype(float), "m": np.repeat(m, T),
                         "treated": np.repeat(treated, T).astype(float)})


def _fit(name, coefs, y, X, groups):
    r = ols_cluster(y, X, groups)
    return [(name, c, r["beta"][j], r["se_iid"][j], r["se_cluster"][j])
            for j, c in coefs]


def tables():
    d = panel()
    one = np.ones(len(d))
    rows = _fit("pooled", [(1, "k")], d.y, np.column_stack([one, d.k]), d.firm)
    w = d[["y", "k", "s"]] - d.groupby("firm")[["y", "k", "s"]].transform("mean")
    rows += _fit("within", [(0, "k")], w.y, w[["k"]], d.firm)
    f = d.sort_values(["firm", "year"]).groupby("firm")[["y", "k"]].diff().dropna()
    rows += _fit("first difference", [(1, "k")], f.y,
                 np.column_stack([np.ones(len(f)), f.k]), d.loc[f.index, "firm"])
    rows += _fit("pooled with subsidy", [(1, "k"), (2, "s")], d.y,
                 np.column_stack([one, d.k, d.s]), d.firm)
    tw = d[["y", "k", "s"]].copy()
    tw = tw - tw.groupby(d.firm).transform("mean")
    tw = tw - tw.groupby(d.year).transform("mean")
    rows += _fit("two-way", [(0, "k"), (1, "s")], tw.y, tw[["k", "s"]], d.firm)
    res = pd.DataFrame(rows, columns=["model", "coef", "estimate", "se_iid", "se_cluster"])
    facts = pd.DataFrame({"n_firms": [FIRMS], "years": [len(YEARS)], "rows": [len(d)],
                          "treated": [int(d.groupby("firm").treated.first().sum())],
                          "var_k": [d.k.var()], "cov_km": [np.cov(d.k, d.m)[0, 1]],
                          "sd_y": [d.y.std()]})
    return res, facts


if __name__ == "__main__":
    res, facts = tables()
    write_table(res, __file__, "firms_results", float_format="%.4f")
    write_table(facts, __file__, "firms_facts", float_format="%.4f")

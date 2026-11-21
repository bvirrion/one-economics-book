"""Worked numbers for Book 4, chapter 30 (exercises and the weekend problem)."""

import numpy as np

# Exercise 5: the small data set solved by hand
X5 = np.array([[1, 1, 0], [1, 2, 0], [1, 3, 1], [1, 4, 1], [1, 5, 1]], dtype=float)
Y5 = np.array([4, 4, 9, 13, 14], dtype=float)


def ols(y, X):
    return np.linalg.solve(X.T @ X, X.T @ y)


def r2(y, X):
    e = y - X @ ols(y, X)
    return 1 - (e @ e) / ((y - y.mean()) @ (y - y.mean()))


def adj_r2(r2_value, n, k):
    return 1 - (1 - r2_value) * (n - 1) / (n - k)


def vif(X, j):
    """1 / (1 - R2) from regressing column j on the other columns (incl. constant)."""
    others = np.delete(X, j, axis=1)
    return 1 / (1 - r2(X[:, j], others))


def brenland():
    """Heads with positive gross income: log gross income on schooling and age."""
    from country import load

    h = load("households")
    h = h[h.gross_income > 0]
    y = np.log(h.gross_income.to_numpy())
    s, a = h.school_years.to_numpy(float), h.age_head.to_numpy(float)
    one = np.ones(len(h))
    short = np.column_stack([one, s])
    long = np.column_stack([one, s, a, a**2])
    exper = a - s - 6
    return y, short, long, np.column_stack([one, s, a, exper])


def cps(extra=()):
    from econdata import nsw

    d = nsw("cps_controls")
    d = d[(d.re78 > 0) & (d.re75 > 0)]
    cols = [
        np.ones(len(d)),
        d.education,
        d.age,
        d.age**2,
        d.black,
        d.hispanic,
        d.married,
    ]
    cols += [d[c] for c in extra]
    return np.log(d.re78.to_numpy()), np.column_stack(cols).astype(float)


def collinearity_table(n, seed=30):
    """The listing's loop at sample size n: (rho, se of b1, VIF) for each rho."""
    import statsmodels.api as sm

    rng = np.random.default_rng(seed)
    rows = []
    for rho in (0.0, 0.5, 0.9, 0.99):
        x1 = rng.standard_normal(n)
        x2 = rho * x1 + np.sqrt(1 - rho**2) * rng.standard_normal(n)
        y = 1 + x1 + x2 + rng.standard_normal(n)
        fit = sm.OLS(y, sm.add_constant(np.column_stack([x1, x2]))).fit()
        r = np.corrcoef(x1, x2)[0, 1]
        rows.append((rho, fit.bse[1], 1 / (1 - r**2)))
    return rows


def brenland_ovb():
    """short = long + gamma_age delta_age + gamma_age2 delta_age2 (Part III)."""
    y, short, long, _ = brenland()
    b_long = ols(y, long)
    deltas = [ols(long[:, j], short)[1] for j in (2, 3)]
    bias = b_long[2] * deltas[0] + b_long[3] * deltas[1]
    return ols(y, short)[1], b_long[1], deltas, bias

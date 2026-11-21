"""Worked numbers for Book 4, chapter 31 (exercises and the weekend problem)."""

import numpy as np


def grouping_variance(x, frac, sigma=2.0):
    """Variance of the slope from the means of the bottom and top `frac` of x."""
    k = int(round(frac * len(x)))
    xs = np.sort(x)
    gap = xs[-k:].mean() - xs[:k].mean()
    return sigma**2 * (2 / k) / gap**2


def ols_variance(x, sigma=2.0):
    return sigma**2 / ((x - x.mean()) @ (x - x.mean()))


def f_from_ssr(ssr_r, ssr_u, q, n, k):
    return ((ssr_r - ssr_u) / q) / (ssr_u / (n - k))


def moulton(m, rho_u, rho_x=1.0):
    return np.sqrt(1 + (m - 1) * rho_x * rho_u)


def randhie_tests():
    """D exercise: health dummies and plan variables, classical and robust F."""
    import statsmodels.api as sm
    from econdata import sm_dataset

    d = sm_dataset("randhie")
    X = sm.add_constant(d.drop(columns="mdvis"))
    m = sm.OLS(d.mdvis, X)
    out = {}
    for cov in ("nonrobust", "HC1"):
        f = m.fit(cov_type=cov)
        out[cov] = (
            float(f.f_test("hlthg = hlthf = hlthp = 0").fvalue),
            float(f.f_test("lncoins = idp = lpi = fmde = 0").fvalue),
        )
    return out


def size_rates(hetero, n=200, reps=4000, seed=31):
    """The size listing, with or without unequal error variances."""
    import statsmodels.api as sm

    rng = np.random.default_rng(seed)
    rej = np.zeros(2)
    for _ in range(reps):
        x = rng.standard_normal(n)
        u = (np.abs(x) if hetero else 1.0) * rng.standard_normal(n)
        model = sm.OLS(1 + u, sm.add_constant(x))
        rej += [abs(model.fit().tvalues[1]) > 1.96,
                abs(model.fit(cov_type="HC1").tvalues[1]) > 1.96]  # fmt: skip
    return rej / reps


def firms():
    """Brenland's census of firms: log output on log workers and log capital."""
    from country import load

    f = load("firms")
    y = np.log(f.output.to_numpy(float))
    lab = np.log(f.workers.to_numpy(float))
    cap = np.log(f.capital.to_numpy(float))
    return y, lab, cap, f.sector.to_numpy()


def firms_results():
    import statsmodels.api as sm
    from scipy import stats

    y, lab, cap, sector = firms()
    X = sm.add_constant(np.column_stack([lab, cap]))
    m = sm.OLS(y, X)
    groups = np.unique(sector, return_inverse=True)[1]
    c = m.fit()
    h = m.fit(cov_type="HC1")
    g = m.fit(cov_type="cluster", cov_kwds={"groups": groups})
    restricted = sm.OLS(y - lab, sm.add_constant(cap - lab)).fit()
    t2 = stats.t.ppf(0.975, 2)
    return {
        "b": c.params,
        "se": (c.bse, h.bse, g.bse),
        "sum": c.params[1] + c.params[2],
        "F_ssr": f_from_ssr(restricted.ssr, c.ssr, 1, len(y), 3),
        "F_robust": float(h.f_test("x1 + x2 = 1").fvalue),
        "ci_robust": (c.params[2] - 1.96 * h.bse[2], c.params[2] + 1.96 * h.bse[2]),
        "ci_cluster": (c.params[2] - t2 * g.bse[2], c.params[2] + t2 * g.bse[2]),
        "t2": t2,
        "ssr": (restricted.ssr, c.ssr),
        "r2": c.rsquared,
    }

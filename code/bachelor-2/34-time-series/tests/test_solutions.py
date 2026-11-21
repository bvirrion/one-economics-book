"""The numbers of b2 ch. 34, recomputed by a second route.

t statistics from correlations, autocorrelations and AR fits by numpy, the
Dickey-Fuller, Granger and Newey-West statistics built by hand, and Brenland's AR(1)
forecast from its closed form.
"""

import importlib.util
import re
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "code" / "shared"), str(ROOT / "figdata" / "lib")]
spec = importlib.util.spec_from_file_location(
    "sol34", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def out(name):
    return (HERE / "outputs" / f"{name}.txt").read_text()


def nums(name):
    return [float(v) for v in re.findall(r"-?\d+\.\d+", out(name))]


def ols(y, X):
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    e = y - X @ b
    cov = np.linalg.inv(X.T @ X) * (e @ e) / (len(y) - X.shape[1])
    return b, np.sqrt(np.diag(cov)), e


def macro():
    from econdata import sm_dataset

    return sm_dataset("macrodata")


def test_random_walks_by_correlation():
    rng = np.random.default_rng(34)
    n, reps, lev, dif, r2 = 200, 2000, 0, 0, []
    for _ in range(reps):
        x = rng.standard_normal(n).cumsum()
        y = rng.standard_normal(n).cumsum()
        for a, b, d in ((x, y, 0), (np.diff(x), np.diff(y), 1)):
            r = np.corrcoef(a, b)[0, 1]
            big = abs(r * np.sqrt((len(a) - 2) / (1 - r**2))) > 1.96
            lev, dif = (lev + big, dif) if d == 0 else (lev, dif + big)
            if d == 0:
                r2.append(r**2)
    printed = [nums("random_walks")[i] for i in (1, 2, 4)]  # skip the two 1.96
    mine = [float(f"{v:.3f}") for v in (lev / reps, np.median(r2), dif / reps)]
    assert printed == mine
    assert printed == [0.839, 0.174, 0.059]


def test_acf_lags_by_hand():
    d = macro()
    for name in ("infl", "unemp"):
        x = d[name].to_numpy() - d[name].mean()
        r = [(x[k:] @ x[:-k]) / (x @ x) for k in range(1, 5)]
        assert f"{np.round(r, 3)}" in out("acf")
    assert "+/- 0.138" in out("acf")


def test_ar_fits_by_numpy():
    u = macro().unemp.to_numpy()
    b, _, _ = ols(u[1:], np.column_stack([np.ones(len(u) - 1), u[:-1]]))
    assert f"c {b[0]:.4f}, phi {b[1]:.4f}" in out("ar_fit")
    assert f"half-life {np.log(0.5) / np.log(b[1]):.1f}" in out("ar_fit")
    b2, se2, _ = ols(u[2:], np.column_stack([np.ones(len(u) - 2), u[1:-1], u[:-2]]))
    assert f"t of the second lag {b2[2] / se2[2]:.2f}" in out("ar_fit")
    assert (round(b[1], 4), round(b[0] / (1 - b[1]), 2)) == (0.988, 7.44)


def df_by_hand(x, lags, trend):
    dx = np.diff(x)
    n = len(dx) - lags
    cols = [np.ones(n), x[lags:-1]]
    if trend:
        cols.append(np.arange(1, n + 1))
    cols += [dx[lags - k : -k] for k in range(1, lags + 1)]
    b, se, _ = ols(dx[lags:], np.column_stack(cols))
    return b[1] / se[1]


def test_dickey_fuller_by_hand():
    lg = np.log(macro().realgdp.to_numpy())
    assert f"ADF {df_by_hand(lg, 2, True):6.2f}" in out("adf")
    assert f"ADF {df_by_hand(400 * np.diff(lg), 1, False):6.2f}" in out("adf")
    assert [nums("adf")[i] for i in (0, 1, 2, 3)] == [-2.38, -3.43, 0.389, -6.97]


def test_granger_by_hand():
    d = macro()
    m = 400 * np.diff(np.log(d.m1.to_numpy()))
    infl = d.infl.to_numpy()[1:]
    for target, cause, text in ((infl, m, "F 2.15"), (m, infl, "F 1.47")):
        y = target[4:]
        lags_y = [target[4 - k : -k] for k in range(1, 5)]
        lags_x = [cause[4 - k : -k] for k in range(1, 5)]
        X_r = np.column_stack([np.ones(len(y))] + lags_y)
        X_u = np.column_stack([X_r] + lags_x)
        ssr_r = (ols(y, X_r)[2] ** 2).sum()
        ssr_u = (ols(y, X_u)[2] ** 2).sum()
        F = (ssr_r - ssr_u) / 4 / (ssr_u / (len(y) - X_u.shape[1]))
        assert f"F {F:.2f}" == text and text in out("granger")


def test_newey_west_by_hand():
    d = macro()
    p = np.log(d.cpi.to_numpy())
    pi4 = 100 * (p[4:] - p[:-4])
    u = d.unemp.to_numpy()[4:]
    y = pi4[4:] - pi4[:-4]
    X = np.column_stack([np.ones(len(y)), u[:-4]])
    b, se, e = ols(y, X)
    L = 4  # Bartlett weights, maxlags 4
    g = X * e[:, None]
    S = g.T @ g
    for j in range(1, L + 1):
        G = g[j:].T @ g[:-j]
        S += (1 - j / (L + 1)) * (G + G.T)
    A = np.linalg.inv(X.T @ X)
    nw = np.sqrt((A @ S @ A)[1, 1])  # statsmodels default: no small-sample factor
    assert f"classical s.e. {se[1]:.3f}, Newey-West s.e. {nw:.3f}" in out("hac")
    assert f"slope on unemployment {b[1]:.3f}" in out("hac")


def test_forecast_rmse_matches_chart_data():
    import pandas as pd

    f = pd.read_csv(ROOT / "figdata/bachelor-2/34-time-series/out/fcst.csv")
    for col, label in (("ar", "regression"), ("rw", "random walk")):
        r = np.sqrt(((f.actual - f[col]) ** 2).mean())
        assert (
            abs(float(re.search(label + r"\s+RMSE (\d+\.\d+)", out("forecast"))[1]) - r)
            < 2e-3
        )
    assert "forecasts: 95" in out("forecast")


def test_brenland_closed_form():
    years, pi = sol.brenland_inflation()
    x, y = pi[:-1], pi[1:]
    phi = ((x - x.mean()) @ (y - y.mean())) / ((x - x.mean()) @ (x - x.mean()))
    c = y.mean() - phi * x.mean()
    r = sol.brenland()
    assert np.isclose(r["phi"], phi) and np.isclose(r["c"], c)
    f2 = c * (1 + phi) + phi**2 * pi[-1]
    assert np.isclose(r["f2"], f2)
    assert (round(r["phi"], 2), round(r["half_life"], 2), round(r["f2"], 2)) == (
        0.48,
        0.96,
        2.65,
    )
    assert (round(r["lo2"], 1), round(r["hi2"], 1), round(r["df"], 2)) == (
        -0.8,
        6.1,
        -2.77,
    )
    assert (len(pi), int(r["max_year"]), round(r["max"], 1)) == (25, 2022, 9.7)
    assert (
        sol.ar1_acf(0.5, 3) == 0.125 and sol.long_run_multiplier([0.2, 0.3, 0.1]) == 0.6
    )


def test_phillips_forecast_by_statsmodels():
    import pandas as pd
    import statsmodels.api as sm

    d = macro()
    t = d.year + (d.quarter - 1) / 4
    pi4 = 100 * np.log(d.cpi).diff(4)
    frame = pd.DataFrame(
        {"y": pi4.shift(-4), "p0": pi4, "p4": pi4.shift(4), "u": d.unemp}
    )
    err = []
    for i in np.flatnonzero((t >= 1985).to_numpy() & frame.y.notna().to_numpy()):
        train = frame.iloc[8 : i - 3]
        fit = sm.OLS(train.y, sm.add_constant(train[["p0", "p4", "u"]])).fit()
        x = np.r_[1.0, frame.loc[i, ["p0", "p4", "u"]].to_numpy(float)]
        err.append(frame.y[i] - fit.params.to_numpy() @ x)
    assert len(err) == 95
    assert np.isclose(np.sqrt(np.mean(np.square(err))), sol.phillips_forecast()["ar+u"])
    assert round(sol.phillips_forecast()["ar+u"], 3) == 1.775


def test_brenland_df_by_hand():
    _, pi = sol.brenland_inflation()
    assert np.isclose(df_by_hand_nolag(pi), sol.brenland()["df"])
    assert round(sol.brenland_df_critical()["5%"], 2) == -2.99


def df_by_hand_nolag(x):
    dx = np.diff(x)
    b, se, _ = ols(dx, np.column_stack([np.ones(len(dx)), x[:-1]]))
    return b[1] / se[1]


def test_surge_and_mean_se():
    _, pi = sol.brenland_inflation()
    r = sol.brenland()
    s = sol.surge()
    assert np.isclose(s["f23"], r["c"] + r["phi"] * 9.6956, atol=1e-3)
    assert (round(s["resid"], 2), round(s["z"], 1)) == (6.51, 4.2)
    assert (round(s["f23"], 2), round(s["a23"], 2), round(s["f24"], 2), round(s["a24"], 2)) == (
        6.09, 5.49, 4.05, 3.71)  # fmt: skip
    # delta method against a numerical derivative of c / (1 - phi)
    u = macro().unemp.to_numpy()
    b, _, e = ols(u[1:], np.column_stack([np.ones(len(u) - 1), u[:-1]]))
    X = np.column_stack([np.ones(len(u) - 1), u[:-1]])
    V = np.linalg.inv(X.T @ X) * (e @ e) / (len(e) - 2)
    h = 1e-6
    m = lambda c, p: c / (1 - p)  # noqa: E731
    g = np.array(
        [
            (m(b[0] + h, b[1]) - m(b[0], b[1])) / h,
            (m(b[0], b[1] + h) - m(b[0], b[1])) / h,
        ]
    )
    assert abs(np.sqrt(g @ V @ g) - sol.unemp_mean_se()) < 1e-2
    assert round(sol.unemp_mean_se(), 1) == 3.0

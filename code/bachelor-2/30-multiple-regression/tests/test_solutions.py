"""The numbers the text and solutions of b2 ch. 30 print, recomputed by another route.

The solutions use numpy's normal equations; the tests use statsmodels (and hand values),
so a wrong design matrix or formula in one shows up as a disagreement.
"""

import importlib.util
import re
import sys
from pathlib import Path

import numpy as np
import statsmodels.api as sm
from statsmodels.stats.outliers_influence import variance_inflation_factor

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "code" / "shared"), str(ROOT / "figdata" / "lib")]
spec = importlib.util.spec_from_file_location(
    "sol30", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def out(name):
    return (HERE / "outputs" / f"{name}.txt").read_text()


def num(text, label):
    return float(re.search(re.escape(label) + r"\s+(-?[\d.]+)", text).group(1))


def test_hand_example():
    assert sol.ols(sol.Y5, sol.X5).round(10).tolist() == [1, 2, 3]
    assert (sol.X5.T @ sol.X5).tolist() == [[5, 15, 3], [15, 55, 12], [3, 12, 3]]
    # SSR 4, SST 90.8 by hand
    assert round(sol.r2(sol.Y5, sol.X5), 3) == round(1 - 4 / 90.8, 3) == 0.956
    assert round(sol.adj_r2(1 - 4 / 90.8, 5, 3), 3) == round(1 - 2 / 22.7, 3) == 0.912
    assert round(sol.adj_r2(0.1181, 13055, 7), 4) == 0.1177


def test_cps_listings_against_statsmodels():
    y, X = sol.cps()
    fit = sm.OLS(y, X).fit()
    b = fit.params[1]
    assert num(out("fwl"), "long regression:") == round(b, 6) == 0.038343
    assert num(out("fwl"), "residual on residual:") == round(b, 6)
    assert num(out("ovb"), "short regression (no 1975 earnings):") == round(b, 6)
    y2, X2 = sol.cps()
    from econdata import nsw

    d = nsw("cps_controls")
    d = d[(d.re78 > 0) & (d.re75 > 0)]
    long = sm.OLS(y2, np.column_stack([X2, np.log(d.re75)])).fit()
    assert num(out("ovb"), "long regression:") == round(long.params[1], 6) == 0.020429
    assert num(out("ovb"), "gamma, effect of log 1975 earnings:") == round(
        long.params[-1], 6
    )
    assert round(fit.rsquared, 4) == 0.1181
    assert round(long.rsquared, 3) == 0.254  # text: R2 from 0.118 to 0.254


def test_cps_nodegree():
    y, X = sol.cps(("nodegree",))
    fit = sm.OLS(y, X).fit()
    assert (round(fit.params[1], 4), round(fit.params[-1], 4)) == (0.0216, -0.1482)
    assert round(variance_inflation_factor(X, 1), 2) == round(sol.vif(X, 1), 2) == 2.24
    assert round(variance_inflation_factor(sol.cps()[1], 1), 2) == 1.14


def test_brenland():
    y, short, long, exper = sol.brenland()
    assert len(y) == 1922
    fs, fl = sm.OLS(y, short).fit(), sm.OLS(y, long).fit()
    assert (round(fs.params[1], 4), round(fl.params[1], 4)) == (0.0580, 0.0584)
    lo, hi = fl.conf_int()[1]
    assert (round(lo, 4), round(hi, 4)) == (0.0518, 0.0649)
    assert (
        round(fs.rsquared, 3),
        round(fl.rsquared, 3),
        round(fl.rsquared_adj, 3),
    ) == (
        0.108,
        0.309,
        0.308,
    )
    s, b, deltas, bias = sol.brenland_ovb()
    assert abs(s - (b + bias)) < 1e-12
    assert (round(deltas[0], 3), round(deltas[1], 2), round(bias, 5)) == (
        0.318,
        30.99,
        -0.00036,
    )
    vifs = [variance_inflation_factor(long, j) for j in (1, 2, 3)]
    assert [round(v, 1) for v in vifs] == [1.0, 43.5, 43.5]
    assert np.linalg.matrix_rank(exper) == 3


def test_collinearity_listing_and_n2000():
    lines = out("collinearity").splitlines()[2:6]
    table = sol.collinearity_table(500)
    for line, (rho, se, v) in zip(lines, table):
        cells = line.split()
        assert (
            float(cells[0]) == rho
            and cells[3] == f"{se:.3f}"
            and cells[4] == f"{v:.1f}"
        )
    big = sol.collinearity_table(2000)
    assert [f"{se:.3f}" for _, se, _ in big] == ["0.022", "0.025", "0.052", "0.160"]
    # by the variance formula the standard error at rho = 0 halves when n is four times larger
    assert abs(table[0][1] / big[0][1] - 2) < 0.1


def test_age_example():
    """Exercise 6: adding age, by statsmodels, against the bias formula by hand."""
    y, X = sol.cps()
    short = sm.OLS(y, X[:, :2]).fit().params[1]
    long = sm.OLS(y, X[:, :3]).fit().params
    delta = sm.OLS(X[:, 2], X[:, :2]).fit().params[1]
    assert (round(short, 4), round(long[1], 4)) == (0.0410, 0.0522)
    assert (round(long[2], 4), round(delta, 3)) == (0.0192, -0.585)
    assert round(0.0522 + 0.0192 * -0.585, 4) == 0.0410  # the printed, rounded values
    assert round(np.corrcoef(X[:, 1], X[:, 2])[0, 1], 2) == -0.15

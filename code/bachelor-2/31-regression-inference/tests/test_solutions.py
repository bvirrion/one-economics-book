"""The numbers of b2 ch. 31, recomputed by a second route.

Robust and cluster covariances and Wald statistics are rebuilt here with numpy from
their formulas, against statsmodels in the solutions; variances of the grouping
estimator are checked against hand values; simulations against their outputs.
"""

import importlib.util
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "code" / "shared"), str(ROOT / "figdata" / "lib")]
spec = importlib.util.spec_from_file_location(
    "sol31", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def out(name):
    return (HERE / "outputs" / f"{name}.txt").read_text()


def sandwich(X, e, groups=None):
    n, k = X.shape
    a = np.linalg.inv(X.T @ X)
    if groups is None:
        meat = (X * e[:, None] ** 2).T @ X
        return a @ meat @ a * n / (n - k)
    g = np.unique(groups)
    s = np.array([X[groups == j].T @ e[groups == j] for j in g])
    c = len(g) / (len(g) - 1) * (n - 1) / (n - k)
    return c * a @ (s.T @ s) @ a


def test_grouping_by_hand():
    x = np.linspace(0, 10, 40)
    # bottom half mean 2.436, top half 7.564: gap 5.128; 4 * (1/20 + 1/20) / 5.128^2
    assert (
        round(sol.grouping_variance(x, 0.5), 5)
        == round(0.4 / (200 / 39) ** 2, 5)
        == 0.01521
    )
    # quarters: gap 10 - 2 * 45 / 39 = 7.692
    assert round(sol.grouping_variance(x, 0.25), 5) == round(0.8 / (300 / 39) ** 2, 5)
    assert round(sol.ols_variance(x), 5) == 0.01141
    assert "groups    0.4998       0.01508               0.01521" in out(
        "gauss_markov_sim"
    )


def test_f_and_moulton():
    assert round(sol.f_from_ssr(382137.5, 381469.6, 3, 20190, 10), 2) == 11.78
    assert "F by hand 11.778; statsmodels 11.778" in out("t_and_f")
    assert round(sol.moulton(25, 0.1), 2) == 1.84
    assert "sqrt(1 + (m - 1) rho): 2.191" in out("cluster_sim")
    assert "cluster over classical: 2.115" in out("cluster_sim")


def test_randhie_wald_by_hand():
    from econdata import sm_dataset

    d = sm_dataset("randhie")
    X = np.column_stack([np.ones(len(d)), d.drop(columns="mdvis").to_numpy(float)])
    y = d.mdvis.to_numpy(float)
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    V = sandwich(X, y - X @ b)
    R = np.zeros((3, 10))
    R[0, 7] = R[1, 8] = R[2, 9] = 1
    rb = R @ b
    wald = rb @ np.linalg.solve(R @ V @ R.T, rb) / 3
    res = sol.randhie_tests()
    assert round(wald, 2) == round(res["HC1"][0], 2) == 5.40
    assert [round(v, 2) for v in res["nonrobust"]] == [11.78, 82.26]
    assert round(res["HC1"][1], 2) == 80.80


def test_size():
    lines = out("size_sim").splitlines()
    assert lines[1].endswith("0.254") and lines[2].endswith("0.057")
    assert tuple(np.round(sol.size_rates(True), 3)) == (0.254, 0.057)
    assert tuple(np.round(sol.size_rates(False), 3)) == (0.054, 0.056)


def test_firms_by_hand():
    y, lab, cap, sector = sol.firms()
    X = np.column_stack([np.ones(len(y)), lab, cap])
    b = np.linalg.lstsq(X, y, rcond=None)[0]
    e = y - X @ b
    r = sol.firms_results()
    assert np.allclose(np.sqrt(np.diag(sandwich(X, e))), r["se"][1])
    assert np.allclose(np.sqrt(np.diag(sandwich(X, e, sector))), r["se"][2])
    assert [round(v, 4) for v in r["b"]] == [2.7766, 0.6498, 0.3516]
    assert [round(s[2], 4) for s in r["se"]] == [0.0124, 0.0120, 0.0044]
    assert round(r["F_ssr"], 3) == 0.053 and round(r["F_robust"], 3) == 0.055
    assert [round(v, 3) for v in r["ci_robust"] + r["ci_cluster"]] == [
        0.328,
        0.375,
        0.333,
        0.371,
    ]
    assert round(r["t2"], 3) == 4.303 and round(r["sum"], 4) == 1.0014


def test_critical_values_and_small_numbers():
    from scipy import stats

    assert round(stats.f.ppf(0.95, 1, 497), 2) == 3.86
    assert round(stats.f.ppf(0.95, 4, 20180), 3) == 2.372
    assert round(1.0658 / 0.1293, 2) == 8.24  # robust t of physlm, from printed values
    assert round(25 / (1 + 24 * 0.1), 1) == 7.4  # pupils' worth per class

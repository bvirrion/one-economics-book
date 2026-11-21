"""The numbers of b2 ch. 32, recomputed by a second route.

Engel fits by numpy least squares; the proxy and attenuation results against their
population formulas (worked by hand below); counts of tests by the binomial formula.
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
    "sol32", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def out(name):
    return (HERE / "outputs" / f"{name}.txt").read_text()


def test_engel_by_numpy():
    from econdata import sm_dataset

    d = sm_dataset("engel")
    b = np.polyfit(np.log(d.income), np.log(d.foodexp), 1)[0]
    assert f"elasticity {b:.3f}" in out("engel") and round(b, 3) == 0.856
    slope = np.polyfit(d.income, d.foodexp, 1)[0]
    assert round(slope * d.income.mean() / d.foodexp.mean(), 3) == 0.764
    c = np.log(d.income) - np.log(d.income).mean()
    coef = np.polyfit(c, np.log(d.foodexp), 2)  # highest power first
    q = sol.engel_quadratic()
    assert np.allclose([coef[1], coef[0]], [q["b1"], q["b2"]])
    assert (round(q["b1"], 3), round(q["b2"], 3)) == (0.872, -0.077)
    assert (round(q["e10"], 2), round(q["e90"], 2), round(q["p2"], 3)) == (
        0.96,
        0.79,
        0.014,
    )


def proxy_plim(noise):
    """Population coefficient on schooling with the score as control, by hand.

    Var(s) = 1.5^2 + 2^2 = 6.25, Var(q) = 1 + noise^2, Cov(s, q) = Cov(s, a) = 1.5,
    Cov(q, a) = 1. The bias is 0.10 times the coefficient on s in the projection of
    ability on (s, q).
    """
    S = np.array([[6.25, 1.5], [1.5, 1 + noise**2]])
    delta = np.linalg.solve(S, np.array([1.5, 1.0]))[0]
    return 0.08 + 0.10 * delta


def test_proxy_against_population():
    text = out("proxy")
    assert abs(float(re.search(r"no control for ability\s+([\d.]+)", text).group(1))
               - (0.08 + 0.10 * 1.5 / 6.25)) < 0.002  # fmt: skip
    assert (
        abs(float(re.search(r"as a proxy\s+([\d.]+)", text).group(1)) - proxy_plim(0.7))
        < 0.002
    )
    assert round(proxy_plim(0.7), 4) == 0.0904
    assert round(sol.proxy_coef(0.3), 3) == 0.083
    assert abs(sol.proxy_coef(0.3) - proxy_plim(0.3)) < 0.002


def test_attenuation_against_lambda():
    rows = [line.split() for line in out("attenuation").splitlines()[2:]]
    for s2, x_noisy, plim, y_noisy in rows:
        assert abs(float(x_noisy) - 2 / (1 + float(s2))) < 0.01
        assert float(plim) == round(2 / (1 + float(s2)), 3)
        assert abs(float(y_noisy) - 2) < 0.01


def test_search_and_small_numbers():
    assert round(sol.any_rejection(20), 3) == 0.642
    assert "best of 20 significant at 5 %:        0.640" in out("search")
    assert round(sol.bonferroni_z(20), 2) == 3.02
    assert (round(sol.percent(0.738), 2), round(sol.percent(0.440), 3)) == (1.09, 0.553)
    assert round(sol.corrected(0.196, 0.8), 3) == 0.245


def test_brenland_food():
    h, plain, sizes, inter = sol.brenland_food()
    X = np.column_stack([np.ones(len(h)), h.linc])
    assert round(np.linalg.lstsq(X, h.lfood, rcond=None)[0][1], 3) == 0.288
    dummies = [(h["size"] == k).astype(float) for k in range(2, 6)]
    X2 = np.column_stack([np.ones(len(h)), h.linc, *dummies, h.owner])
    b = np.linalg.lstsq(X2, h.lfood, rcond=None)[0]
    assert round(b[1], 3) == round(sizes.params.linc, 3) == 0.196
    assert [round(v, 3) for v in b[2:6]] == [0.246, 0.440, 0.597, 0.738]
    g = inter.params["linc:owner"]
    assert (round(inter.params.linc, 3), round(inter.params.linc + g, 3)) == (
        0.187,
        0.211,
    )
    assert (round(g, 3), round(inter.bse["linc:owner"], 3)) == (0.024, 0.009)
    assert round(sizes.rsquared, 3) == 0.924 and round(plain.rsquared, 3) == 0.181


def test_problem_extras():
    _, _, _, inter = sol.brenland_food()
    t = inter.params["linc:owner"] / inter.bse["linc:owner"]
    assert round(t, 2) == 2.64 and 1.96 < t < sol.bonferroni_z(20)
    assert round(sol.any_rejection(20, 0.0025), 4) == 0.0488
    assert round(sol.percent(0.15), 3) == 0.162

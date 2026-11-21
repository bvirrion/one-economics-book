"""The numbers of b2 ch. 33, recomputed by a second route.

Differences in means and their standard errors by a plain loop, regression by numpy,
the sample-size formula against statsmodels' power solver, and the selection identity
checked from the printed numbers.
"""

import importlib.util
import math
import re
import sys
from pathlib import Path

import numpy as np

HERE = Path(__file__).resolve().parents[1]
ROOT = HERE.parents[2]
sys.path[:0] = [str(ROOT / "code" / "shared"), str(ROOT / "figdata" / "lib")]
spec = importlib.util.spec_from_file_location(
    "sol33", HERE / "exercises" / "solutions.py"
)
sol = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sol)


def out(name):
    return (HERE / "outputs" / f"{name}.txt").read_text()


def mean_var(x):
    m = sum(x) / len(x)
    return m, sum((v - m) ** 2 for v in x) / (len(x) - 1)


def test_experiment_by_loop():
    from econdata import nsw

    d = nsw("nsw_dw")
    t = [v for v, g in zip(d.re78, d.treat) if g == 1]
    c = [v for v, g in zip(d.re78, d.treat) if g == 0]
    (mt, vt), (mc, vc) = mean_var(t), mean_var(c)
    se = math.sqrt(vt / len(t) + vc / len(c))
    assert f"difference {mt - mc:.1f}, s.e. {se:.1f}" in out("nsw_experiment")
    assert (round(mt - mc, 1), round(se, 1)) == (1794.3, 671.0)


def test_adjustment_by_numpy():
    import pandas as pd
    from econdata import nsw

    exp = nsw("nsw_dw")
    obs = pd.concat([exp.query("treat == 1"), nsw("cps_controls")])
    cols = [
        "age",
        "education",
        "black",
        "hispanic",
        "married",
        "nodegree",
        "re74",
        "re75",
    ]
    for d, expect in ((exp, "1675.9"), (obs, "793.6")):
        X = np.column_stack(
            [np.ones(len(d)), d.treat, d.age**2, d[cols].to_numpy(float)]
        )
        b = np.linalg.lstsq(X, d.re78.to_numpy(float), rcond=None)[0][1]
        assert f"{b:.1f}" == expect and expect in out("regression_adjust")
    assert "naive difference -8497.5" in out("naive_cps")


def test_selection_identity_and_balance():
    nums = [float(v) for v in re.findall(r"-?\d+\.\d+", out("selection_sim"))]
    ate, att, diff, att2, bias, total, rand = nums
    assert att2 == att and round(att + bias, 3) == diff == total
    assert (ate, att, bias, rand) == (1.001, 1.284, -2.221, 1.051)
    lines = out("balance").splitlines()[2:]
    big = [line.split()[0] for line in lines if abs(float(line.split()[-1])) > 1.96]
    assert big == ["nodegree"]
    assert round(sol.any_imbalance(8), 3) == 0.337


def test_pilot():
    r = sol.rct()
    assert (round(r["ate"]), round(r["diff"]), round(r["se"])) == (1499, 1100, 362)
    assert (round(r["lo"]), round(r["hi"]), round(r["sd0"])) == (389, 1810, 5217)
    w = sol.rollout()
    assert abs(w["diff"] - w["att"] - w["bias"]) < 1e-6
    assert (round(w["diff"]), round(w["att"]), round(w["bias"]), w["share"]) == (
        5272,
        1782,
        3491,
        0.51,
    )


def test_sample_size_against_statsmodels():
    from statsmodels.stats.power import NormalIndPower

    for delta, sigma in ((1500, 5000), (1500, 5216.85), (750, 5000)):
        n_sm = NormalIndPower().solve_power(
            effect_size=delta / sigma, alpha=0.05, power=0.8
        )
        assert abs(sol.n_per_arm(delta, sigma) - n_sm) < 0.5
    assert [math.ceil(sol.n_per_arm(1500, s)) for s in (5000, 5216.85)] == [175, 190]
    assert math.ceil(sol.n_per_arm(750, 5000)) == 698


def test_low_earners_by_numpy():
    import pandas as pd
    from econdata import nsw

    n, raw, _, adj, _ = sol.low_earners()
    cps = nsw("cps_controls")
    low = cps[cps.re75 < 5000]
    d = pd.concat([nsw("nsw_dw").query("treat == 1"), low])
    y = d.re78.to_numpy(float)
    t = d.treat.to_numpy(float)
    assert round(y[t == 1].mean() - y[t == 0].mean()) == round(raw) == 127
    cols = [
        "age",
        "education",
        "black",
        "hispanic",
        "married",
        "nodegree",
        "re74",
        "re75",
    ]
    X = np.column_stack([np.ones(len(d)), t, d.age**2, d[cols].to_numpy(float)])
    assert round(np.linalg.lstsq(X, y, rcond=None)[0][1]) == round(adj) == 1193
    assert n == 4231


def test_power_against_statsmodels():
    from statsmodels.stats.power import NormalIndPower

    p_sm = NormalIndPower().power(effect_size=1500 / 5216.85, nobs1=400, alpha=0.05)
    assert abs(sol.power(400, 1500, 5216.85) - p_sm) < 1e-3
    assert round(sol.power(400, 1500, 5216.85), 2) == 0.98


def test_low_earners_keeps_high_trainees():
    # the 5,000-dollar cut applies to the survey men only: count the trainees above it
    from econdata import nsw

    e = nsw("nsw_dw").query("treat == 1")
    assert (len(e), int((e.re75 >= 5000).sum())) == (185, 20)

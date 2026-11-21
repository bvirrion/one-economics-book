import numpy as np
from schooling_data import draw


def test_ability_bias_ols_overstates_and_formula_agrees(run):
    _, r = run("ability_bias")
    ols = float(r["OLS slope"])
    assert 0.11 < ols < 0.14                      # 0.08 + 0.10 / 2.16 in the limit
    assert abs(ols - float(r["0.08 + 0.10 * slope(a, s)"])) < 0.002


def test_wald_equals_2sls_and_is_near_the_truth(run):
    _, r = run("tsls_by_hand")
    assert r["Wald ratio"] == r["2SLS slope"]
    assert abs(float(r["2SLS slope"]) - 0.08) < 2 * float(r["2SLS s.e."])
    assert float(r["first-stage F"]) > 100


def test_naive_se_differs_from_the_correct_one(run):
    out, _ = run("tsls_by_hand")
    se = {line[:16].strip(): line[16:].split()[0] for line in out.splitlines()}
    assert float(se["naive s.e."]) > float(se["2SLS s.e."])


def test_draw_is_seeded():
    a, b = draw(100, 5), draw(100, 5)
    assert np.array_equal(a["school"], b["school"])


def test_weak_instruments_bias_toward_ols_and_oversize(run):
    out, _ = run("weak_iv")
    rows = [line.split() for line in out.splitlines()[1:]]
    f = {int(r[0]): [float(x) for x in r[1:]] for r in rows}
    assert abs(f[2][0] - 2) < 0.3 and abs(f[50][0] - 50) < 2
    assert f[2][1] > 0.2 > abs(f[50][1])          # the median 2SLS drifts toward OLS
    assert f[2][3] > 0.08 and abs(f[50][3] - 0.05) < 0.015


def test_late_recovers_compliers_not_everyone(run):
    _, r = run("late_sim")
    wald, late, ate = (float(r[k]) for k in ("Wald estimate", "compliers' mean gain",
                                              "everyone's mean gain (ATE)"))
    assert abs(wald - late) < 0.015
    assert abs(late - 0.15) < 0.002 and abs(ate - 0.115) < 0.002
    assert abs(float(r["first stage (complier share)"]) - 0.30) < 0.005


def test_geography_first_stage_is_strong_and_iv_imprecise(run):
    out, r = run("geography_iv")
    assert r["countries"] == "157"
    assert float(r["first-stage F"]) > 10
    lines = [line for line in out.splitlines() if "elasticity" in line]
    ols_b, iv_b = (float(line.split()[2]) for line in lines)
    iv_se = float(lines[1].split()[4].rstrip(")"))
    assert ols_b > iv_b > 0 and iv_b - 1.96 * iv_se < 0

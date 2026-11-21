def test_ex08_without_population_the_first_stage_halves(run_exercise):
    out, r = run_exercise("ex08_no_population")
    assert 15 < float(r["first-stage F"]) < 18
    lines = [line for line in out.splitlines() if "elasticity" in line]
    ols_b, iv_b = (float(line.split()[2]) for line in lines)
    iv_se = float(lines[1].split()[4].rstrip(")"))
    assert ols_b > iv_b and iv_b - 1.96 * iv_se < 0
    assert float(r["corr(log trade, log pop)"]) < -0.5


def test_ex10_f5_test_is_oversized_and_median_near_zero(run_exercise):
    _, r = run_exercise("ex10_weak_f5")
    assert abs(float(r["mean first-stage F"]) - 5) < 0.3
    assert 0.07 < float(r["rejects b = 0 at 5%"]) < 0.11
    assert abs(float(r["median 2SLS"])) < 0.06
    assert 0.10 < float(r["share of draws with F>10"]) < 0.16


def test_ex10_selecting_on_f_moves_toward_ols(run_exercise):
    _, r = run_exercise("ex10_weak_f5")
    assert float(r["median 2SLS if F>10"]) > 0.25 > 0 > float(r["median 2SLS if F<=10"])

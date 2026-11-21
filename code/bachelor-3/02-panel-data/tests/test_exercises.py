def test_ex05_clustered_errors_are_larger(run_exercise):
    out, _ = run_exercise("ex05_year_effects")
    for line in out.splitlines()[:2]:
        f = line.split()
        iid, cl = float(f[-4]), float(f[-1])
        assert cl > 2 * iid
    assert "2.068" in out.splitlines()[1]


def test_ex09_fertility_falls_with_income_both_ways(run_exercise):
    _, r = run_exercise("ex09_fertility")
    assert -1.0 < float(r["between slope"]) < -0.6
    assert -1.0 < float(r["within slope"]) < -0.6


def test_ex11_nickell_formula_good_for_long_panels(run_exercise):
    out, _ = run_exercise("ex11_nickell")
    rows = [list(map(float, line.split())) for line in out.splitlines()[1:]]
    for T, _, bias, approx in rows:
        assert bias < 0
        if T >= 10:
            assert abs(bias - approx) < 0.02

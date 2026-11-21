def test_load_trade(run):
    out, _ = run("load_trade")
    assert "countries 224" in out and "CHN    USA" in out


def test_ols_distance_in_range(run):
    _, rows = run("gravity_ols")
    out, _ = run("gravity_ols")
    line = [s for s in out.splitlines() if s.startswith("ln_dist")][0]
    assert -1.5 < float(line.split()[1]) < -0.6


def test_fe_and_ppml(run):
    for name, lo, hi in (("gravity_fe", -1.8, -1.0), ("gravity_ppml", -1.0, -0.4)):
        out, _ = run(name)
        line = [s for s in out.splitlines() if s.startswith("ln_dist")][0]
        assert lo < float(line.split()[1]) < hi
    assert "converged True" in run("gravity_ppml")[0]

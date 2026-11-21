def test_ex05_three_samples(run_exercise):
    out, _ = run_exercise("ex05_convergence")
    assert len(out.splitlines()) == 3 and "(25 countries)" in out


def test_ex06_levels_more_persistent(run_exercise):
    out, _ = run_exercise("ex06_persistence")
    for line in out.splitlines():
        g = float(line.split("growth")[1].split(",")[0])
        lev = float(line.split("level")[1].split()[0])
        assert lev > g


def test_ex11_investment_robust(run_exercise):
    out, _ = run_exercise("ex11_bounds")
    assert out.splitlines()[0].endswith("robust")

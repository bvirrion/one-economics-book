def test_ex05_dummy_matches_the_zero_group(run_exercise):
    out, _ = run_exercise("ex05_zero_earnings")
    lines = out.splitlines()
    assert lines[1].split()[-1] == lines[2].split()[-1]


def test_ex11_ols_biased_iv_recovers(run_exercise):
    out, _ = run_exercise("ex11_endogenous_price")
    ols = float(out.splitlines()[1].split()[1])
    iv = float(out.splitlines()[2].split()[1])
    assert ols > -1.5 and abs(iv + 2) < 0.15

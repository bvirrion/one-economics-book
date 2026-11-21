def test_ex08_five(run_exercise):
    out, _ = run_exercise("ex08_ageing")
    assert len(out.splitlines()) == 6


def test_ex12_recovers(run_exercise):
    out, _ = run_exercise("ex12_age_rd")
    est = float(out.splitlines()[-1].split()[4])
    assert abs(est - 0.15) < 0.05

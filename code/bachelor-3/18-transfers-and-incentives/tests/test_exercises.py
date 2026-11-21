def test_ex08_rates(run_exercise):
    out, _ = run_exercise("ex08_one_child")
    assert "phase-in 34.00 %" in out and "highest" in out


def test_ex12_gini_falls(run_exercise):
    out, _ = run_exercise("ex12_gini")
    lines = out.splitlines()
    assert float(lines[0].split()[-1]) > float(lines[2].split()[-1])

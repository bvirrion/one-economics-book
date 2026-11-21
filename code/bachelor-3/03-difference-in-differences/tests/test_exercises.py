def test_ex06_placebo_small_against_its_error(run_exercise):
    out, _ = run_exercise("ex06_placebo_1974")
    for line in out.splitlines()[1:]:
        f = line.split()
        est, se = float(f[-2]), float(f[-1].strip("()"))
        assert abs(est) < 1.96 * se


def test_ex10_wrong_reference_shifts_everything(run_exercise):
    out, _ = run_exercise("ex10_anticipation")
    first, second = out.splitlines()
    assert "k=-2: -0.31" in first and "k=-1:  0.31" in second

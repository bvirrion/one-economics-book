def test_ex07_three_periods(run_exercise):
    out, _ = run_exercise("ex07_feldstein_horioka")
    slopes = [float(line.split("slope ")[1].split()[0]) for line in out.splitlines()]
    assert len(slopes) == 3 and all(-0.5 < s < 1.2 for s in slopes)


def test_ex12_reversals_found(run_exercise):
    out, _ = run_exercise("ex12_reversals")
    assert int(out.splitlines()[0].split()[1]) > 20

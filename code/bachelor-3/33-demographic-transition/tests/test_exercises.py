def test_ex07_slope_negative_both_years(run_exercise):
    out, _ = run_exercise("ex07_fertility_income")
    slopes = [float(x.split("slope")[1].split()[0]) for x in out.splitlines()]
    assert len(slopes) == 2 and all(b < 0 for b in slopes)


def test_ex11_eleven_half_centuries(run_exercise):
    out, _ = run_exercise("ex11_half_centuries")
    lines = out.splitlines()
    assert len(lines) == 12 and lines[-1].endswith("1750")

def test_ex08_peaks_in_2022(run_exercise):
    out, _ = run_exercise("ex08_inflation_peaks")
    lines = out.splitlines()
    assert len(lines) == 2 and all("/2022" in line.split(";")[0] for line in lines)

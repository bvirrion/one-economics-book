def test_ex06_three_lines(run_exercise):
    out, _ = run_exercise("ex06_oaxaca")
    assert len(out.splitlines()) == 3


def test_ex12_composition(run_exercise):
    out, _ = run_exercise("ex12_mariel")
    raw = float(out.splitlines()[0].split(":")[1])
    within = float(out.splitlines()[1].split(":")[1])
    assert raw < -0.05 and abs(within) < 0.05

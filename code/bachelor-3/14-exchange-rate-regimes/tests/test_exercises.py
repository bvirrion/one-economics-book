def test_ex05_four_eras(run_exercise):
    out, _ = run_exercise("ex05_trilemma")
    assert len(out.splitlines()) == 4


def test_ex08_greece_above(run_exercise):
    out, _ = run_exercise("ex08_greece_germany")
    assert float(out.splitlines()[-1].split()[2]) > 0

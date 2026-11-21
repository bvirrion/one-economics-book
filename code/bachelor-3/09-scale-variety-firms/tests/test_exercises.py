def test_ex07_cutoff_matches_formula(run_exercise):
    out, _ = run_exercise("ex07_cutoff")
    first = out.splitlines()[0].split()
    assert abs(float(first[4].rstrip(",")) - float(first[-1])) < 0.01


def test_ex11_productivity_rises(run_exercise):
    out, _ = run_exercise("ex11_industry_productivity")
    line = out.splitlines()[1]
    closed = float(line.split("closed ")[1].split(",")[0])
    opened = float(line.split("open ")[1].split()[0])
    assert opened > closed

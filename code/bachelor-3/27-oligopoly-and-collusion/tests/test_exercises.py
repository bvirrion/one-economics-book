def test_ex08_five_thresholds(run_exercise):
    out, _ = run_exercise("ex08_thresholds")
    per = [float(line.split()[-1]) for line in out.splitlines()]
    assert len(per) == 5 and per[1] > per[0]


def test_ex11_closer_rival_matters_more(run_exercise):
    out, _ = run_exercise("ex11_pairs")
    rises = [float(line.split("=")[-1]) for line in out.splitlines()[1:]]
    assert rises[0] > rises[1] > 0

def test_ex05_five_each_way(run_exercise):
    out, _ = run_exercise("ex05_ranks")
    lines = out.splitlines()
    assert sum(x.startswith("rise") for x in lines) == 5
    assert sum(x.startswith("fall") for x in lines) == 5


def test_ex11_longer_lived_countries_gain_with_kappa(run_exercise):
    out, _ = run_exercise("ex11_kappa")
    rows = {
        x.split()[0]: [float(v) for v in x.split()[1:]] for x in out.splitlines()[1:]
    }
    # Japan outlives the U.S., India does not: kappa raises one and lowers the other
    assert rows["JPN"][0] < rows["JPN"][2] and rows["IND"][0] > rows["IND"][2]

def test_ex06_two_stable_matchings(run_exercise):
    out, _ = run_exercise("ex06_deferred")
    a, b = out.splitlines()
    # by hand: pupils proposing give p1-A, p2-B, p3-D, p4-C; schools proposing
    # give p1-B, p2-A, p3-D, p4-C
    assert "'p1': 'A', 'p2': 'B', 'p3': 'D', 'p4': 'C'" in a
    assert "'p1': 'B', 'p2': 'A', 'p3': 'D', 'p4': 'C'" in b


def test_ex11_first_price_above_second(run_exercise):
    out, _ = run_exercise("ex11_risk")
    rev = [float(line.split()[-1]) for line in out.splitlines()]
    # by hand: E[second highest of 4] = 3/5; first-price 3/3.5 x 4/5 = 0.686
    assert abs(rev[0] - 0.6) < 0.005 and abs(rev[2] - 0.6857) < 0.005

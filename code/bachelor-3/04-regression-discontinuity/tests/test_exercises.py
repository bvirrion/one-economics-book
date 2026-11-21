def test_ex05_high_order_polynomials_are_noisier(run_exercise):
    out, _ = run_exercise("ex05_global_polynomial")
    sd = {line[:18].strip(): float(line.split()[-1]) for line in out.splitlines()[1:]}
    assert sd["poly 6"] > 2 * sd["local linear 0.25"]


def test_ex08_donut_moves_toward_the_truth(run_exercise):
    out, _ = run_exercise("ex08_donut")
    j = [float(line.split("jump")[1].split()[0]) for line in out.splitlines()]
    assert abs(j[1] - 0.10) < abs(j[0] - 0.10)


def test_ex11_coverage_collapses_for_wide_windows(run_exercise):
    out, _ = run_exercise("ex11_coverage")
    cov = [float(line.split()[-1]) for line in out.splitlines()]
    assert cov[0] > 0.9 and cov[-1] < 0.5

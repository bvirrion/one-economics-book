def test_ex11_bias_up(run_exercise):
    out, _ = run_exercise("ex11_hedonic")
    a, b = (float(line.split()[-2]) for line in out.splitlines())
    assert abs(a - 6.0) < 1.5 and b > 2 * a

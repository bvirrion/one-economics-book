def test_ex05_float_shorter(run_exercise):
    out, _ = run_exercise("ex05_half_lives")
    last = out.splitlines()[-1]
    a = float(last.split("half-life: ")[1].split()[0])
    b = float(last.split("years (1870-2020), ")[1].split()[0])
    assert b < a


def test_ex08_mean_slope_below_one(run_exercise):
    out, _ = run_exercise("ex08_uip_by_country")
    assert float(out.splitlines()[-1].split()[2].rstrip(";")) < 1

def test_sharp_estimates_near_the_calibration_and_balance_holds(run):
    out, r = run("rd_sharp")
    rows = [line.split() for line in out.splitlines()[2:5]]
    for _h, jump, se, _ in rows:
        assert abs(float(jump) - 0.077) < 3 * float(se)
    assert float(r["difference of means within 0.05:"]) > 0.09
    bal = out.splitlines()[-1].split()
    assert abs(float(bal[-3])) < 2 * float(bal[-1].strip(")"))


def test_bandwidth_tradeoff(run):
    out, _ = run("rd_bandwidth")
    rows = [line.split() for line in out.splitlines()[1:]]
    const = [float(x[2]) for x in rows if x[0] == "constant"]
    lin_sd = [float(x[3]) for x in rows if x[0] == "linear"]
    assert const == sorted(const) and lin_sd == sorted(lin_sd, reverse=True)


def test_fuzzy_is_the_wald_ratio(run):
    out, _ = run("rd_fuzzy")
    lines = out.splitlines()
    first = float(lines[1].split()[-3])
    reduced = float(lines[2].split()[-3])
    wald = float(lines[3].split()[-1])
    assert abs(reduced / first - wald) < 0.002 and abs(wald + 0.25) < 0.1


def test_density_test_flags_only_the_remarked(run):
    out, _ = run("density_test")
    t = [float(line.split()[-1]) for line in out.splitlines()[1:]]
    assert abs(t[0]) < 2 and t[1] > 10

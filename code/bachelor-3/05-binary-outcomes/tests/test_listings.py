def test_ames_of_logit_and_probit_agree(run):
    out, _ = run("lpm_logit_probit")
    for line in out.splitlines()[2:6]:
        f = line.split()
        assert abs(float(f[-2]) - float(f[-1])) < 0.01
    assert "LPM fitted values above 1" in out


def test_newton_matches_statsmodels(run):
    out, _ = run("newton_logit")
    lines = out.splitlines()
    last = [x for x in lines if x.startswith("step")][-1].split()
    sm = [x for x in lines if x.startswith("statsmodels")][0].split()
    assert last[3] == sm[1] and last[-1] == sm[-1]
    se = lines[-1].replace(",", "").split()
    assert se[6] == se[8]


def test_mode_choice_value_of_time_and_iia(run):
    out, _ = run("travel_mode")
    assert "17.2 dollars an hour" in out
    lines = out.splitlines()
    actual = lines[-3].split("[")[1].split("]")[0].split()
    fitted = lines[-2].split("[")[1].split("]")[0].split()
    assert actual == fitted                      # logit matches shares by mode


def test_log_share_inversion_recovers_price_coefficient(run):
    out, _ = run("logit_demand")
    est = float(out.splitlines()[0].split("estimated")[1].split()[0])
    assert abs(est + 2) < 0.15

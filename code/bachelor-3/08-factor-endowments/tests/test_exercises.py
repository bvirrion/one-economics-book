def test_ex08(run_exercise):
    out, _ = run_exercise("ex08_factor_content")
    assert "capital 22.0" in out and "labour -24.0" in out


def test_ex11_signs(run_exercise):
    out, _ = run_exercise("ex11_hov_sign")
    lines = out.splitlines()
    assert "sign matches 1.00" in lines[0] and "slope of measured on predicted 1.00" in lines[0]
    assert "slope of measured on predicted 0.20" in lines[1]

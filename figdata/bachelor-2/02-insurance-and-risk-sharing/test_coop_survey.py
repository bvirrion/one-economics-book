from make_coop_survey import KEPT, regression


def test_regression_recovers_the_kept_share():
    reg, meta = regression()
    r = reg.set_index("term")
    assert meta.observations[0] == 700
    assert abs(r.coef["dlnm"] - KEPT) < 3 * r.se["dlnm"]
    # a household keeping KEPT of its own shocks moves 1 - KEPT with the average
    assert abs(r.coef["dlncbar"] - (1 - KEPT)) < 3 * r.se["dlncbar"]
    assert (1 - r.coef["dlncbar"]) / r.se["dlncbar"] > 3  # beta_1 = 1 is rejected
    assert r.t["dlnm"] > 5  # full sharing (b2 = 0) is rejected

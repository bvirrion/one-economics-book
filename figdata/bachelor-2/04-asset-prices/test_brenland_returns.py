from make_brenland_returns import predict, returns


def test_sixty_years():
    r = returns()
    assert len(r) == 60 and r.year.iloc[-1] == 2024


def test_no_predictability_detected():
    p = predict().iloc[0]
    assert abs(p.t) < 1.96 and p.n_up + p.n_down == 59

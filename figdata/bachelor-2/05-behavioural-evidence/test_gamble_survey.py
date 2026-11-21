from make_gamble_survey import summary, survey


def test_acceptance_rises_with_the_gain():
    s = survey()
    assert s.accept.is_monotonic_increasing and s.accept.iloc[-1] > 90


def test_median_near_two():
    m = summary().iloc[0]
    assert 175 <= m.median_switch <= 225

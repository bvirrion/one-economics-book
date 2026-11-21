from make_scarcity import facts, hours_income, meals_away


def test_hours_income():
    h = hours_income()
    assert len(h) >= 100 and h.hours.between(1000, 3000).all()
    f = facts().set_index("name").value
    assert f.hours_richest_third_median < f.hours_poorest_third_median


def test_meals_away_rises():
    m = meals_away()
    assert m.away_share.is_monotonic_increasing and (m.away < m.food).all()

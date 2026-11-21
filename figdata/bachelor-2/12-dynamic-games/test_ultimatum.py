from make_ultimatum import summary, table


def test_range():
    s = summary().iloc[0]
    assert (s.lowest, s.highest, s.groups) == (26.0, 58.0, 18)
    assert s.zero_rejection == 3 and s["median"] == 40.5


def test_every_offer_above_quarter():
    assert (table().offer > 25).all()

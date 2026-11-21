from make_bids import summary, table


def test_counts():
    s = summary().iloc[0]
    assert (s.above3, s.above6, s.at6, s.below6) == (18, 14, 1, 3)


def test_slopes_bracket_prediction():
    t = table()
    assert (t.slope3 > 2 / 3).all()
    assert round(t.slope6.min(), 3) == 0.787

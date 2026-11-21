from make_returns import summary, table


def test_returns_fall_with_odds():
    r = table()["return"].tolist()
    assert r == sorted(r, reverse=True)


def test_summary():
    s = summary().iloc[0]
    assert s.gap == 55.5
    assert s.payback_favourite == 0.945 and s.payback_longest == 0.39

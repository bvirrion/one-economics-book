from make_cartels import summary, table


def test_summary():
    s = summary().iloc[0]
    assert (s.lowest, s.highest, s["median"], s.longest, s.with_range) == (
        3.7,
        10.0,
        5.3,
        29.0,
        6,
    )


def test_ranges_contain_mean():
    t = table()
    assert len(t) == 9 and (t.minus >= 0).all() and (t["plus"] >= 0).all()

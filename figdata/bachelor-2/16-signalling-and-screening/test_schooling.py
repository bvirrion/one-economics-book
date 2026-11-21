from make_schooling import summary, table


def test_sample():
    t = table()
    assert t.n.sum() == 15992
    assert t.education.min() == 0 and t.education.max() == 18


def test_jumps():
    s = summary().iloc[0]
    assert (s.jump12, s.jump16) == (4.81, 3.51)
    assert s.max_other == 1.17
    assert (s.dollars11, s.dollars12, s.dollars15, s.dollars16) == (
        9903,
        14715,
        12749,
        16256,
    )


def test_topcode():
    s = summary().iloc[0]
    assert (s.topcode, s.n_top, s.n_zero) == (25243.6, 3007, 1748)

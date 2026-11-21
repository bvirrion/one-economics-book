from make_coal import summary, table


def test_shares_add_to_about_100():
    assert summary().iloc[0].max_rounding <= 0.5


def test_nonstate_rises_every_year():
    s = table().nonstate.tolist()
    assert all(b > a for a, b in zip(s, s[1:]))


def test_changes():
    s = summary().iloc[0]
    assert s.nonstate_change == 10.6 and s.central_change == -7.0

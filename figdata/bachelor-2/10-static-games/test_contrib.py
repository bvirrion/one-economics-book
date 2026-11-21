from make_contrib import summary, table


def test_shares():
    s = summary().iloc[0]
    assert (s.strangers_all, s.strangers_final) == (18.5, 9.5)
    assert (s.partners_all, s.partners_final) == (37.5, 16.0)
    assert s.largest == 91.0


def test_punishment_raises_contributions():
    d = table()
    assert (d["all"].iloc[1::2].values > d["all"].iloc[0::2].values).all()

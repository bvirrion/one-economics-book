from make_randhie import summary as hie
from make_randhie import table as hie_table
from make_safelite import summary, table


def test_safelite():
    assert list(table().pct) == [20, 44, 22]
    s = summary().iloc[0]
    assert (s["between"], s.within_share) == (22, 0.5)


def test_randhie():
    s = hie().iloc[0]
    assert (s.free, s.c25, s.c50, s.c95, s.n) == (3.555, 2.787, 2.561, 2.112, 14941)
    assert s.fall_pct == 40.6
    t = hie_table()
    assert (t["mean"].diff().dropna() < 0).all()

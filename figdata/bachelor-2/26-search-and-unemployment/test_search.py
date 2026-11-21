from make_search import bev_summary, beveridge


def test_beveridge():
    d = beveridge()
    assert len(d) == 68
    assert (d.u.max(), d.v.max(), d.u.min()) == (12.3, 3.3, 6.2)


def test_points():
    s = bev_summary().set_index("time")
    assert (s.loc["2013-Q1", "u"], s.loc["2013-Q1", "v"]) == (12.3, 1.3)
    assert (s.loc["2022-Q2", "u"], s.loc["2022-Q2", "v"]) == (6.7, 3.3)
    assert (s.loc["2019-Q4", "theta"], s.loc["2022-Q2", "theta"]) == (0.311, 0.493)

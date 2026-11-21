from make_olg import eff_summary, oadr_summary


def test_oadr():
    s = oadr_summary().set_index("iso3")
    assert list(s.y1960) == [8.9, 14.5, 5.6, 14.7, 6.0, 8.6]
    assert list(s.y2025) == [51.0, 39.7, 29.3, 28.5, 5.4, 16.0]


def test_efficiency():
    s = eff_summary().iloc[0]
    assert (s.n, s.n_above, s.below) == (129, 128, "CHN")
    assert (s.median_cap, s.median_inv) == (47.8, 23.0)
    assert (s.chn_cap, s.chn_inv, s.usa_cap, s.usa_inv) == (42.2, 42.7, 40.8, 21.7)


def test_efficiency_by_hand():
    # both flows at national prices: recount from the two sources directly
    from econdata import pwt, wdi

    p = pwt(since=2019, until=2019).set_index("iso3").labsh.dropna()
    w = wdi("NE.GDI.TOTL.ZS", since=2019, until=2019).set_index("iso3").value.dropna()
    common = p.index.intersection(w.index)
    above = sum(100 * (1 - p[c]) > w[c] for c in common)
    assert (len(common), above) == (129, 128)

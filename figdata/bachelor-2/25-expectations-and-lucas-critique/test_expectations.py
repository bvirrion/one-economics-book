from make_expectations import cbi, cbi_fit, it_event, phillips_dec


def test_cbi():
    d = cbi().set_index("iso3")
    assert len(d) == 15
    assert (d.loc["ESP", "infl"], d.loc["DEU", "infl"]) == (9.95, 3.19)
    f = cbi_fit().iloc[0]
    assert (f.slope, f.intercept, f["corr"]) == (-1.83, 10.29, -0.8)
    assert d.loc["USA", "infl"] == 4.51


def test_phillips():
    p = phillips_dec().set_index("decade")
    assert (p.loc[1960, "infl"], p.loc[1970, "infl"]) == (2.55, 7.22)
    assert (p.loc[1960, "unemp"], p.loc[1980, "unemp"]) == (4.78, 7.28)


def test_it_event():
    e = it_event().set_index("k")
    assert (e.loc[-5, "median"], e.loc[0, "median"], e.loc[10, "median"]) == (
        8.56,
        6.37,
        3.03,
    )
    assert e.n.min() == 27

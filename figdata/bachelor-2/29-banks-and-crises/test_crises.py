from make_crises import credit, decades, paths, paths_n


def test_decades():
    d = decades().set_index("decade").crises
    assert d.sum() == 88
    assert (d[1930], d[2000], d[1940] + d[1950] + d[1960]) == (14, 13, 0)


def test_paths():
    p = paths().set_index("h")
    assert list(p.financial) == [0, -2.95, -2.7, -1.53, 0.01, 1.28]
    assert list(p.normal) == [0, -2.18, -0.31, 1.62, 3.23, 4.89]
    n = paths_n().iloc[0]
    assert (n.n_financial, n.n_normal) == (88, 203)


def test_credit():
    c = credit().set_index("group")
    assert (c.loc[1, "mean"], c.loc[1, "median"], c.loc[1, "n"]) == (13.35, 10.55, 63)
    assert (c.loc[0, "mean"], c.loc[0, "median"], c.loc[0, "n"]) == (4.79, 4.41, 1861)

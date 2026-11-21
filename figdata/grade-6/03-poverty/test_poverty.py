from make_poverty import brenland, lines_2024, regions, ssa_count, world


def test_world():
    share, count = world()
    s = share.set_index("year").share
    assert s[1981] == 47.1 and s[2024] == 10.1 and 2019 not in s.index
    c = count.set_index("year")
    assert c.poor.idxmax() == 1993 and 2.3 < c.poor[1993] < 2.4
    assert 0.8 < c.poor[2024] < 0.85
    # WDI: the share jumps from 42.1 % (1988) to 43.6 % (1989), so the number above the line dips once
    # (2.963 -> 2.937 billion); everywhere else it rises. The number below the line rises with dips to 1993
    # (1986, 1988), falls after it, and rises again in 1997-1998 and in 2020.
    down = [y for y, d in c.not_poor.diff().items() if d < 0]
    assert down == [1989] and c.not_poor[2024] > 3 * c.not_poor[1981]
    up_after = [y for y, d in c.poor.loc[1994:].diff().items() if d > 0]
    assert up_after == [1997, 1998, 2020]


def test_regions():
    r = regions().set_index("year")
    assert r.loc[2024].drop("wld").idxmax() == "ssf"
    assert r.eas[1990] > 60 and r.eas[2024] < 3


def test_ssa():
    d = ssa_count().set_index("year")
    assert d.ssa_share_of_poor[2024] > 60 > d.ssa_share_of_poor[1990]


def test_brenland():
    basket, bands = brenland()
    assert round(basket.cost.sum(), 2) == 4442.92
    assert bands.households.sum() == 2000
    assert list(bands.people[:2]) == [387, 530]


def test_lines():
    d = lines_2024().set_index("line").share
    assert d["3.00"] == 10.1 and d["4.20"] == 18.2 and d["8.30"] == 46.2

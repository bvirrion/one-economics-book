from make_connected import brenland_trade, computer_prices, connections, facts, mobile_early, trade_share


def test_trade_share_waves():
    t = trade_share().set_index("year").jst_median
    assert t[1913] > t[1870] and t[1932] < t[1913] and t[2008] > t[1913]
    assert t.loc[1930:1950].min() < 0.5 * t[1913]


def test_world_series():
    w = trade_share().set_index("year").world.dropna()
    assert w.index.min() == 1970 and w.index.max() == 2024 and w[2009] < w[2008]


def test_connections_split():
    assert mobile_early().year.max() == 1999
    c = connections()
    assert c.year.min() == 2005 and c.isna().sum().sum() == 0


def test_computers_cheaper():
    p = computer_prices().set_index("year")["index"]
    assert p.iloc[0] == 100 and p[2025] < 10


def test_facts_call():
    f = facts().set_index("name").value
    assert f.call_1927_dollars == 75 and 1300 < f.call_1927_in_2025_dollars < 1500
    assert f.mobile_pass50_year == 2007 and f.singapore_trade_2024 > 100


def test_brenland_trade():
    b = brenland_trade()
    assert (b.share > 60).all() and (b.to_kestria < b.exports).all()

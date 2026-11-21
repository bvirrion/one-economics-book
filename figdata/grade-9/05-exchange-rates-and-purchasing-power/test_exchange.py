from make_exchange import market_vs_ppp, price_level_income


def test_us_equal_and_poor_gain():
    m = market_vs_ppp().set_index("iso3")
    assert m.market["USA"] == m.ppp["USA"]
    assert m.ppp["ETH"] > 2 * m.market["ETH"] and m.ppp["CHE"] < m.market["CHE"]


def test_price_level_rises_with_income():
    d = price_level_income()
    assert d[d.income < 5000].pli.median() < d[d.income > 50000].pli.median() / 2
    assert len(d) > 150


def test_sorted_by_market():
    m = market_vs_ppp()
    assert list(m.market) == sorted(m.market, reverse=True)

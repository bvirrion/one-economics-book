from make_money import accounts, barter


def test_accounts_rose():
    a = accounts()
    assert len(a) == 11 and (a.y2024 > a.y2011).all()
    assert a.set_index("iso3").y2024["WLD"] > 75


def test_barter_rates():
    b = barter().set_index("goods")
    assert b.rates[4] == 6 and b.rates[10] == 45

from make_competition import ferry, juice, telecom


def test_monopoly_price():
    j = juice().set_index("price")
    assert j.profit.idxmax() == 3.0 and j.cups[3.0] == 400


def test_ferry():
    f = ferry().set_index("fare")
    assert f.profit_alone.idxmax() == 30 and f.profit_each_of_two[20] == 500 and f.profit_each_of_two[15] < 0


def test_telecom_fall():
    t = telecom().set_index("year")
    assert (t.loc[2025] < 45).all()

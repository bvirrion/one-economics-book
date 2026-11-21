from make_institutions import bribery_income, koreas, valleys


def test_koreas_gap_and_values():
    k = koreas().set_index("year")
    assert (k.south[2022], k.north[2022], k.north[1940], k.south[1940]) == (41321, 1569, 2624, 1975)
    assert k.north.loc[1944:1989].isna().all()


def test_bribery_falls_with_income():
    d = bribery_income()
    assert d[d.income < 5000].bribery.median() > d[d.income > 30000].bribery.median()


def test_valleys():
    v = valleys().set_index("year")
    assert v.a[20] == 1806 and v.b[20] == 1220

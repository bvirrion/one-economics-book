from make_light import table


def test_light():
    d = table()
    assert list(d.year) == sorted(d.year)
    assert d.hours.iloc[0] == 5.37 and d.hours.iloc[-1] == 0.000119
    assert 40000 < d.hours.iloc[0] / d.hours.iloc[-1] < 50000

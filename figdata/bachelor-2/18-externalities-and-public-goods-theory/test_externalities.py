from make_allowance import table as allowance
from make_so2 import summary, table


def test_so2():
    t = table()
    assert t.year.min() == 1970
    s = summary().iloc[0]
    assert s["last"] == 2023
    assert (s.power_1980, s.power_1990, s.power_2000, s.power_2010) == (
        15.85,
        14.76,
        11.17,
        4.88,
    )
    assert (s.power_last, s.total_last, s.power_fall_pct) == (0.79, 1.49, 95)


def test_allowance():
    a = allowance()
    assert list(a.price) == [273.0, 703.0, 390.0, 70.0, 0.56]

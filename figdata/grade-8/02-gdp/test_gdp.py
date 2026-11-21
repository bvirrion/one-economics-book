from country import load

from make_gdp import brenland_gdp, largest


def test_largest():
    t = largest()
    assert len(t) == 10 and t.total.is_monotonic_decreasing and t.iso3.iloc[0] == "CHN"


def test_brenland_adds_up():
    a = load("accounts").set_index("year").loc[2025]
    assert brenland_gdp().value.sum() == a.gdp

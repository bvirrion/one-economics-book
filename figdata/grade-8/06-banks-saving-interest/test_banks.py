from make_banks import brenland, facts, us_real


def test_long_above_short_most_years():
    f = facts().set_index("name").value
    assert f["spread_positive"] / f["spread_years"] > 0.6


def test_us_real_signs():
    r = us_real().set_index("year")
    assert r.real[1975] < 0 < r.real[1981]


def test_brenland_2022():
    b = brenland().set_index("year")
    assert b.inflation[2022] == 10.2 and b.rate_minus_inflation[2022] < 0

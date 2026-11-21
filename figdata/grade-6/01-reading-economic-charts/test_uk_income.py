from make_uk_income import table


def test_years_and_values():
    d = table().set_index("year")
    assert d.index.min() == 1820 and d.index.max() == 2022
    assert 3000 < d.gdppc[1820] < 3600
    assert d.gdppc[2022] > 10 * d.gdppc[1820]


def test_quoted_values():
    # values quoted in the chapter and its exercises (figdata: uk_income)
    d = table().set_index("year")
    assert d.gdppc[1950] == 11061 and d.gdppc[2000] == 31946

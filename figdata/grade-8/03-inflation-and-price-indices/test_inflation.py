from country import load

from make_inflation import basket, facts, germany


def test_basket_matches_cpi():
    b = basket()
    a = load("accounts").set_index("year")
    assert round(100 * b.c2025.sum() / b.c2015.sum(), 1) == a.cpi[2025]
    assert round(100 * b.c2024.sum() / b.c2015.sum(), 1) == a.cpi[2024]


def test_germany_eleven_powers():
    g = germany().set_index("year").level
    assert 1e11 < g[1923] < 1e12


def test_us_2022():
    f = facts().set_index("name").value
    assert 7.5 < f.us_inf_2022 < 8.5

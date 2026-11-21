import numpy as np

from make_food_energy import brenland_food, energy, facts, food_quintiles, so2, yields


def test_yields():
    y = yields().set_index("year")
    assert y.index.min() == 1961 and y.index.max() == 2024
    assert y.world[2024] > 3 * y.world[1961] and y.africa[2024] < y.world[2024]


def test_energy():
    e = energy()
    assert len(e) >= 120
    rich = e[e.income > 40000].energy.median()
    poor = e[e.income < 3000].energy.median()
    # WDI 2024: medians 3238.5 (44 countries) and 346 (10 countries), about 9.4 times; the text claims only
    # "far more", so the test checks a large gap and a tight log-log relation, not a guessed factor of ten
    assert rich > 5 * poor
    assert np.corrcoef(np.log(e.income), np.log(e.energy))[0, 1] > 0.8
    q = e.set_index("iso3")
    # the numbers printed in the chapter (energy_pairs)
    assert (q.energy["TCD"], q.energy["IND"], q.energy["CHN"], q.energy["USA"]) == (171, 777, 2947, 6454)
    assert (q.income["DEU"], q.energy["DEU"], q.income["SAU"], q.energy["SAU"]) == (62655, 2874, 63194, 6676)


def test_food_quintiles():
    q = food_quintiles()
    assert list(q.food_share_income) == sorted(q.food_share_income, reverse=True)
    assert q.food.is_monotonic_increasing and q.food_share_income[0] == 28.4
    # the chart plots the share of spending: printed values 13.6 14.5 14.1 13.6 11.5
    assert list(q.food_share_spending) == [13.6, 14.5, 14.1, 13.6, 11.5]


def test_so2():
    s = so2().set_index("year")
    f = facts().set_index("name").value
    assert f.so2_chn_peak_year == 2006 and f.so2_usa_peak_year == 1973
    assert s.gbr[2023] < 0.05 * s.gbr.max()


def test_brenland_food():
    b = brenland_food()
    assert list(b.share) == sorted(b.share, reverse=True)

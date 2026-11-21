from make_health import child_mortality, facts, fertility, life_expectancy, pairs


def test_life_expectancy():
    d = life_expectancy().set_index("year")
    assert d.index.min() == 1800 and d.index.max() == 2024
    assert not any(1950 <= y < 1960 for y in d.index)
    assert d.loc[1800].max() < 35 and d.loc[2024].min() > 60
    assert d.world[1918] < d.world[1917] - 10                       # the 1918 pandemic
    assert d.world[1800] == 30.6 and d.world[2024] == 73.5


def test_child_mortality():
    d = child_mortality()
    assert len(d) >= 120
    rich = d[d.income > 40000].mortality.median()
    poor = d[d.income < 3000].mortality.median()
    assert poor > 10 * rich
    p = pairs(d)
    assert len(p) == 2 and (p.high_mort / p.low_mort).min() > 5
    assert ((p.high_income / p.low_income) - 1).abs().max() < 0.1


def test_fertility():
    f = fertility().set_index("year")
    assert f.wld[1960] > 4.5 and f.wld[2024] < 2.3
    assert f.wld[f.wld < 3].index[0] == 1993
    assert f.loc[2024].idxmax() == "ssf" and f.ssf[2024] > 4


def test_facts():
    d = facts().set_index("name").value
    assert d.urban_1960 == 34.2 and d.urban_2025 == 57.8 and d.old_dep_2024 == 15.7

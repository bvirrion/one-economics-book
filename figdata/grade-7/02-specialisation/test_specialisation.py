from make_specialisation import facts, farm_share_income, people_per_farmer


def test_farm_share_falls_with_income():
    f = facts().set_index("name").value
    assert f.farm_median_below_5000 > 10 * f.farm_median_above_40000
    assert len(farm_share_income()) >= 150


def test_people_per_farmer():
    p = people_per_farmer().set_index("year")
    assert p.index.min() == 1991 and p.index.max() == 2024
    assert p.isna().sum().sum() == 0
    assert (p.loc[2024] > p.loc[1991]).all()
    assert p.loc[2024].usa > 10 * p.loc[2024].ind

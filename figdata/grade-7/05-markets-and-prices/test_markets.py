from make_markets import black_sea_wheat, eggs, facts, split_eggs


def test_wheat_2010_drop():
    w = black_sea_wheat().set_index("year")
    assert w.rus[2010] < 0.75 * w.rus[2009] and w.world[2010] < w.world[2009]


def test_eggs_split_and_peaks():
    a, b = split_eggs()
    assert len(a) + len(b) == len(eggs())
    f = facts().set_index("name").value
    assert f.eggs_2023_01 > 2 * f.eggs_2021_12 and f.eggs_2023_08 < 0.5 * f.eggs_2023_01
    assert f.eggs_peak_year == 2025

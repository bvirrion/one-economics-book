import math

from make_distribution import TOWN, brenland_fifths, fifths, world_distribution, world_tables


def test_fifths_sum_to_100():
    assert abs(sum(fifths(range(1, 101))) - 100) < 0.3
    b = brenland_fifths()
    assert abs(b.gross.sum() - 100) < 0.3 and abs(b.disposable.sum() - 100) < 0.3
    assert b.disposable.iloc[4] < b.gross.iloc[4] and b.disposable.iloc[0] > b.gross.iloc[0]
    assert sum(TOWN) == 100


def test_world_coverage_and_shift():
    _, cover = world_tables()
    assert cover[1990] > 0.7 and cover[2019] > 0.8
    w = world_distribution()
    assert w.y2019.sum() > w.y1990.sum()
    # the 2019 mass sits further right than the 1990 mass
    m90 = (w.logmid * w.y1990).sum() / w.y1990.sum()
    m19 = (w.logmid * w.y2019).sum() / w.y2019.sum()
    assert m19 > m90 + 0.2

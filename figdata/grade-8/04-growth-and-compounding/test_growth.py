from make_growth import neighbours, speeds


def test_selection_rule():
    s = speeds().set_index("role")
    assert abs(s.growth["slow"] - 1) < 0.5 and abs(s.growth["mid"] - 2) < 0.3 and abs(s.growth["fast"] - 6) < 0.6


def test_neighbours_ends():
    n = neighbours().set_index("year")
    assert n.kestria[2000] == 10400 and n.kestria[2025] == 27700
    assert n.brenland[2025] > n.brenland[2000]

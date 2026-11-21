from make_serves import summary, table


def test_recomputed_rates_match_printed():
    assert summary().iloc[0].max_printed_gap <= 0.006


def test_totals():
    s = summary().iloc[0]
    assert s.games == 40 and s.p05 == 1 and s.p10 == 2
    assert round(s.overall_l, 2) == 0.64 and round(s.overall_r, 2) == 0.65


def test_serves_total():
    assert table().serves.sum() == 3026

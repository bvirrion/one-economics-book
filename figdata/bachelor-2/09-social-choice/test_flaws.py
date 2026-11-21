from make_flaws import summary, table


def test_no_winner_share():
    assert summary().iloc[0].no_winner == 0.55


def test_all_rates_small():
    d = table()
    assert len(d) == 7 and d.rate.max() == 3.8 and (d.rate < 5).all()

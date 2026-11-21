from make_ce_age import summary, table


def test_seven_groups_and_the_hump():
    t = table()
    assert len(t) == 7
    assert t.income_after.idxmax() == 3 and t.spending.idxmax() == 3


def test_spending_is_flatter_than_income():
    s = summary().iloc[0]
    assert s.peak_spending_ratio < s.peak_income_ratio


def test_the_oldest_spend_about_their_income():
    t = table()
    assert t.ratio.iloc[-1] > 1.0 > t.ratio.iloc[3]

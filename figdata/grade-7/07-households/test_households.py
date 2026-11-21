from make_households import budget_shares, engel_quarters, income_sources, problem_rows


def test_shares_pattern():
    b = budget_shares()
    assert b.housing.iloc[0] > b.housing.iloc[4] and b.insurance.iloc[4] > 5 * b.insurance.iloc[0]
    s = income_sources().set_index("group")
    assert (abs(s.sum(axis=1) - 100) < 0.5).all()
    assert s.wages["Highest"] > 2 * s.wages["Lowest"] and s.retirement["Lowest"] > 50


def test_engel_brenland():
    q = engel_quarters()
    assert q.share.is_monotonic_decreasing and q.food.is_monotonic_increasing


def test_problem_rows_identity():
    p = problem_rows()
    assert (p.gross - p.tax + p.transfers == p.disposable).all()
    assert (p.disposable - p.consumption == p.saving).all()

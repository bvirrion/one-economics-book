from make_allais import table


def test_two_pairs_from_the_article():
    t = table().set_index("pos")
    assert list(t.index) == [1, 2]
    assert t.certain.tolist() == [82, 80] and t.scaled.tolist() == [17, 35]
    assert t.n.tolist() == [72, 95]


def test_expected_utility_is_broken_by_a_majority_in_each_pair():
    # A respondent obeying expected utility picks the less risky option in both
    # problems or in neither,
    # so at least certain - scaled percent of respondents broke it.
    t = table()
    assert (t.gap > 40).all()
    assert t.gap.tolist() == [65, 45]

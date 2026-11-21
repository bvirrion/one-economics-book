from make_annuities import summary, table


def test_multiples():
    s = summary().iloc[0]
    assert (s.escalating_vs_male, s.indexed_vs_male) == (3.5, 4.2)


def test_signs():
    t = table().set_index("feature")
    assert t.loc["Escalating", "voluntary"] == -15.2
    assert t.loc["Guaranteed", "voluntary"] == 4.6

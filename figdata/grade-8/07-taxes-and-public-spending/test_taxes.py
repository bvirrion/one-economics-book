from make_taxes import budget, tax


def test_tax_bands():
    assert tax(12_000) == 0 and tax(30_000) == 3_600 and tax(60_000) == 12_600


def test_debt_identity():
    b = budget().set_index("year")
    assert (b.debt.diff().dropna() == b.deficit.loc[2015:]).all()

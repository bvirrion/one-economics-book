from make_ck import tables


def test_did_matches_the_printed_difference():
    _, s = tables()
    v = dict(zip(s.stat, s.value))
    assert v["change_pa"] == -2.16 and v["change_nj"] == 0.59
    assert v["did"] == 2.75          # the table prints 2.76 from unrounded means
    assert v["cf_nov"] == 18.28

from make_smith import summary, table, wide


def test_table_one():
    d = table()
    t1 = d[d.test == "T1"]
    assert t1.pbar.tolist() == [1.8, 1.86, 2.02, 2.03, 2.03] and t1.period.max() == 5
    assert d[d.test == "T7"].alpha.tolist() == [49.1, 22.2, 7.1, 5.4, 3.0, 2.7]


def test_convergence():
    s = summary().iloc[0]
    assert s.n_tests == 10 and s.t6a_first < 50 and 99 < s.t6a_last < 102
    assert s.share_alpha_fell > 80


def test_wide_shape():
    w = wide("ratio")
    assert list(w.columns)[0] == "period" and len(w) == 6

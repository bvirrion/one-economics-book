from make_replication import split, summary, table


def test_counts_match_the_paper():
    s = summary().iloc[0]
    assert s.n == 18 and s.n_replicated == 11
    assert abs(s.mean_orig - 0.474) < 0.005 and abs(s.mean_rep - 0.279) < 0.005


def test_split_is_complete():
    yes, no = split()
    assert len(yes) + len(no) == len(table())

from make_gap import summary, table


def test_parts_add_up():
    s = summary().iloc[0]
    assert s.max_rounding <= 0.06


def test_paper_summary():
    s = summary().iloc[0]
    assert s.fall == 8.1 and s.share_transport == 28
    assert table().residual.iloc[-1] < table().residual.iloc[0] / 2

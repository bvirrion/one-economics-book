from make_event_study import table


def test_leads_flat_and_lags_track_the_truth():
    t = table().set_index("k")
    for k in (-5, -4, -3, -2):
        assert t.lo[k] < 0 < t.hi[k]
    for k in range(6):
        assert abs(t.est[k] - t.true[k]) < 0.15
    assert t.est[-1] == 0.0

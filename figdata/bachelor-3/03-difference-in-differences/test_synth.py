from make_synth import tables


def test_matches_the_listing_and_fits_before():
    chart, s = tables()
    v = dict(zip(s.stat, s.value))
    assert round(v["rmspe_pre"], 3) == 0.258      # synth_demo.py prints 0.258
    assert round(v["gap_post"], 3) == -1.681      # and -1.681
    assert len(chart) == 30

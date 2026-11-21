from make_brenland_age import bands, fit


def test_six_bands_cover_the_survey():
    t = bands()
    assert len(t) == 6 and t.n.sum() == 2000


def test_consumption_tracks_income():
    f = fit().iloc[0]
    assert 0.7 < f.slope < 0.9

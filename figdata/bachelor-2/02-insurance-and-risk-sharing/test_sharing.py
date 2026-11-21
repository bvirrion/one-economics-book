from make_sharing import tables


def test_country_count_and_coverage():
    vol, cor, summ = tables()
    assert len(vol) == len(cor) == summ.n[0]
    assert 110 <= len(vol) <= 140
    assert "WLD" not in set(vol.iso3) and "USA" in set(vol.iso3)


def test_most_countries_fail_the_full_sharing_predictions():
    _, _, s = tables()
    # full international risk sharing: consumption smoother than output, and more
    # correlated with the world; most countries show the opposite on both counts
    assert s.share_ratio_above_1[0] > 60 and s.median_ratio[0] > 1
    assert s.share_cons_corr_below_gdp[0] > 60
    assert s.median_corr_cons[0] < s.median_corr_gdp[0]


def test_known_values():
    vol, _, _ = tables()
    v = vol.set_index("iso3")
    assert abs(v.sd_gdp["USA"] - 1.76) < 0.01 and abs(v.sd_cons["USA"] - 1.97) < 0.01
    assert v.ratio["JPN"] < 1 < v.ratio["KOR"]

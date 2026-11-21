from make_trade import korea_mix, tariff_example, tariffs


def test_korea_mix():
    k = korea_mix().set_index("group")
    assert k.y1965["Manufactures"] == 59.3 and k.y2024["Manufactures"] == 87.3
    assert 95 < k.y1965.sum() <= 100.5 and 95 < k.y2024.sum() <= 100.5


def test_tariff_example():
    e = tariff_example()
    assert (e["qd0"], e["qs0"], e["m0"]) == (70, 20, 50)
    assert (e["qd1"], e["qs1"], e["m1"], e["revenue"]) == (60, 30, 30, 60)
    # every extra dalen buyers pay on the units they still buy goes to home producers or the state
    assert e["buyers_extra"] == e["producers_extra"] + e["revenue"] == 120


def test_tariffs_fall():
    t = tariffs().set_index("year")
    for c in ["USA", "CHN", "IND", "BRA"]:
        s = t[c].dropna()
        assert s.iloc[-1] < s.iloc[0]


def test_us_2019_break_removed():
    t = tariffs().set_index("year")
    assert t.loc[2019, "USA"] != t.loc[2019, "USA"]  # nan
    assert t.USA.dropna().max() < 5

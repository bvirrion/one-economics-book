from make_consumption import growth_summary, share_summary


def test_growth():
    s = growth_summary().iloc[0]
    assert (s.n, s.sd_dc, s.sd_dy, s["corr"]) == (202, 0.69, 0.9, 0.44)
    assert (s.mean_dc, s.mean_dy) == (0.84, 0.83)


def test_share():
    s = share_summary().set_index("iso3")
    assert s.loc["USA", "first"] == 60.3 and s.loc["KOR", "first"] == 73.5
    assert s.loc["USA", "last"] > s.loc["USA", "first"]


def test_gdp_ratio():
    s = share_summary().set_index("iso3").gdp_ratio
    assert list(s) == [2.6, 2.7, 18.7, 1.4]


def test_germany_from_1991_by_hand():
    import pandas as pd

    t = pd.read_csv(__file__.replace("test_consumption.py", "out/share.csv"))
    assert t.loc[t.year < 1991, "DEU"].isna().all()
    assert t.loc[t.year == 1991, "DEU"].notna().all()
    s = share_summary().set_index("iso3")
    assert s.loc["DEU", "first"] == round(float(t.loc[t.year == 1991, "DEU"].iloc[0]), 1)

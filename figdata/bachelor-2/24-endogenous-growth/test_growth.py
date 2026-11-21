from make_growth import res_summary, tfp


def test_tfp():
    assert list(tfp().growth) == [1.33, 0.86, -0.23, 0.75, 0.96, 0.38, 0.53]


def test_researchers():
    s = res_summary().set_index("iso3")
    assert list(s.y1996) == [3207, 2802, 4906, 2186, 447]
    assert list(s.ratio) == [1.54, 2.11, 1.14, 4.33, 4.71]
    assert s.loc["USA", "last_year"] == 2022

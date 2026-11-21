from make_debt import debt_summary, offset_summary, uk_summary


def test_debt():
    s = debt_summary().set_index("iso3")
    assert (s.loc["GBR", "peak"], s.loc["GBR", "peak_year"]) == (270, 1946)
    assert (s.loc["FRA", "peak"], s.loc["FRA", "peak_year"]) == (237, 1921)
    assert list(s.y2020) == [104, 128, 115, 254, 156]


def test_offset():
    s = offset_summary().iloc[0]
    assert (s.n, s.slope, s.se, s.intercept, s["corr"]) == (87, 0.53, 0.19, 0.48, 0.3)


def test_uk_identity():
    # nominal growth = real growth x deflator growth, by compounding the printed rates
    s = uk_summary().iloc[0]
    assert abs((1 + s.real_total / 100) * (1 + s.deflator / 100) - 1 - s.nominal / 100) < 0.002  # one-decimal rounding
    assert abs((1 + s.real / 100) * (1 + s["pop"] / 100) - 1 - s.real_total / 100) < 0.002
    assert (s.real_total, s.deflator, s["pop"]) == (2.4, 6.3, 0.5)


def test_uk():
    s = uk_summary().iloc[0]
    assert (s.debt1946, s.debt1975, s.nominal, s.inflation, s.real, s.ltrate) == (
        270,
        47,
        8.9,
        5.7,
        2.0,
        6.4,
    )

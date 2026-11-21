from make_rules import recent_summary, rule, rule_dec, rule_summary


def test_rule_by_hand():
    # 1980-Q1: inflation 14.589, gap 2.083 -> 14.589 + 1.0415 + 6.2945 + 2 = 23.925
    d = rule().set_index("t")
    assert (d.loc[1980.0, "infl"], d.loc[1980.0, "gap"]) == (14.589, 2.083)
    assert d.loc[1980.0, "rule"] == 23.925
    assert len(d) == 196


def test_rule_tables():
    t = rule_dec().set_index("decade")
    assert list(t["mean"]) == [-0.49, -4.74, 0.88, -0.21, -2.13]
    s = rule_summary().iloc[0]
    assert (s.mad6079, s.mad8707, s.corr6079, s.corr8707) == (2.9, 1.4, 0.93, 0.68)


def test_recent():
    s = recent_summary().iloc[0]
    assert (s.cpi_peak, s.cpi_peak_ym, s.ffr_at_peak) == (9.1, "2022-06", 1.21)
    assert (s.first_above, s.ffr_peak, s.ffr_peak_ym) == ("2022-05", 5.33, "2023-08")

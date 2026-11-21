import numpy as np
from make_co2_panels import tables


def test_counts_and_slopes():
    between, bline, bins, wline, stats = tables()
    s = stats.iloc[0]
    assert s.countries == 200 and s.rows == 6419 == int(s.rows)
    assert 2.5 < s["between"] < 3.0 and 0.9 < s["within"] < 1.1
    assert len(between) == 200 and len(bins) == 20


def test_bins_are_centred_and_ordered():
    _, _, bins, _, _ = tables()
    assert np.all(np.diff(bins.dly) > 0)
    assert abs(bins.dly.mean()) < 1e-3 and abs(bins.dco2.mean()) < 0.05


def test_between_line_through_the_means():
    between, bline, *_ = tables()
    ly = np.log(between.gdp)
    b = (bline.co2[1] - bline.co2[0]) / (np.log(bline.gdp[1]) - np.log(bline.gdp[0]))
    assert abs(bline.co2[0] + b * (ly.mean() - np.log(bline.gdp[0])) - between.co2.mean()) < 1e-6

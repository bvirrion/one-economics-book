import numpy as np
from make_commuters import tables


def test_estimates_near_truth_and_value_of_time():
    b, m, s, _ = tables()
    est, se = dict(zip(m.term, m.est)), dict(zip(m.term, m.se))
    # the data are drawn with cost -0.25 and time -0.06: each estimate lies within
    # 2.5 standard errors of the value that generated it
    assert abs(est["cost"] + 0.25) < 2.5 * se["cost"]
    assert abs(est["time"] + 0.06) < 2.5 * se["time"]
    vot = 60 * est["time"] / est["cost"]
    assert 10 < vot < 20


def test_shares_and_iia_forecast():
    _, _, s, _ = tables()
    s = s.set_index("mode")
    assert np.allclose(s.actual[:3], s.fitted[:3], atol=1e-8)   # score equations
    assert abs(s.forecast.sum() - 1) < 1e-12
    ratio = s.forecast[:3] / s.fitted[:3]
    assert ratio.max() - ratio.min() < 0.25          # not proportional per person

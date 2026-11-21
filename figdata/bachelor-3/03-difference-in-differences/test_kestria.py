import numpy as np
from make_kestria import tables


def test_two_by_two_is_the_difference_of_the_printed_means():
    means, _, est, _, _ = tables()
    m = means.set_index("group").round(4)
    did = (m.y2020.west - m.y2018.west) - (m.y2020.north - m.y2018.north)
    assert abs(did - round(est.est[0], 4)) < 1.5e-4


def test_twfe_biased_toward_zero_clean_close_to_truth():
    _, _, est, _, _ = tables()
    two_by_two, twfe, clean, true = est.est
    assert true < clean + 0.005 and abs(clean - true) < 0.005
    assert twfe > true + 0.01


def test_synthetic_weights_are_a_point_of_the_simplex():
    _, _, _, w, gap = tables()
    assert (w.weight >= 0).all() and abs(w.weight.sum() - 1) < 1e-9
    assert np.all(np.abs(gap.gap[gap.year < 2019]) < 0.03)
    assert (gap.gap[gap.year >= 2020] < -0.09).all()

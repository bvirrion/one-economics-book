import numpy as np
from make_nickell import table


def test_bias_negative_and_shrinking():
    t = table().set_index("T")
    assert (t.estimate < 0.5).all()
    assert np.all(np.diff(t.estimate.values) > 0)
    assert t.estimate[3] < 0.05 and t.estimate[30] > 0.43


def test_approximation_close_for_long_panels():
    t = table().set_index("T")
    assert abs(t.estimate[20] - t.approx[20]) < 0.03

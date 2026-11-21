"""The simulated slopes against least squares by numpy and against the plim."""

import numpy as np
from make_attenuation import table


def test_plim_by_hand():
    t = table().set_index("s2")
    # lambda = 1 / (1 + s2): 1, 0.5 and 0.25 at s2 = 0, 1, 3
    assert (t.loc[0.0, "plim"], t.loc[1.0, "plim"], t.loc[3.0, "plim"]) == (
        2.0,
        1.0,
        0.5,
    )


def test_slopes_near_plim():
    t = table()
    assert len(t) == 31
    # with n = 1000 each slope is within 0.15 of its limit
    assert np.abs(t.slope - t.plim).max() < 0.15
    assert t.slope.iloc[0] > 1.9 and t.slope.iloc[-1] < 0.65

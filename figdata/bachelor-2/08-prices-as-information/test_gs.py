import numpy as np
from make_gs import points, residual_var, share


def test_indifference_holds():
    for c in [0.05, 0.1116, 0.2]:
        phi = share(c)
        assert np.isclose(residual_var(phi), np.exp(2 * c) - 1, atol=1e-9)


def test_cheaper_information_more_informed():
    p = points()
    assert p.phi.is_monotonic_decreasing
    assert p.resid.is_monotonic_increasing


def test_reference_point():
    p = points().set_index("c")
    assert abs(p.loc[0.1116].phi - 0.433) < 0.001
    assert abs(p.loc[0.1116].resid - 0.25) < 0.001

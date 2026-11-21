import numpy as np
from synth import rmspe, synth_weights


def test_recovers_an_exact_convex_combination():
    rng = np.random.default_rng(0)
    Y0 = rng.normal(size=(20, 6)).cumsum(0)
    w0 = np.array([0.5, 0.3, 0.2, 0, 0, 0])
    w = synth_weights(Y0 @ w0, Y0)
    assert np.allclose(w, w0, atol=1e-4)
    assert rmspe(Y0 @ w0, Y0, w) < 1e-4


def test_weights_are_a_point_of_the_simplex():
    rng = np.random.default_rng(1)
    Y0 = rng.normal(size=(15, 8))
    y1 = Y0.max(1) + 1                     # outside the hull: best effort
    w = synth_weights(y1, Y0)
    assert (w >= 0).all() and abs(w.sum() - 1) < 1e-9

import numpy as np
import statsmodels.api as sm
from rdtools import density_test, local_linear


def test_local_linear_matches_weighted_least_squares():
    rng = np.random.default_rng(3)
    x = rng.uniform(-1, 1, 4000)
    y = 1 + 0.5 * x + 0.3 * (x >= 0) + rng.normal(0, 0.2, 4000)
    r = local_linear(x, y, 0, 0.5)
    fits = {}
    for name, side in (("right", x >= 0), ("left", x < 0)):
        xs, ys = x[side], y[side]
        w = np.clip(1 - np.abs(xs) / 0.5, 0, None)
        k = w > 0
        fits[name] = sm.WLS(ys[k], sm.add_constant(xs[k]), weights=w[k]).fit().params[0]
    assert np.isclose(fits["right"], r["right"]) and np.isclose(fits["left"], r["left"])
    assert abs(r["jump"] - 0.3) < 0.05


def test_local_constant_is_a_difference_of_means_with_uniform_weights():
    x = np.array([-0.3, -0.2, -0.1, 0.0, 0.1, 0.2, 0.9])
    y = np.array([1.0, 2.0, 3.0, 5.0, 6.0, 7.0, 100.0])
    r = local_linear(x, y, 0, 0.25, degree=0, kernel="uniform")
    assert np.isclose(r["jump"], 6.0 - 2.5)


def test_density_test_detects_bunching_only_when_planted():
    rng = np.random.default_rng(4)
    clean = rng.normal(60, 10, 20000)
    assert abs(density_test(clean, 70, 10)["theta"]) < 3 * density_test(clean, 70, 10)["se"]
    moved = clean.copy()
    near = (moved >= 66) & (moved < 70) & (rng.uniform(size=moved.size) < 0.5)
    moved[near] = 70 + rng.uniform(0, 1, near.sum())
    r = density_test(moved, 70, 10)
    assert r["theta"] > 5 * r["se"]

import numpy as np
import statsmodels.api as sm
from metatools import dersimonian_laird, fat_pet, filtered_mean, fixed_effect, power


def test_power_and_filtered_mean_against_simulation():
    rng = np.random.default_rng(0)
    b, s = 0.1, 0.08
    draws = rng.normal(b, s, 2_000_000)
    kept = draws[draws / s > 1.96]
    assert abs(power(b, s) - len(kept) / len(draws)) < 0.002
    assert abs(filtered_mean(b, s) - kept.mean()) < 0.001


def test_fixed_effect_and_dl():
    est, se = np.array([0.1, 0.3, 0.2]), np.array([0.1, 0.1, 0.2])
    m, sm_ = fixed_effect(est, se)
    assert np.isclose(m, (0.1 * 100 + 0.3 * 100 + 0.2 * 25) / 225)
    assert np.isclose(sm_, 1 / np.sqrt(225))
    r, rse, tau2, q = dersimonian_laird([0.0, 0.5, 1.0], [0.1, 0.1, 0.1])
    assert np.isclose(q, 50.0) and np.isclose(tau2, (50 - 2) / (300 - 100))
    assert np.isclose(r, 0.5)


def test_fat_pet_matches_statsmodels_wls():
    rng = np.random.default_rng(1)
    se = rng.uniform(0.02, 0.3, 40)
    est = 0.05 + 0.8 * se + rng.normal(0, se)
    pet, pet_se, fat, fat_se = fat_pet(est, se)
    m = sm.WLS(est, sm.add_constant(se), weights=1 / se**2).fit()
    assert np.allclose([pet, fat], m.params) and np.allclose([pet_se, fat_se], m.bse)

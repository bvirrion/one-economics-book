"""A simulated town: schooling, earnings, and an ability nobody records."""
import numpy as np


def draw(n, seed, pull=0.8):
    rng = np.random.default_rng(seed)
    ability = rng.normal(0, 1, n)          # unseen by the economist
    near = rng.integers(0, 2, n)           # 1 if a college is near home
    school = 12 + pull * near + 1.0 * ability + rng.normal(0, 1, n)
    log_wage = 1.5 + 0.08 * school + 0.10 * ability + rng.normal(0, 0.3, n)
    return {"ability": ability, "near": near, "school": school,
            "log_wage": log_wage}

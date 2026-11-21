"""An omitted variable: ability raises both schooling and earnings (simulated)."""

import numpy as np

rng = np.random.default_rng(2026)
slopes_short, slopes_long = [], []
for _ in range(1_000):
    ability = rng.standard_normal(500)
    school = 12 + 1.5 * ability + rng.normal(0, 2, 500)
    log_y = 9 + 0.06 * school + 0.10 * ability + rng.normal(0, 0.5, 500)
    slopes_short.append(np.polyfit(school, log_y, 1)[0])  # ability left out
    X = np.column_stack([np.ones(500), school, ability])
    slopes_long.append(np.linalg.lstsq(X, log_y, rcond=None)[0][1])
print("true effect of a year of school: 0.060")
print(f"slope, ability left out: mean {np.mean(slopes_short):.4f}")
print(f"slope, ability included: mean {np.mean(slopes_long):.4f}")
print(f"predicted bias 0.10 * 1.5 / (1.5**2 + 2**2) = {0.10 * 1.5 / 6.25:.4f}")

"""Simulated potential outcomes: difference in means = ATT + selection bias, exactly."""

import numpy as np

rng = np.random.default_rng(33)
n = 10_000
skill = rng.standard_normal(n)
y0 = 10 + 2 * skill + rng.standard_normal(n)  # earnings without training
y1 = (
    y0 + 1.0 - 0.5 * skill + 0.5 * rng.standard_normal(n)
)  # larger for the less skilled
treated = skill + rng.standard_normal(n) < 0  # the less skilled take the training

observed = np.where(treated, y1, y0)
diff = observed[treated].mean() - observed[~treated].mean()
att = (y1 - y0)[treated].mean()
bias = y0[treated].mean() - y0[~treated].mean()
print(f"ATE {(y1 - y0).mean():.3f}, ATT {att:.3f}")
print(f"difference in observed means {diff:.3f}")
print(f"ATT + selection bias {att:.3f} + ({bias:.3f}) = {att + bias:.3f}")

random = rng.random(n) < 0.5  # the same people, assigned at random
observed = np.where(random, y1, y0)
print(
    f"with random assignment: {observed[random].mean() - observed[~random].mean():.3f}"
)

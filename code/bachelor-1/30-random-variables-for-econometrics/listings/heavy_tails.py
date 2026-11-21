"""Means of a Pareto population with alpha = 1.5: the variance does not exist."""

import numpy as np

rng = np.random.default_rng(2026)
alpha = 1.5  # mean alpha / (alpha - 1) = 3, variance infinite
for n in (100, 10_000, 1_000_000):
    x = rng.pareto(alpha, size=(20, n)) + 1  # Pareto with minimum 1
    means = x.mean(axis=1)
    print(f"n = {n:>9,}: means from {means.min():.2f} to {means.max():.2f}")

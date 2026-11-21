"""A monthly survey of 100,000 people in the labour force, true rate 6.0%."""

import numpy as np

rng = np.random.default_rng(2026)
n, rate = 100_000, 0.060
months = rng.binomial(n, rate, size=2) / n  # two independent monthly samples
se = np.sqrt(rate * (1 - rate) / n)
print(
    f"estimates {100 * months[0]:.2f}% and {100 * months[1]:.2f}%; standard error"
    f" {100 * se:.3f} points"
)
change = months[1] - months[0]
se_change = np.sqrt(2) * se  # independent samples; overlapping samples do better
print(
    f"change {100 * change:+.2f} points; its standard error {100 * se_change:.3f};"
    f" 90% margin {100 * 1.645 * se_change:.2f}"
)

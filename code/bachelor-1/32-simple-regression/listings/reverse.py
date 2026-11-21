"""Supply and demand shocks: the price-quantity slope is neither curve's (simulated)."""

import numpy as np

rng = np.random.default_rng(2026)
n = 10_000
u_d, u_s = rng.normal(0, 1, n), rng.normal(0, 2, n)  # demand and supply shocks
# demand q = 10 - p + u_d and supply q = 2 + p + u_s, solved for the market
p = (8 + u_d - u_s) / 2
q = (12 + u_d + u_s) / 2
print("demand slope -1, supply slope +1")
print(f"regression of quantity on price: slope {np.polyfit(p, q, 1)[0]:.3f}")

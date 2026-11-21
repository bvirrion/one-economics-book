"""Exercise 12: a shift-share measure of import exposure (invented data).

Five regions, three industries. Shares: each industry's share of a region's
employment in 1990. Shocks: growth of imports per worker in each industry
nationally, 1990--2007 (thousands of dalens). Outcome: change in the region's
manufacturing employment share, in points.
"""
import numpy as np

shares = np.array([[0.30, 0.10, 0.05],   # region A
                   [0.10, 0.25, 0.05],   # region B
                   [0.05, 0.05, 0.20],   # region C
                   [0.20, 0.20, 0.10],   # region D
                   [0.02, 0.03, 0.05]])  # region E
shocks = np.array([8.0, 3.0, 1.0])  # textiles, machinery, food
outcome = np.array([-3.1, -1.6, -0.7, -2.6, -0.2])

exposure = shares @ shocks  # the shift-share sum, region by region
X = np.column_stack([np.ones(5), exposure])
beta, *_ = np.linalg.lstsq(X, outcome, rcond=None)
for name, e, y in zip("ABCDE", exposure, outcome):
    print(f"region {name}: exposure {e:.2f}, change {y:+.1f} points")
print(f"slope {beta[1]:.3f} points per thousand dalens of exposure")

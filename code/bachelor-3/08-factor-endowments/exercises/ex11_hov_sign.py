"""Exercise 11: an HOV sign test on a simulated world of 10 countries and 3 factors.
Each country's measured factor content of trade is its HOV prediction V - s V_w,
times a home-bias factor (0.2: four fifths of the trade is missing), plus noise with a
standard deviation of half the typical prediction. Seed 1995."""
import numpy as np

rng = np.random.default_rng(1995)
V = rng.lognormal(mean=3.0, sigma=0.8, size=(10, 3))       # endowments
s = V.sum(axis=1) / V.sum()                                # shares of world income
pred = V - s[:, None] * V.sum(axis=0)
scale = np.abs(pred).mean()
for label, measured in [("exact HOV", pred),
                        ("missing trade", 0.2 * pred),
                        ("missing trade + noise",
                         0.2 * pred + rng.normal(0, 0.5 * scale, pred.shape))]:
    signs = np.mean(np.sign(measured) == np.sign(pred))
    slope = (measured * pred).sum() / (pred**2).sum()
    print(f"{label:22s} sign matches {signs:.2f}   slope of measured on predicted"
          f" {slope:.2f}")

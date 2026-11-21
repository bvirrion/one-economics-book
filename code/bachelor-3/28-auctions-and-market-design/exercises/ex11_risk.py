"""Exercise 11: four auction formats with risk-averse bidders. Four bidders with
values uniform on [0, 1] and utility x^0.5 of their gain. In the English and
second-price auctions bidding one's value (or staying in up to it) is still a
dominant strategy; in the first-price and Dutch auctions the equilibrium bid is
(n - 1) / (n - 1 + 0.5) times the value, against (n - 1) / n for risk-neutral bidders.
"""
import numpy as np

n, rho, draws = 4, 0.5, 200_000
rng = np.random.default_rng(11)
v = np.sort(rng.uniform(size=(draws, n)), axis=1)
second, top = v[:, -2].mean(), v[:, -1].mean()
first_price = (n - 1) / (n - 1 + rho) * top
first_neutral = (n - 1) / n * top
for name, rev in [("English", second), ("second-price", second),
                  ("Dutch", first_price), ("first-price", first_price)]:
    print(f"{name:13s} expected revenue {rev:.3f}")
print(f"first-price with risk-neutral bidders: {first_neutral:.3f}")

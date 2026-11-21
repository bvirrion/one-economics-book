"""First-price and second-price auctions with values uniform on [0, 1]."""

import numpy as np

rng = np.random.default_rng(1414)
auctions = 200_000

for n in (2, 3, 6):
    values = rng.uniform(0, 1, size=(auctions, n))
    top_two = np.sort(values, axis=1)[:, -2:]  # second-highest, highest
    first = (n - 1) / n * top_two[:, 1]  # winner pays her own equilibrium bid
    second = top_two[:, 0]  # winner pays the second-highest value
    cautious = (n - 1) / (n - 0.5) * top_two[:, 1]  # bidders with r = 0.5
    print(
        f"n = {n}: revenue first-price {first.mean():.3f} (sd {first.std():.3f}), "
        f"second-price {second.mean():.3f} (sd {second.std():.3f}); "
        f"theory {(n - 1) / (n + 1):.3f}"
    )
    print(f"        first-price with risk-averse bidders {cautious.mean():.3f}")

"""The significance filter: 20,000 simulated trials of a treatment whose true effect is
0.1 standard deviations, at six sample sizes. Only significant positive estimates are
published. How large is the average published estimate?"""
import numpy as np
from metatools import filtered_mean, power

rng = np.random.default_rng(6)
beta = 0.1
print("per arm   s.e.   power   published mean   exaggeration   formula")
for n in [50, 100, 200, 400, 800, 1600]:
    s = np.sqrt(2 / n)                        # s.e. of a difference of two means
    est = rng.normal(beta, s, 20_000)         # one estimate per simulated trial
    published = est[est / s > 1.96]
    print(f"{n:7d}  {s:.3f}   {len(published) / len(est):.3f}"
          f"   {published.mean():14.3f}   {published.mean() / beta:12.2f}"
          f"   {filtered_mean(beta, s) / beta:7.2f}")
print(f"power by formula at 50 and 1600 per arm: {power(beta, np.sqrt(2 / 50)):.3f},"
      f" {power(beta, np.sqrt(2 / 1600)):.3f}")

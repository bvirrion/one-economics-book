"""LATE: with unequal gains, IV recovers the compliers' average effect."""
import numpy as np

rng = np.random.default_rng(11)
n = 200_000
kind = rng.choice(["always", "never", "complier"], size=n, p=[0.2, 0.5, 0.3])
gain = np.select([kind == "always", kind == "complier"], [0.30, 0.15], 0.02)
gain = gain + rng.normal(0, 0.05, n)          # gains also vary inside a type
y0 = 10 + 0.2 * (kind == "always") + rng.normal(0, 0.5, n)
z = rng.integers(0, 2, n)                     # the offer, at random
d = (kind == "always") | ((kind == "complier") & (z == 1))
y = y0 + d * gain                             # observed outcome

first = d[z == 1].mean() - d[z == 0].mean()
wald = (y[z == 1].mean() - y[z == 0].mean()) / first
print(f"share treated if offered      {d[z == 1].mean():.3f}")
print(f"share treated if not offered  {d[z == 0].mean():.3f}")
print(f"first stage (complier share)  {first:.3f}")
print(f"Wald estimate                 {wald:.3f}")
print(f"compliers' mean gain          {gain[kind == 'complier'].mean():.3f}")
print(f"everyone's mean gain (ATE)    {gain.mean():.3f}")
print(f"treated minus untreated       {y[d].mean() - y[~d].mean():.3f}")

"""Manipulation at a cutoff: exam scores (whole marks) with a pass mark of 70, before
and after a marker moves half of the scripts on 66-69 up to 70."""
import numpy as np
from rdtools import density_test

rng = np.random.default_rng(70)
clean = np.clip(np.round(rng.normal(58, 12, 20000)), 0, 100)
moved = clean.copy()
pick = (moved >= 66) & (moved <= 69) & (rng.uniform(size=moved.size) < 0.5)
moved[pick] = 70
print(f"scripts moved {pick.sum()}")
for name, x in (("clean", clean), ("re-marked", moved)):
    r = density_test(x, cutoff=69.5, h=10, bin=1)
    print(f"{name:10s} log jump in density {r['theta']:6.3f}  (s.e. {r['se']:.3f})"
          f"  t = {r['theta'] / r['se']:5.1f}")

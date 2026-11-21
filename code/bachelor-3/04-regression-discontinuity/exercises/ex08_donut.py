"""Exercise 8: a donut regression discontinuity. Exam scores as in the chapter's
density_test.py; earnings (log) rise with the true score and jump by 0.10 at a pass."""
import numpy as np
from rdtools import local_linear

rng = np.random.default_rng(70)
true = np.clip(np.round(rng.normal(58, 12, 20000)), 0, 100)
moved = true.copy()
pick = (moved >= 66) & (moved <= 69) & (rng.uniform(size=moved.size) < 0.5)
moved[pick] = 70
earn = 3 + 0.01 * true + 0.10 * (moved >= 70) + rng.normal(0, 0.3, true.size)

r = local_linear(moved, earn, cutoff=69.5, h=10)
print(f"all recorded scores          jump {r['jump']:6.3f} (s.e. {r['se']:.3f})")
for hole in (1, 2):
    keep = np.abs(moved - 69.5) > hole
    r = local_linear(moved[keep], earn[keep], cutoff=69.5, h=10)
    print(f"donut, {hole} mark(s) each side jump {r['jump']:6.3f} (s.e. {r['se']:.3f})")

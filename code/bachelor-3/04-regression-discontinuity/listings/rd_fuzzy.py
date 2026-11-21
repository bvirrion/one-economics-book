"""A fuzzy discontinuity: Maimonides' rule on simulated schools. Most schools split a
grade into classes of at most 40; the rest follow their own target size.
True effect of one more pupil per class on the class's mean score: -0.25 points."""
import numpy as np
from rdtools import local_linear

rng = np.random.default_rng(1999)
S = 4000
enrol = rng.integers(15, 131, S)                       # pupils in the grade
rule = enrol / ((enrol - 1) // 40 + 1)                 # Maimonides' rule
target = rng.uniform(28, 38, S)                        # other schools' own target
own = enrol / np.ceil(enrol / target)
size = np.where(rng.uniform(size=S) < 0.75, rule, own)
score = 75 - 0.25 * size + 0.02 * enrol + rng.normal(0, 6, S)

first = local_linear(enrol, size, cutoff=40.5, h=10)
reduced = local_linear(enrol, score, cutoff=40.5, h=10)
print(f"schools within 10 of the cutoff {first['n']}")
for name, r in (("first stage: jump in class size", first),
                ("reduced form: jump in score", reduced)):
    print(f"{name:32s}{r['jump']:7.2f} (s.e. {r['se']:.2f})")
print(f"fuzzy RD (Wald ratio)           {reduced['jump'] / first['jump']:7.3f}")

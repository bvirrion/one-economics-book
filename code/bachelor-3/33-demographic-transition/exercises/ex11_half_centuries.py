"""Exercise 11: growth of income per person by half-century, 1300--1850, in the
Maddison Project's United Kingdom series, between decade means (the ten years from
a - 5 to a + 4; the 1850 mean has only 1845--1850), and the first half-century in which
it exceeds 0.3 % a year and stays above it."""
import numpy as np
from econdata import maddison

s = maddison(isos=["GBR"], since=1290, until=1850).set_index("year").gdppc
d = {a: s.loc[a - 5:a + 4].mean() for a in range(1300, 1851, 50)}
g = {a: 100 * np.log(d[a + 50] / d[a]) / 50 for a in range(1300, 1850, 50)}
for a, v in g.items():
    print(f"{a}-{a + 50}: {v:+.2f} % a year")
first = next(a for a in g if all(v > 0.3 for b, v in g.items() if b >= a))
print(f"growth above 0.3 % in every half-century from {first}")

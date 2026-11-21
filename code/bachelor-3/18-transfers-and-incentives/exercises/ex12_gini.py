"""Exercise 12: redistribution in Brenland's household survey.

Gini coefficients of gross income, of gross income minus tax, and of disposable
income (gross - tax + transfers).
"""
import numpy as np
from country import load


def gini(x):
    x = np.sort(np.asarray(x, dtype=float))
    n = len(x)
    return (2 * np.arange(1, n + 1) - n - 1).dot(x) / (n * x.sum())


h = load("households")
g0 = gini(h.gross_income)
g1 = gini(h.gross_income - h.tax)
g2 = gini(h.disposable)
print(f"Gini, gross income:          {g0:.3f}")
print(f"Gini, gross minus tax:       {g1:.3f}")
print(f"Gini, disposable income:     {g2:.3f}")
print(f"reduction: {g0 - g2:.3f}, of which taxes {g0 - g1:.3f} "
      f"({100 * (g0 - g1) / (g0 - g2):.0f} %), transfers {g1 - g2:.3f}")

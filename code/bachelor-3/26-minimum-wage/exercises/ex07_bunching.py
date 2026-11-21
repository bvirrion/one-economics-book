"""Exercise 7: a bunching estimate from invented wage histograms.

Jobs by one-dollar wage bin before and after a minimum wage rises from 8 to 10, in
treated and control states (thousands of jobs). Missing jobs below the new minimum
and excess jobs from it to 4 dollars above, each net of the change in control
states; the employment effect is their sum.
"""
import numpy as np

bins = np.arange(6, 20)
treated_before = np.array([5, 9, 14, 16, 15, 14, 12, 11, 9, 8, 7, 6, 5, 4.0])
treated_after = np.array([0, 0, 1, 2, 40, 25, 16, 12, 9, 8, 7, 6, 5, 4.0])
control_before = np.array([4, 8, 13, 15, 15, 13, 12, 10, 9, 8, 7, 6, 5, 4.0])
control_after = np.array([4, 8, 13, 15, 15, 14, 12, 11, 9, 8, 7, 6, 5, 4.0])

change = (treated_after - treated_before) - (control_after - control_before)
below = bins < 10
window = (bins >= 10) & (bins < 14)
missing, excess = change[below].sum(), change[window].sum()
base = treated_before[bins < 14].sum()
print(f"missing jobs below the new minimum: {missing:.1f} thousand")
print(f"excess jobs from 10 to 13 dollars: {excess:.1f} thousand")
print(f"employment change: {missing + excess:.1f} thousand, "
      f"{100 * (missing + excess) / base:.1f} % of jobs below 14 dollars")

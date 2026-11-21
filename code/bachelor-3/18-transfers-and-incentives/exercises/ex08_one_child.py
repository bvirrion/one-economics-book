"""Exercise 8: the marginal effective tax rate of a single parent with one child,
United States, 2024 (federal income tax, employee payroll tax, earned income credit,
child tax credit; state taxes and benefits left out). Parameters: Rev. Proc. 2023-34,
2024 Schedule 8812 instructions, IRS Topic 751.
"""
import numpy as np

BRACKETS = [(0, 0.10), (16_550, 0.12), (63_100, 0.22)]
STD, PAYROLL = 21_900, 0.0765
EARNED, MAXIMUM, START, END = 12_390, 4_213, 22_720, 49_084  # one child
CTC, ACTC_MAX = 2_000, 1_700


def net(e):
    z, t0 = max(0.0, e - STD), 0.0
    for (lo, r), nxt in zip(BRACKETS, BRACKETS[1:] + [(float("inf"), 0)]):
        t0 += max(0.0, min(z, nxt[0]) - lo) * r
    used = min(t0, CTC)
    actc = min(CTC - used, ACTC_MAX, 0.15 * max(0.0, e - 2_500))
    if e <= START:
        eitc = min(MAXIMUM / EARNED * e, MAXIMUM)
    else:
        eitc = max(0.0, MAXIMUM - MAXIMUM / (END - START) * (e - START))
    return e * (1 - PAYROLL) - (t0 - used) + actc + eitc


e = np.arange(0, 60_001, 100, dtype=float)
n = np.array([net(x) for x in e])
mtr = 100 * (1 - np.diff(n) / 100)
print(f"phase-in {100 * MAXIMUM / EARNED:.2f} %, "
      f"phase-out {100 * MAXIMUM / (END - START):.2f} %")
for lo, hi in ((0, 10_000), (15_000, 20_000), (30_000, 40_000), (50_000, 60_000)):
    sel = (e[1:] > lo) & (e[1:] <= hi)
    print(f"{lo:>6}-{hi:<6} marginal rate {mtr[sel].min():6.2f} to "
          f"{mtr[sel].max():6.2f} %")
top = mtr.argmax()
print(f"highest: {mtr[top]:.2f} % at {e[top + 1]:,.0f} dollars")

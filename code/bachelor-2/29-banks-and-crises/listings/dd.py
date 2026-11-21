"""The Diamond-Dybvig bank: the deposit contract and the run threshold.

A share PI of depositors must consume at date 1; the others can wait for date 2. One
unit invested gives 1 if liquidated at date 1 and R at date 2. Utility c**(1-g)/(1-g).
"""

PI, R = 0.25, 2.0


def contract(g):
    """Payouts c1, c2 that maximise expected utility with PI c1 + (1-PI) c2 / R = 1."""
    c1 = 1 / (PI + (1 - PI) * R ** (1 / g - 1))
    return c1, R ** (1 / g) * c1


def patient_wait(c1, f):
    """What a patient depositor gets by waiting when a share f withdraws at date 1."""
    left = max(1 - f * c1, 0.0)
    return left * R / (1 - f)


print("risk aversion   c1      c2     run threshold   bank empty at")
for g in (1.0, 2.0, 4.0):
    c1, c2 = contract(g)
    threshold = (R - c1) / (c1 * (R - 1))
    print(f"{g:13.0f}  {c1:6.3f}  {c2:6.3f}  {threshold:14.3f}  {1 / c1:13.3f}")

c1, _ = contract(2.0)
for f in (0.25, 0.5, 0.6, 0.75):
    print(
        f"withdrawals {f:.2f}: waiting pays {patient_wait(c1, f):.3f}, running {c1:.3f}"
    )

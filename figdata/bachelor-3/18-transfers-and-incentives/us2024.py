"""Federal taxes and credits of a single parent (head of household) with two
qualifying children, United States, 2024, as functions of earnings in dollars.
Parameters: Rev. Proc. 2023-34 (brackets, standard deduction, EITC), Schedule 8812
instructions and the CP08 page (child tax credit), IRS Topic 751 (payroll tax).
Left out: state taxes, SNAP and other benefits. The EITC is computed from its
parameters; the IRS tables round in steps of 50 dollars."""
import numpy as np

BRACKETS = [(0, 0.10), (16_550, 0.12), (63_100, 0.22), (100_500, 0.24)]
STD = 21_900
EITC_EARNED, EITC_MAX, EITC_START, EITC_END = 17_400, 6_960, 22_720, 55_768
CTC, ACTC_MAX, ACTC_FLOOR, ACTC_RATE, KIDS = 2_000, 1_700, 2_500, 0.15, 2
PAYROLL = 0.062 + 0.0145
PHASE_IN = EITC_MAX / EITC_EARNED
PHASE_OUT = EITC_MAX / (EITC_END - EITC_START)


def income_tax_before_credits(e):
    z = max(0.0, e - STD)
    t = 0.0
    for (lo, r), nxt in zip(BRACKETS, BRACKETS[1:] + [(float("inf"), 0)]):
        if z > lo:
            t += (min(z, nxt[0]) - lo) * r
    return t


def eitc(e):
    if e <= EITC_START:
        return min(PHASE_IN * e, EITC_MAX)
    return max(0.0, EITC_MAX - PHASE_OUT * (e - EITC_START))


def child_credits(e, t0):
    """Non-refundable part used against tax, and refundable part (ACTC)."""
    full = CTC * KIDS
    used = min(t0, full)
    actc = min(full - used, ACTC_MAX * KIDS, ACTC_RATE * max(0.0, e - ACTC_FLOOR))
    return used, actc


def net_income(e):
    t0 = income_tax_before_credits(e)
    used, actc = child_credits(e, t0)
    return e - PAYROLL * e - (t0 - used) + actc + eitc(e)


def schedule(top=70_000, step=100):
    e = np.arange(0, top + step, step, dtype=float)
    n = np.array([net_income(x) for x in e])
    mtr = np.r_[np.nan, 100 * (1 - np.diff(n) / step)]
    return e, n, mtr

"""Worked numbers of the exercises and weekend problem of b1 ch. 23.

Weekend problem: Kestria's printing press. Real balances as a share of GDP:
m(pi) = 0.25 exp(-2.5 pi), pi the continuously compounded inflation rate. In a steady
state with no real growth, money grows at pi and seigniorage is pi m(pi) of GDP.
"""

import math

K, A = 0.25, 2.5


def m(pi):
    return K * math.exp(-A * pi)


def seign(pi):
    return pi * m(pi)


def roots(target):
    """The two inflation rates at which seigniorage equals target (bisection)."""
    out = []
    for lo, hi in ((0.0, 1 / A), (1 / A, 5.0)):
        f_lo = seign(lo) - target
        for _ in range(200):
            mid = (lo + hi) / 2
            if (seign(mid) - target) * f_lo > 0:
                lo, f_lo = mid, seign(mid) - target
            else:
                hi = mid
        out.append(round((lo + hi) / 2, 4))
    return out


def problem():
    pi_max = 1 / A
    return {
        "m0": m(0),
        "m5": round(m(0.05), 4),
        "v5": round(1 / m(0.05), 3),
        "m10": round(m(0.10), 4),
        "v10": round(1 / m(0.10), 3),
        "semi": A,
        "elast5": round(A * 0.05, 3),
        "s5": round(100 * seign(0.05), 3),
        "roots2": roots(0.02),
        "m_low": round(m(roots(0.02)[0]), 4),
        "m_high": round(m(roots(0.02)[1]), 4),
        "pi_max": pi_max,
        "s_max": round(100 * seign(pi_max), 3),
        "s_max_exact": round(100 * K / (A * math.e), 3),
        "m_at_max": round(m(pi_max), 4),
        "annual_max": round(100 * (math.exp(pi_max) - 1), 2),
        "s_60": round(100 * seign(0.6), 3),
        "s_150": round(100 * seign(1.5), 3),
        "m_150": round(m(1.5), 5),
        "annual_150": round(100 * (math.exp(1.5) - 1), 1),
        "m_02": round(m(0.02), 4),
        "jump": round(m(0.02) / m(1.5), 1),
        "issue": round(100 * (m(0.02) - m(1.5)), 2),
    }


def exercises():
    return {
        "pi": 8 - 3,
        "seign": 0.2 * 0.1,
        "elast": 4 * 0.05,
        "pi_star": 1 / 2,
        "s_star": round(1 / (2 * math.e), 4),
        "bol_ratio": round(12.1 / 27.1, 3),
        "pi8": 6 + (-1) - 2,
        "vel_factor": round(1.782 / 1.182, 3),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())

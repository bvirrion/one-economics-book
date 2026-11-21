"""Worked numbers of the exercises and weekend problem of b1 ch. 13.

Weekend problem: Brenland sugar, demand Q = 120 - 10 P and supply Q = 10 p
(thousand tonnes a year; dalens a kilogram), a tax of tau dalens a kilogram.
"""

import math


def sugar(tau):
    p = 6 - tau / 2
    q = 10 * p
    big_p = p + tau
    cs = 0.5 * q * (12 - big_p)
    ps = 0.5 * q * p
    rev = tau * q
    return {
        "P": big_p,
        "p": p,
        "Q": q,
        "CS": cs,
        "PS": ps,
        "R": rev,
        "DWL": 360 - cs - ps - rev,
    }


def r(d, k=4):
    return {key: round(val, k) for key, val in d.items()}


def problem():
    return {
        "t0": r(sugar(0)),
        "t12": r(sugar(1.2)),
        "t24": r(sugar(2.4)),
        "t6": r(sugar(6)),
        "harberger_12": 0.5 * 1.2**2 * (60 / 6) * 0.5,
        "mdwl_12": round(5 * 1.2 / (60 - 10 * 1.2), 4),
        "mdwl_24": round(5 * 2.4 / (60 - 10 * 2.4), 4),
        "avg_12": round(sugar(1.2)["DWL"] / sugar(1.2)["R"], 4),
        "avg_24": round(sugar(2.4)["DWL"] / sugar(2.4)["R"], 4),
        "subsidy_Q": 60 + 5 * 1.2,
        "subsidy_cost": 1.2 * (60 + 5 * 1.2),
    }


def exercises():
    p0, q0 = 10.0, 10.0
    p1 = math.sqrt(100 / 1.1)
    q1 = p1
    dwl = 100 * math.log(q0 / q1) - (q0**2 - q1**2) / 2
    wedge = 1.1 * p1 - p1
    return {
        "ex1": (40, 40, 0.5 * 40 * 20, 0.5 * 40 * 40),
        "cs_log": round(100 * math.log(2), 2),
        "ad_p": round(p1, 4),
        "ad_P": round(1.1 * p1, 4),
        "dwl_exact": round(dwl, 4),
        "dwl_2nd_initial": 0.5 * 1.0**2 * (q0 / p0) * 0.5,
        "dwl_2nd_wedge": round(0.5 * wedge**2 * (q0 / p0) * 0.5, 4),
        "vat_std": round(100 * (1 - 1.16 / 1.19), 2),
        "vat_red": round(100 * (1 - 1.05 / 1.07), 2),
    }


if __name__ == "__main__":
    print(problem())
    print(exercises())

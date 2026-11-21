"""Worked numbers of the exercises and weekend problem of b1 ch. 11.

Weekend problem: a Kestrian maize farm, q = 40 * N**0.25 * T**0.25 (tonnes),
fertiliser N at v kests per kg, land T at rent rho kests per hectare a year,
maize price p.
"""

import math

A = 40.0


def long_run(p, v, rho):
    q = p * A**2 / (4 * math.sqrt(v * rho))
    rev = p * q
    return {"q": q, "N": 0.25 * rev / v, "T": 0.25 * rev / rho, "profit": 0.5 * rev}


def short_run(p, v, t_fixed=250.0, rho=200.0):
    b = A * t_fixed**0.25
    n = (p * b / (4 * v)) ** (4 / 3)
    q = b * n**0.25
    return {"q": q, "N": n, "profit": p * q - v * n - rho * t_fixed, "B": b}


def r(d, k=2):
    return {key: round(val, k) for key, val in d.items()}


def problem():
    return {
        "lr100": r(long_run(100, 2, 200)),
        "profit_fn": 100**2 * A**2 / (8 * math.sqrt(2 * 200)),
        "sr100": r(short_run(100, 2)),
        "sr150": r(short_run(150, 2)),
        "lr150": r(long_run(150, 2, 200)),
        "sr_both": r(short_run(150, 4.5)),
        "lr_both": r(long_run(150, 4.5, 200)),
        "cube": round(1.5 ** (1 / 3), 4),
    }


def exercises():
    p, w, rr = 8, 1, 1
    q = (p**0.75 * 0.25**0.25 * 0.5**0.5) ** 4
    return {
        "shutdown": 10 - 1.5 + 1.5**2 / 3,
        "q": round(q, 4),
        "K": round(0.25 * p * q / rr, 4),
        "L": round(0.5 * p * q / w, 4),
        "profit": round(p**4 / (64 * rr * w**2), 4),
        "soya_ratio": round(45.907 / 11.487, 2),
        "world_growth": round(100 * ((4.206 / 1.353) ** (1 / 63) - 1), 2),
        "africa_growth": round(100 * ((1.676 / 0.81) ** (1 / 63) - 1), 2),
    }


if __name__ == "__main__":
    print(problem())
    print(exercises())

"""Worked numbers of the exercises and weekend problem of b1 ch. 20.

Weekend problem: Kestria after the war. y = k^(1/3) per worker, s = 0.2, n = 0.01,
delta = 0.05. The exact path uses z = k^(1 - alpha), which obeys
dz/dt = (1 - alpha) [s - (n + delta) z] and so converges at the rate
lambda = (1 - alpha)(n + delta) exactly.
"""

import math


def steady(s, nd, a):
    k = (s / nd) ** (1 / (1 - a))
    y = k**a
    return k, y, (1 - s) * y


def path_k(k0, s, nd, a, t):
    lam = (1 - a) * nd
    zs = s / nd
    z = zs + (k0 ** (1 - a) - zs) * math.exp(-lam * t)
    return z ** (1 / (1 - a))


def problem():
    a, s, nd = 1 / 3, 0.2, 0.06
    k, y, c = steady(s, nd, a)
    kg, yg, cg = steady(a, nd, a)
    k0 = k / 2
    y0 = k0**a
    g_k0 = s * y0 / k0 - nd
    lam = (1 - a) * nd
    half = math.log(2) / lam
    kh = path_k(k0, s, nd, a, half)
    yh = kh**a
    log_gap0 = math.log(y / y0)
    log_gap_h = math.log(y / yh)
    # reform to the golden rule from the prewar steady state
    c_jump = (1 - a) * y
    t = 0.0
    while (1 - a) * path_k(k, a, nd, a, t) ** a < c:
        t += 0.01
    c10 = (1 - a) * path_k(k, a, nd, a, 10) ** a
    # technical progress
    ngd = 0.08
    kt, yt, ct = steady(s, ngd, a)
    return {
        "k": round(k, 3),
        "y": round(y, 3),
        "c": round(c, 3),
        "K_Y": round(k / y, 3),
        "mpk": round(a * y / k, 4),
        "kg": round(kg, 3),
        "yg": round(yg, 3),
        "cg": round(cg, 3),
        "k0": round(k0, 3),
        "y0": round(y0, 3),
        "g_k0": round(g_k0, 4),
        "g_y0": round(a * g_k0, 4),
        "lam": round(lam, 4),
        "half": round(half, 2),
        "kh": round(kh, 3),
        "yh": round(yh, 3),
        "log_gap0": round(log_gap0, 4),
        "log_gap_h": round(log_gap_h, 4),
        "share_closed": round(1 - log_gap_h / log_gap0, 3),
        "level_closed": round((yh - y0) / (y - y0), 3),
        "c_jump": round(c_jump, 3),
        "t_cross": round(t, 1),
        "c10": round(c10, 3),
        "kt": round(kt, 3),
        "yt": round(yt, 3),
        "ct": round(ct, 3),
        "K_Y_t": round(kt / yt, 3),
        "lam_t": round((1 - a) * ngd, 4),
        "half_t": round(math.log(2) / ((1 - a) * ngd), 2),
    }


def exercises():
    k, y, c = steady(0.25, 0.07, 0.3)
    lam = (2 / 3) * 0.07
    return {
        "k": round(k, 3),
        "y": round(y, 3),
        "c": round(c, 3),
        "lam": round(lam, 4),
        "half": round(math.log(2) / lam, 2),
        "ratio": round((0.25 / 0.10) ** 0.5, 3),
        "data_ratio": round(38117 / 5342, 2),
        "quart_pred": round((26.7 / 15.4) ** 0.5, 2),
        "alpha_2pct": round(1 - 0.02 / 0.08, 2),
        "kg": round((0.3 / 0.07) ** (1 / 0.7), 3),
        "K_Y_bal": round(0.2 / 0.08, 3),
        "z0": round((6.086 / 2) ** (2 / 3), 4),
        "india": round(8854 / 7390, 3),
        "usa": round(49351 / 68683, 3),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())

"""Worked numbers of the exercises and weekend problem of b1 ch. 8.

Weekend problem: a Brenland worker, wage 15 dalens an hour, 3,000 hours a year
to divide between work h and free time l. A benefit of 9,000 dalens a year is
withdrawn at 48% of earnings (30% after a reform); income tax TAX_BANDS (0 below
12,000, 20% to 40,000). Preferences u = (1 - a) ln c + a ln l.
"""

import math

W, T, B = 15.0, 3000.0, 9000.0


def net(earn, wr=0.48):
    ben = max(B - wr * earn, 0.0)
    tax = 0.2 * max(min(earn, 40000) - 12000, 0) + 0.35 * max(earn - 40000, 0)
    return earn - tax + ben


def segment_optimum(a, intercept, keep):
    """CD optimum on the line c = intercept + keep * W * h, ignoring its ends."""
    nw = keep * W
    full = intercept + nw * T
    leisure = a * full / nw
    return T - leisure, (1 - a) * full


def utility(a, c, leisure):
    return (1 - a) * math.log(c) + a * math.log(leisure)


def best(a, wr=0.48, step=0.1):
    n = int(2500 / step)
    hs = [i * step for i in range(n + 1)]
    return max(hs, key=lambda h: utility(a, net(W * h, wr), T - h))


def problem():
    h_ana, c_ana = segment_optimum(0.6, 9000, 0.52)
    h_new, c_new = segment_optimum(0.6, 9000, 0.70)
    e_old, e_new = W * h_ana, W * h_new
    out = {
        "c800": net(12000),
        "c1250": net(18750),
        "c1200": net(18000),
        "keep2": (net(18000) - net(12000)) / 6000,
        "h_ana": round(h_ana, 1),
        "c_ana": round(c_ana, 1),
        "u_ana": round(utility(0.6, c_ana, T - h_ana), 4),
        "u_kink1250": round(utility(0.6, 17400, 1750), 4),
        "h_new": round(h_new, 1),
        "c_new": round(c_new, 1),
        "ben_old": round(B - 0.48 * round(e_old, 1), 1),
        "ben_new": round(B - 0.30 * round(e_new, 1), 1),
        "ben_h1": segment_optimum(0.5, 9000, 0.52)[0],
        "ben_h2": segment_optimum(0.5, 11400, 0.32)[0],
        "ben_h3": segment_optimum(0.5, 2400, 0.80)[0],
        "prod_kink": 15240 * 2200,
        "prod_3": 19200 * 1600,
        "res_ana": round(1.5 * 9000 / 3000 / 0.52, 2),
        "res_ben": round(9000 / 3000 / 0.52, 2),
        "h18": round(T - 0.6 * (9000 + 0.52 * 18 * T) / (0.52 * 18), 1),
        "best_ana": best(0.6),
        "best_ben": best(0.5),
        "best_ana_new": best(0.6, 0.30),
        "best_ben_new": best(0.5, 0.30),
    }
    out["cost"] = round(out["ben_new"] - out["ben_old"], 1)
    return out


def saving(y1, y2, r, beta=0.96):
    wealth = y1 + y2 / (1 + r)
    c1 = wealth / (1 + beta)
    return {
        "wealth": round(wealth, 2),
        "c1": round(c1, 2),
        "s": round(y1 - c1, 2),
        "c2": round(beta * (1 + r) * c1, 2),
    }


def exercises():
    return {
        "res": 6000 / 3000,
        "h_log": lambda w, y: T / 2 - y / (2 * w),
        "c1_two": saving(30000, 20000, 0.05, 0.9),
    }


if __name__ == "__main__":
    print(problem())
    print(saving(16200, 12960, 0.04), saving(16200, 12960, 0.08))
    print(saving(9000, 30000, 0.04))
    print(exercises()["c1_two"], exercises()["h_log"](20, 6000))

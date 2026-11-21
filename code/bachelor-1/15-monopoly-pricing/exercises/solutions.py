"""Worked numbers of the exercises and weekend problem of b1 ch. 15.

Weekend problem: the ferry between Brenland and Kestria. Marginal cost 10 dalens a
trip. Residents: 4,000 people, each demanding 40 - p trips a year (160 - 4p thousand
trips). Tourists: 80 - p thousand trips. Money in thousands of dalens a year.
"""

import math

C = 10.0


def qr(p):
    return max(160 - 4 * p, 0.0)


def qt(p):
    return max(80 - p, 0.0)


def dwl_r(p):
    return 0.5 * (p - C) * (qr(C) - qr(p))


def dwl_t(p):
    return 0.5 * (p - C) * (qt(C) - qt(p))


def problem():
    p1 = (48 + C) / 2  # inverse demand p = 48 - Q/5 for p <= 40; MR = 48 - 2Q/5
    q1 = 240 - 5 * p1
    single = {
        "p": p1,
        "Q": q1,
        "qr": qr(p1),
        "qt": qt(p1),
        "profit": (p1 - C) * q1,
        "lerner": round((p1 - C) / p1, 4),
        "eps": round(-5 * p1 / q1, 4),
        "cs_r": 0.5 * qr(p1) * (40 - p1),
        "cs_t": 0.5 * qt(p1) * (80 - p1),
        "dwl": dwl_r(p1) + dwl_t(p1),
        "tourists_only": (45 - C) * qt(45),
    }
    pr, pt = (40 + C) / 2, (80 + C) / 2
    disc = {
        "pr": pr,
        "qr": qr(pr),
        "pt": pt,
        "qt": qt(pt),
        "eps_r": round(-4 * pr / qr(pr), 4),
        "eps_t": round(-pt / qt(pt), 4),
        "profit": (pr - C) * qr(pr) + (pt - C) * qt(pt),
        "cs_r": 0.5 * qr(pr) * (40 - pr),
        "cs_t": 0.5 * qt(pt) * (80 - pt),
        "dwl": dwl_r(pr) + dwl_t(pt),
    }
    fee = 0.5 * (40 - C) ** 2
    pas = {
        "fee": fee,
        "trips_each": 40 - C,
        "qr": qr(C),
        "profit_r": 4000 * fee / 1000,
        "profit": 4000 * fee / 1000 + (pt - C) * qt(pt),
        "dwl": dwl_t(pt),
        "removed": round(100 * (single["dwl"] - dwl_t(pt)) / single["dwl"], 2),
    }
    F = 1500.0
    # average-cost price: (p - C)(240 - 5p) = F, smaller root
    a, b, c = 5, -(240 + 5 * C), 240 * C + F
    pac = (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a)
    cap1 = pac * (1 + 0.02 - 0.03)
    reg = {
        "Q_mc": 240 - 5 * C,
        "loss_mc": -F,
        "pac": round(pac, 2),
        "Qac": round(240 - 5 * pac, 2),
        "dwl_ac": round(dwl_r(pac) + dwl_t(pac), 2),
        "profit_monopoly": (p1 - C) * q1 - F,
        "cap1": round(cap1, 2),
        "profit_cap_cut": round((cap1 - 9) * (240 - 5 * cap1) - F, 2),
        "profit_cap_nocut": round((cap1 - C) * (240 - 5 * cap1) - F, 2),
    }
    return {"single": single, "disc": disc, "pass": pas, "reg": reg}


def exercises():
    # q1 = 100 - p, q2 = 60 - p, MC 20
    disc_w = 0.5 * 40 * 40 + 0.5 * 20 * 20 + 40 * 40 + 20 * 20
    single_w = 0.5 * 50 * 50 + 0.5 * 10 * 10 + 30 * 60
    best_w = 0.5 * 80 * 80 + 0.5 * 40 * 40
    return {
        "mono": {"q": 40, "p": 60, "profit": 40 * 40, "dwl": 0.5 * 40 * 40},
        "lerner": (0.25, round(1 / 0.75, 4)),
        "disc": {
            "p1": 60,
            "q1": 40,
            "p2": 40,
            "q2": 20,
            "single_p": 50,
            "single_q1": 50,
            "single_q2": 10,
        },
        "welfare": {
            "disc": disc_w,
            "single": single_w,
            "dwl_disc": best_w - disc_w,
            "dwl_single": best_w - single_w,
        },
        "two_part": {"p": 2, "fee": 0.5 * 8 * 8},
        "bundle": {"separate": max(2 * 8, 2 * 2 * 3), "bundle": 2 * 11},
        "ramsey": {
            "p": (120 - math.sqrt(120**2 - 4 * 3200)) / 2,
            "q": 60,
            "dwl": 0.5 * 20 * 20,
        },
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())

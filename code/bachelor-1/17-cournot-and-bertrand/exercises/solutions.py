"""Worked numbers of the exercises and weekend problem of b1 ch. 17.

Weekend problem: ferries to the islands. An island of S thousand people demands
Q = S (60 - p) thousand trips a year; a ferry's marginal cost is 20 a trip and its fixed
cost 800 thousand dalens a year. Money in thousands of dalens a year.
"""

A, C, F = 60.0, 20.0, 800.0


def cournot(S, n):
    q = S * (A - C) / (n + 1)
    Q = n * q
    p = A - Q / S
    return {
        "q": round(q, 2),
        "Q": round(Q, 2),
        "p": round(p, 2),
        "profit": round((p - C) * q - F, 2),
    }


def threshold(n):
    """Smallest S at which n Cournot ferries break even."""
    return F * (n + 1) ** 2 / (A - C) ** 2


def problem():
    a = cournot(4, 1)
    b2 = cournot(9, 2)
    p2 = A - 240 / 9
    eps = -p2 / (A - p2)
    stack_q1 = 9 * (A - C) / 2
    stack_q2 = (9 * (A - C) - stack_q1) / 2
    stack_p = A - (stack_q1 + stack_q2) / 9
    s = [threshold(n) for n in range(1, 5)]
    per = [s[n - 1] / n for n in range(1, 5)]
    n_b = max(n for n in range(1, 10) if threshold(n) <= 9)
    return {
        "A": a,
        "A_lerner": 0.5,
        "A_eps": -40 / 20,
        "A_cs": 0.5 * 80 * 20,
        "A_dwl": 0.5 * 80 * 20,
        "B2": b2,
        "B2_lerner": round((p2 - C) / p2, 4),
        "B2_eps": round(eps, 4),
        "B2_cs": round(0.5 * 240 * (A - p2), 1),
        "B_mono": cournot(9, 1),
        "stackelberg": {
            "q1": stack_q1,
            "q2": stack_q2,
            "p": stack_p,
            "pi1": (stack_p - C) * stack_q1 - F,
            "pi2": (stack_p - C) * stack_q2 - F,
        },
        "thresholds": s,
        "per_firm": [round(x, 3) for x in per],
        "ratios": [round(per[i + 1] / per[i], 3) for i in range(3)],
        "n_on_B": n_b,
        "B3": cournot(9, 3),
        "S3_over_S1": s[2] / s[0],
    }


def exercises():
    a, c = 120.0, 30.0

    def ts(n):
        Q = n * (a - c) / (n + 1)
        return (a - c) * Q - Q**2 / 2

    return {
        "duo": {"q": 30, "Q": 60, "p": 60, "profit": 900},
        "third": c + (a - c) / 4,
        "ts": [ts(n) for n in (1, 2, 3)],
        "ts_max": (a - c) ** 2 / 2,
        "stackelberg": {
            "q1": 45,
            "q2": 22.5,
            "p": 52.5,
            "pi1": 45 * 22.5,
            "pi2": 22.5 * 22.5,
        },
        "diff": {"p": 40, "q": 60, "profit": 30 * 60},
        "dentists": round(2.54 / 2 / 0.71, 2),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())

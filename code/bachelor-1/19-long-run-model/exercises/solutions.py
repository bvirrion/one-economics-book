"""Worked numbers of the exercises and weekend problem of b1 ch. 19.

Weekend problem: Brenland in the long run, calibrated to the shares of 2025 in
accounts.csv. Y = A K^0.35 L^0.65 with K = 1,000 (billions of dalens) and L = 4.4
(million workers), Y = 400; C = 36 + 0.6 (Y - T), T = 80, G = 80, I = 132 - 10 r (r in
per cent).
"""

import country


def lf(Y, T, G, a=36.0, b=0.6, i0=132.0, i1=10.0):
    C = a + b * (Y - T)
    S = Y - C - G
    r = (i0 - S) / i1
    return {
        "C": round(C, 3),
        "S": round(S, 3),
        "r": round(r, 3),
        "I": round(S, 3),
        "private": round(Y - T - C, 3),
        "public": T - G,
    }


def problem():
    Y, K, L, al = 400.0, 1000.0, 4.4, 0.35
    A = Y / (K**al * L ** (1 - al))
    w = (1 - al) * Y / L
    rk = al * Y / K
    base = lf(Y, 80, 80)
    debt = lf(Y, 80, 88)
    tax = lf(Y, 88, 88)
    tech = lf(1.1 * Y, 80, 80)
    a = country.load("accounts").set_index("year").loc[2025]
    return {
        "A": round(A, 4),
        "w": round(w, 2),
        "rk": rk,
        "euler": w * L + rk * K,
        "immig": (round(1.1 ** (-al), 4), round(1.1 ** (1 - al), 4)),
        "base": base,
        "debt": debt,
        "tax": tax,
        "tech": tech,
        "shares": {k: round(a[k] / a.gdp, 3) for k in ("C", "I", "G")},
        "tech_w": round(1.1 * w, 2),
        "tech_rk": round(1.1 * rk, 3),
    }


def exercises():
    K, L = 100.0, 400.0
    Y = 10 * K**0.3 * L**0.7
    a = country.load("accounts").set_index("year").loc[2025]
    C1 = 100 + 0.6 * (2000 - 300)
    S1 = 2000 - C1 - 300
    C2 = 100 + 0.6 * (2000 - 250)
    S2 = 2000 - C2 - 300
    return {
        "Y": round(Y, 2),
        "w": round(0.7 * Y / L, 3),
        "r": round(0.3 * Y / K, 3),
        "euler": round(0.7 * Y / L * L + 0.3 * Y / K * K, 2),
        "lf": {"C": C1, "S": S1, "r": (700 - S1) / 20},
        "taxcut": {"C": C2, "S": S2, "r": (700 - S2) / 20},
        "immig": (round(1.1**-0.3, 4), round(1.1**0.7, 4)),
        "brenland": {"S": a.gdp - a.C - a.G, "I": a.I, "NX": a.X - a.M},
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())

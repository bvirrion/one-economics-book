"""Book 4, chapter 6 (exchange economies): every number the text and solutions print.

Two consumers with Cobb-Douglas utilities a ln x1 + (1 - a) ln x2; p is the price of
good 1 in units of good 2 (good 2 is the numeraire).
"""

import math


def demand(a, w1, w2, p):
    """Cobb-Douglas demand at price p of good 1 (good 2 = 1): (x1, x2)."""
    m = p * w1 + w2
    return a * m / p, (1 - a) * m


def eq_price(a, wa, b, wb):
    """Equilibrium p for shares a, b and endowments wa = (w1, w2), wb."""
    return (a * wa[1] + b * wb[1]) / ((1 - a) * wa[0] + (1 - b) * wb[0])


def contract_x2(a, b, tot, x1):
    """Contract curve: consumer A's good 2 as a function of A's good 1."""
    t1, t2 = tot
    return b * (1 - a) * t2 * x1 / (a * (1 - b) * (t1 - x1) + b * (1 - a) * x1)


def cd_u(a, x1, x2):
    return a * math.log(x1) + (1 - a) * math.log(x2)


def bisect(f, lo, hi, n=100):
    flo = f(lo)
    for _ in range(n):
        mid = (lo + hi) / 2
        if (f(mid) > 0) == (flo > 0):
            lo, flo = mid, f(mid)
        else:
            hi = mid
    return (lo + hi) / 2


def text_example():
    """Section 6.3: a = 1/2 with (8, 2); b = 2/3 with (2, 8)."""
    a, b, wa, wb = 0.5, 2 / 3, (8, 2), (2, 8)
    p = eq_price(a, wa, b, wb)
    xa, xb = demand(a, *wa, p), demand(b, *wb, p)
    ua_w = wa[0] * wa[1]  # A's indifference curve x1 x2 = const through the endowment
    ub_w = (10 - wa[0]) ** 2 * (10 - wa[1])  # B's, in A's coordinates

    def on_a(x1):
        return x1 * contract_x2(a, b, (10, 10), x1) - ua_w

    def on_b(x1):
        return (10 - x1) ** 2 * (10 - contract_x2(a, b, (10, 10), x1)) - ub_w

    core_lo = bisect(on_a, 0.5, 9.5)
    core_hi = bisect(on_b, 0.5, 9.5)
    return {
        "p": p,
        "xa": xa,
        "xb": xb,
        "ica": xa[0] * xa[1],
        "icb": (10 - xa[0]) ** 2 * (10 - xa[1]),
        "core": (core_lo, core_hi),
        "core_x2": (
            contract_x2(a, b, (10, 10), core_lo),
            contract_x2(a, b, (10, 10), core_hi),
        ),
        "mrs_w": (wa[1] / wa[0], 2 * wb[1] / wb[0]),
    }


R3 = 2 ** (8 / 9) - 2 ** (1 / 9)


def z3(p, r=R3):
    """Excess demand for good 1 in the three-equilibrium economy, p = p1/p2."""
    return (r - p ** (1 / 9)) / p + p ** (-1 / 9) - r


def three():
    h = 1e-6
    slopes = {q: (z3(q + h) - z3(q - h)) / (2 * h) for q in (0.5, 1.0, 2.0)}
    return {"r": R3, "z": {q: z3(q) for q in (0.5, 1.0, 2.0)}, "slope": slopes}


# ---- exercises -------------------------------------------------------------


def ex_feasible():
    tot = (10, 10)
    cases = {
        "i": ((4, 7), (6, 3)),
        "ii": ((5, 5), (6, 4)),
        "iii": ((3, 2), (6, 7)),
    }
    out = {}
    for k, (xa, xb) in cases.items():
        s = (xa[0] + xb[0], xa[1] + xb[1])
        out[k] = (s, s == tot, s[0] <= tot[0] and s[1] <= tot[1])
    return out


def ex_mrs():
    """u_A = x1 x2 at (4, 6); u_B = x1 x2^2 at (6, 4)."""
    return {"mrs_a": 6 / 4, "mrs_b": 4 / (2 * 6)}


def ex_cd_eq():
    """u_A = ln x1 + ln x2, (6, 2); u_B = ln x1 + 3 ln x2, (4, 8)."""
    a, b, wa, wb = 0.5, 0.25, (6, 2), (4, 8)
    p = eq_price(a, wa, b, wb)
    return {"p": p, "xa": demand(a, *wa, p), "xb": demand(b, *wb, p)}


def ex_contract():
    a, b = 0.5, 0.25
    return {x: contract_x2(a, b, (10, 10), x) for x in (2, 5, 8)}


def ex_transfer():
    """a = 0.5 with (6, 2), b = 0.25 with (4, 8); move 2 of good 2 from B to A."""
    p0 = eq_price(0.5, (6, 2), 0.25, (4, 8))
    p1 = eq_price(0.5, (6, 4), 0.25, (4, 6))
    return {"p0": p0, "p1": p1, "dp": p1 - p0, "formula": (0.5 - 0.25) * 2 / 6}


def ex_walras():
    a, b, wa, wb, p = 0.5, 0.25, (6, 2), (4, 8), 1.0
    xa, xb = demand(a, *wa, p), demand(b, *wb, p)
    z1 = xa[0] + xb[0] - 10
    z2 = xa[1] + xb[1] - 10
    return {"z1": z1, "z2": z2, "value": p * z1 + z2}


def problem():
    a, b = 0.5, 0.25  # Brenland (fish share), Kestria
    wa, wb, tot = (60, 10), (20, 90), (80, 100)
    mrs_w = (a / (1 - a) * wa[1] / wa[0], b / (1 - b) * wb[1] / wb[0])
    trade_a = cd_u(a, 50, 15) - cd_u(a, *wa)
    trade_b = cd_u(b, 30, 85) - cd_u(b, *wb)

    def on_a(x):
        return cd_u(a, x, contract_x2(a, b, tot, x)) - cd_u(a, *wa)

    def on_b(x):
        return cd_u(b, 80 - x, 100 - contract_x2(a, b, tot, x)) - cd_u(b, *wb)

    core = (bisect(on_a, 1, 79), bisect(on_b, 1, 79))
    p = eq_price(a, wa, b, wb)
    xa, xb = demand(a, *wa, p), demand(b, *wb, p)
    ev_a = xa[0] ** a * xa[1] ** (1 - a) / wa[0] ** a
    ev_a = ev_a ** (1 / (1 - a)) - wa[1]
    ev_b = (xb[0] ** b * xb[1] ** (1 - b) / wb[0] ** b) ** (1 / (1 - b)) - wb[1]
    wa2, wb2 = (60, 20), (20, 80)
    p2 = eq_price(a, wa2, b, wb2)
    xa2, xb2 = demand(a, *wa2, p2), demand(b, *wb2, p2)
    return {
        "mrs_w": mrs_w,
        "trade": (trade_a, trade_b),
        "core": core,
        "core_x2": tuple(contract_x2(a, b, tot, x) for x in core),
        "p": p,
        "income": (p * wa[0] + wa[1], p * wb[0] + wb[1]),
        "xa": xa,
        "xb": xb,
        "u": (cd_u(a, *xa), cd_u(b, *xb), cd_u(a, *wa), cd_u(b, *wb)),
        "ev": (ev_a, ev_b),
        "p2": p2,
        "xa2": xa2,
        "xb2": xb2,
        "u2": (cd_u(a, *xa2), cd_u(b, *xb2)),
        "x2_check": contract_x2(a, b, tot, xa2[0]),
    }

"""Book 4, chapter 7 (welfare theorems): every number the text and solutions print."""

import math


def crusoe(T=16.0, A=4.0, a=0.5):
    """u = a ln c + (1 - a) ln(T - L), c = A sqrt(L): planner and prices."""
    L = a * T / (2 - a)
    c = A * math.sqrt(L)
    w = A / (2 * math.sqrt(L))
    profit = c - w * L
    income = w * T + profit
    return {
        "L": L,
        "c": c,
        "w": w,
        "profit": profit,
        "income": income,
        "leisure": T - L,
    }


def nonconvex(T=10.0):
    """c = L^2 / 10 (increasing returns), u = ln c + ln(T - L)."""
    L = 2 * T / 3
    c = L**2 / 10
    w = 2 * L / 10
    return {"L": L, "c": c, "w": w, "profit": c - w * L, "ic": c * (T - L)}


def ex_gap():
    fall = 22.0 - 13.9
    tfall = 9.9 - 7.6
    return {"fall": fall, "tfall": tfall, "share": tfall / fall, "res": (8.4, 3.5)}


def ex_profit(p=3.0, w=1.0):
    """y = 2 sqrt(L): p / sqrt(L) = w."""
    L = (p / w) ** 2
    y = 2 * math.sqrt(L)
    return {"L": L, "y": y, "profit": p * y - w * L}


def ex_tech():
    before, after = crusoe(A=4), crusoe(A=5)
    return {"before": before, "after": after}


def ex_transfer(x1=6.0):
    """Chapter 6 running example: a = 1/2 with (8, 2), b = 2/3 with (2, 8)."""
    a, b = 0.5, 2 / 3
    x2 = b * (1 - a) * 10 * x1 / (a * (1 - b) * (10 - x1) + b * (1 - a) * x1)
    p = (a / (1 - a)) * x2 / x1
    need = p * x1 + x2
    have = p * 8 + 2
    m_b = p * 2 + 8 + (have - need)
    return {
        "x2": x2,
        "p": p,
        "need": need,
        "have": have,
        "T": need - have,
        "xb": (b * m_b / p, (1 - b) * m_b),
    }


def ex_second(a=0.5, b=0.25, tot=(100.0, 100.0), wa=(80.0, 10.0), x1=40.0):
    """General Cobb-Douglas second-theorem transfer (in units of good 2)."""
    t1, t2 = tot
    x2 = b * (1 - a) * t2 * x1 / (a * (1 - b) * (t1 - x1) + b * (1 - a) * x1)
    p = (a / (1 - a)) * x2 / x1
    T = (p * x1 + x2) - (p * wa[0] + wa[1])
    return {"x2": x2, "p": p, "T": T}


def towns(t, a_dem=100, b_dem=200, s=10, d=10):
    """Ardel supplies s p_A, demands a_dem - d p_A; Brenmoor demands b_dem - d p_B."""
    pa = (b_dem - d * t + a_dem) / (s + 2 * d)
    pb = pa + t
    x = b_dem - d * pb
    q = s * pa
    cs_b = 0.5 * x * (b_dem / d - pb)
    q_a = a_dem - d * pa
    cs_a = 0.5 * q_a * (a_dem / d - pa)
    ps = 0.5 * q * pa  # profit 5 p^2 with s = 10 (area above the supply curve)
    return {
        "pa": pa,
        "pb": pb,
        "x": x,
        "q": q,
        "q_a": q_a,
        "cs_b": cs_b,
        "cs_a": cs_a,
        "ps": ps,
        "total": cs_a + cs_b + ps,
        "freight": t * x,
    }


def problem():
    road, rail = towns(6), towns(2)
    labour = road["q"] ** 2 / 20
    tr = ex_second()
    a, b = 0.5, 0.25
    pe = (a * 10 + b * 90) / ((1 - a) * 80 + (1 - b) * 20)
    xa_e = (a * (pe * 80 + 10) / pe, (1 - a) * (pe * 80 + 10))
    return {
        "road": road,
        "rail": rail,
        "labour": labour,
        "gain": rail["total"] - road["total"],
        "pe": pe,
        "xa_e": xa_e,
        "transfer": tr,
        "xb_target": (100 - 40, 100 - tr["x2"]),
    }

"""Worked numbers of the exercises and weekend problem of b1 ch. 6.

Weekend problem: three kinds of Brenland household (equal numbers) with
Cobb--Douglas preferences over fuel f (litres) and other spending o; fuel
costs 2 dalens a litre and a levy of 0.5 raises it to 2.5; the revenue may
come back as an equal cheque."""

from scipy.optimize import brentq

P0, P1 = 2.0, 2.5
HH = {"A": (20000, 0.10), "B": (30000, 0.08), "C": (50000, 0.06)}


def fuel(m, a, p):
    return a * m / p


def exact_comp(m, a):
    """e(p1, u0) - m for Cobb--Douglas: m * ((P1 / P0) ** a - 1)."""
    return m * ((P1 / P0) ** a - 1)


def household(name):
    m, a = HH[name]
    f0, f1 = fuel(m, a, P0), fuel(m, a, P1)
    m_s = m + (P1 - P0) * f0
    f_s = fuel(m_s, a, P1)
    cv = exact_comp(m, a)
    f_h = fuel(m + cv, a, P1)
    return {
        "f0": f0,
        "f1": f1,
        "m_s": m_s,
        "f_s": f_s,
        "sub_s": f_s - f0,
        "inc_s": f1 - f_s,
        "cv": round(cv, 1),
        "f_h": round(f_h, 1),
        "sub_h": round(f_h - f0, 1),
        "inc_h": round(f1 - f_h, 1),
    }


def with_cheque():
    """Equal cheque c = levy revenue / 3.

    F = sum a (m + c) / P1 with c = (P1 - P0) F / 3.
    """
    tau = P1 - P0

    def gap(F):
        c = tau * F / 3
        return sum(fuel(m + c, a, P1) for m, a in HH.values()) - F

    F = brentq(gap, 1000, 5000)
    c = tau * F / 3
    F0 = sum(fuel(m, a, P0) for m, a in HH.values())
    F1 = sum(fuel(m, a, P1) for m, a in HH.values())
    cvs = {k: round(exact_comp(*v), 1) for k, v in HH.items()}
    fh = {k: household(k)["f_h"] for k in HH}
    return {
        "F0": F0,
        "F1": F1,
        "rev1": tau * F1,
        "F": round(F, 1),
        "c": round(c, 1),
        "fall": round(100 * (1 - F / F0), 1),
        "fall_no": round(100 * (1 - F1 / F0), 1),
        "cv": cvs,
        "cv_sum": round(sum(cvs.values()), 1),
        "FH": round(sum(fh.values()), 1),
        "fall_h": round(100 * (1 - sum(fh.values()) / F0), 1),
        "gain": {k: round(round(c, 1) - v, 1) for k, v in cvs.items()},
    }


def proportional_cheque():
    """Cheque k * m: P1 F = sum a m (1 + k), with k * sum m = (P1 - P0) F."""
    am = sum(a * m for m, a in HH.values())
    total_m = sum(m for m, _ in HH.values())
    F = am / (P1 - am * (P1 - P0) / total_m)
    F0 = sum(fuel(m, a, P0) for m, a in HH.values())
    return {"F": round(F, 2), "fall": round(100 * (1 - F / F0), 1)}


def exercises():
    # star: u = x1 x2 (a = 1/2), m = 100, p2 = 1, p1 from 1 to 2
    x0 = 0.5 * 100 / 1
    x1 = 0.5 * 100 / 2
    m_s = 100 + (2 - 1) * x0
    xs = 0.5 * m_s / 2
    m_h = 100 * 2**0.5
    xh = 0.5 * m_h / 2
    return {
        "x0": x0,
        "x1": x1,
        "xs": xs,
        "sub_s": xs - x0,
        "inc_s": x1 - xs,
        "m_h": round(m_h, 2),
        "xh": round(xh, 2),
        "sub_h": round(xh - x0, 2),
        "inc_h": round(x1 - xh, 2),
    }


if __name__ == "__main__":
    for k in HH:
        print(k, household(k))
    print(with_cheque())
    print(proportional_cheque())
    print(exercises())

"""Worked numbers for the text, exercises and problem of Book 4, chapter 23."""

from math import log, sqrt


def steady(alpha, delta, rho, n):
    k = (alpha / (rho + delta)) ** (1 / (1 - alpha))
    y = k**alpha
    c = y - (n + delta) * k
    return {"k": k, "y": y, "c": c, "s": (n + delta) * k / y}


def golden(alpha, delta, n):
    return (alpha / (n + delta)) ** (1 / (1 - alpha))


def eigen(alpha, delta, rho, n, theta):
    st = steady(alpha, delta, rho, n)
    f2 = alpha * (alpha - 1) * st["k"] ** (alpha - 2)
    a, b = rho - n, st["c"] * f2 / theta  # J = [[a, -1], [b, 0]]
    disc = sqrt(a * a + 4 * (-b))
    lam_pos, lam_neg = (a + disc) / 2, (a - disc) / 2
    return {"a": a, "b": b, "pos": lam_pos, "neg": lam_neg, "half": log(2) / -lam_neg}


def euler_growth(r, rho, theta):
    return (r - rho) / theta


def kestria():
    p = (0.3, 0.06, 0.04, 0.0)
    st = steady(*p)
    e = eigen(*p, theta=2)
    return {
        **st,
        "kg": golden(0.3, 0.06, 0.0),
        "r": 0.3 * st["k"] ** (0.3 - 1) - 0.06,
        "wage": 0.7 * st["y"],
        **{f"e_{k}": v for k, v in e.items()},
        "c_after_g": st["c"] - 0.1,
        "half_theta4": eigen(*p, theta=4)["half"],
    }


def initial_saving(alpha, delta, rho, n, theta, share=0.25):
    """Saving rate at the start of the saddle path from share * k*, by shooting."""
    k_star = steady(alpha, delta, rho, n)["k"]
    k0 = share * k_star

    def fate(c, k, dt=0.01):
        for _ in range(20000):
            dk = k**alpha - c - (n + delta) * k
            dc = c * (alpha * k ** (alpha - 1) - delta - rho) / theta
            if dk < 0:
                return "high"
            if dc < 0:
                return "low"
            k, c = k + dk * dt, c + dc * dt
        return "on"

    lo, hi = 0.0, k0**alpha
    for _ in range(50):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if fate(mid, k0) == "low" else (lo, mid)
    return 1 - lo / k0**alpha

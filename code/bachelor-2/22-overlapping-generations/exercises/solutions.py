"""Worked numbers for the text, exercises and problem of Book 4, chapter 22."""


def steady_k(alpha, beta, n, a=1.0):
    return (beta * (1 - alpha) * a / ((1 + beta) * (1 + n))) ** (1 / (1 - alpha))


def ratio_r_to_growth(alpha, beta):
    """Gross return over 1 + n in the steady state without pensions."""
    return alpha * (1 + beta) / (beta * (1 - alpha))


def golden_k(alpha, n, a=1.0):
    return (alpha * a / (1 + n)) ** (1 / (1 - alpha))


def per_year(gross, years=30):
    return gross ** (1 / years) - 1


def contribution(dependency, replacement):
    return dependency * replacement


def contributions_2025(replacement=0.5):
    oadr = {"JPN": 51.0, "ITA": 39.7, "KOR": 29.3, "USA": 28.5, "NGA": 5.4}
    return {k: contribution(v / 100, replacement) for k, v in oadr.items()}


def brenland():
    alpha, beta, n, a, d = 0.3, 0.6, 0.2, 10.0, 1.0
    k = steady_k(alpha, beta, n, a)
    w = (1 - alpha) * a * k**alpha
    r = alpha * a * k ** (alpha - 1)
    s = beta / (1 + beta) * w
    k_payg = 2.059  # from the listing
    w_payg = (1 - alpha) * a * k_payg**alpha
    r_payg = alpha * a * k_payg ** (alpha - 1)
    return {
        "k": k,
        "w": w,
        "R": r,
        "s": s,
        "c_young": w - s,
        "c_old": r * s,
        "r_year": per_year(r),
        "n_year": per_year(1 + n),
        "k_golden": golden_k(alpha, n, a),
        "w_payg": w_payg,
        "R_payg": r_payg,
        "s_payg": (1 + n) * k_payg,
        "pension": (1 + n) * d,
        "implicit_tax": d - (1 + n) * d / r_payg,
        "tau_now": contribution(0.30, 0.5),
        "tau_2050": contribution(0.45, 0.5),
        "repl_kept": 0.15 / 0.45,
        "tau_later_retire": contribution(0.35, 0.5),
    }

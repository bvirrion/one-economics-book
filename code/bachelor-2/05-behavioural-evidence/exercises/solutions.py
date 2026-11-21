"""Book 4, chapter 5 (behavioural evidence): every number the solutions print.

Symbols as in the chapter: kappa is the loss-aversion coefficient, eta the curvature
of the value function, d the parameter of the weighting function omega(p), chi a
switching cost. Parameter values marked illustrative are not estimates.
"""

import math
from statistics import NormalDist

PHI = NormalDist()
ETA, KAPPA, D = 0.9, 2.0, 0.65  # illustrative values used throughout the chapter


def weight(p, d=D):
    """Probability weighting omega(p) = p^d / (p^d + (1-p)^d)^(1/d)."""
    return p**d / (p**d + (1 - p) ** d) ** (1 / d)


def value(x, eta=ETA, kappa=KAPPA):
    return x**eta if x >= 0 else -kappa * (-x) ** eta


def crossing(d=D):
    """The p at which omega(p) = p, by bisection on (0.01, 0.99)."""
    lo, hi = 0.01, 0.99
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if weight(mid, d) > mid else (lo, mid)
    return lo


def allais():
    """Common ratio (chapter 1) under prospect theory with the illustrative values."""
    return {
        "w80": weight(0.8),
        "w20": weight(0.2),
        "w25": weight(0.25),
        "A": weight(0.8) * 4000**ETA,
        "B": 3000**ETA,
        "C": weight(0.2) * 4000**ETA,
        "D": weight(0.25) * 3000**ETA,
    }


def ex_replication():
    """Exercise 1: counts read from Camerer et al. (2016), Table S1."""
    orig = [0.18, 0.31, 0.72, 0.38, 0.84, 0.12, 0.76, 0.72, 0.21]
    orig += [0.45, 0.64, 0.30, 0.83, 0.28, 0.49, 0.66, 0.32, 0.28]
    rep = [0.08, 0.23, 0.66, 0.36, 0.17, 0.27, -0.12, 0.73, 0.12]
    rep += [0.31, 0.44, 0.33, 0.37, -0.01, 0.34, 0.53, 0.30, -0.12]
    below = sum(r < o for o, r in zip(orig, rep))
    return {
        "below": below,
        "negative": sum(r < 0 for r in rep),
        "rate": 11 / 18,
        "mean_orig": sum(orig) / 18,
        "mean_rep": sum(rep) / 18,
    }


def ex_mixed():
    return {"v150": 0.5 * 150 - 0.5 * KAPPA * 100, "min_g": KAPPA * 100}


def ex_endowment(u=5.0, kappa=KAPPA):
    return {"wta": kappa * u, "wtp_goods": u, "wtp_both": u / kappa}


def ex_prospect():
    g, loss = 1000**ETA, 400**ETA
    return {"g": g, "l": loss, "v": 0.5 * g - 0.5 * KAPPA * loss, "ev": 300}


def ex_default(n=2000):
    return {
        "in": 0.37 * n,
        "out": 0.86 * n,
        "extra": (0.86 - 0.37) * n,
        "at_default": 0.61 * n,
        "pay": 0.61 * n * 0.03 * 30000,
    }


def ex_salience():
    a, b, p, t = 1600, 40, 20, 2
    posted = a - b * (p + t)
    unposted = posted / 0.92
    theta = (a - b * p - unposted) / (b * t)
    return {"posted": posted, "unposted": unposted, "theta": theta}


def ex_fourfold(d=D):
    w = {p: weight(p, d) for p in (0.01, 0.05, 0.5, 0.9, 0.99)}
    return {
        "w": w,
        "gain_low": w[0.01] * 1000,  # 1% chance of 1000 against 10 for sure
        "gain_high": w[0.99] * 1000,  # 99% chance of 1000 against 990 for sure
        "loss_low": -w[0.01] * 1000,
        "loss_high": -w[0.99] * 1000,
    }


def ex_eu_endowment(m=30000.0, wtp=5.0):
    """u = log(money) + b * mug: WTP = m(1 - e^-b), WTA = m(e^b - 1), ratio e^b."""
    b = -math.log(1 - wtp / m)
    wta = m * (math.exp(b) - 1)
    return {"b": b, "wta": wta, "ratio": wta / wtp, "gap": wta - wtp}


def ex_labour(target=200, c=4, kappa=KAPPA):
    lo, hi = math.sqrt(c * target / kappa), math.sqrt(c * target)
    hours = {}
    for w in (16, 20, 25, 28, 32):
        if w * (kappa * w / c) <= target:
            h = kappa * w / c
        elif w * (w / c) >= target:
            h = w / c
        else:
            h = target / w
        hours[w] = h
    return {"lo": lo, "hi": hi, "hours": hours}


def problem():
    lam_lin = 200 / 100
    lam_curv = 2**ETA
    rabin = (100 + 125) * 125 / (125 - 100)
    wta, wtp = 8.0, 3.5
    k_goods = wta / wtp
    k_both = math.sqrt(k_goods)
    a = PHI.inv_cdf(1 - 0.37)  # chi - mu
    b = PHI.inv_cdf(1 - 0.86)  # -chi - mu
    chi = (a - b) / 2
    mu = chi - a
    mu_b = chi - PHI.inv_cdf(1 - 0.45)
    p_out = PHI.cdf(mu_b + chi)
    contrib_in = 0.45 * 6
    contrib_out = 0.61 * 3 + (p_out - 0.61) * 6
    worse_out = p_out - PHI.cdf(mu_b)
    miss_in = PHI.cdf(mu_b) - 0.45
    w05 = weight(0.05)
    k_needed = 100 / (w05 * 500)
    share_low = 1 - PHI.cdf((math.log(k_needed) - math.log(2)) / 0.35)
    return {
        "lam_lin": lam_lin,
        "lam_curv": lam_curv,
        "rabin": rabin,
        "k_goods": k_goods,
        "k_both": k_both,
        "a": a,
        "b": b,
        "chi": chi,
        "mu": mu,
        "mu_b": mu_b,
        "p_out": p_out,
        "gap": p_out - 0.45,
        "contrib_in": contrib_in,
        "contrib_out": contrib_out,
        "worse_out": worse_out,
        "miss_in": miss_in,
        "ev_low": 0.05 * 500,
        "w05": w05,
        "k_needed": k_needed,
        "share_low": share_low,
    }

"""Worked numbers of the text, exercises and weekend problem of b1 ch. 3
(comparative statics), with exact solutions found by root-finding."""

import math

from scipy.integrate import quad
from scipy.optimize import brentq


def linear_tax(a=100.0, b=2.0, d=3.0, tau=0.0):
    """Demand q = a - b p, supply q = d (p - tau): equilibrium and pass-through."""
    p = (a + d * tau) / (b + d)
    return {"p": p, "q": a - b * p, "pass": d / (b + d)}


def tax_figure(tau=5.0):
    """The two panels: q = 100 - 2p and q = 70 - 0.5p against q = 3(p - tau)."""
    out = {}
    for name, a, b in (("elastic", 100.0, 2.0), ("inelastic", 70.0, 0.5)):
        p0 = a / (b + 3)
        p1 = (a + 3 * tau) / (b + 3)
        out[name] = {
            "p0": p0,
            "q0": a - b * p0,
            "p1": p1,
            "q1": a - b * p1,
            "eps_d": -b * p0 / (a - b * p0),
            "pass": 3 / (b + 3),
        }
    return out


def pass_through(eps_d, eps_s):
    return eps_s / (eps_s - eps_d)


def ex_ce(p=4.0):
    """Exercise 1: q = 50 p^-0.5: elasticity and two quantities."""
    return {"eps": -0.5, "q4": 50 * p**-0.5, "q4_4": 50 * 4.4**-0.5}


def ex_envelope(a=4.0):
    """Exercise 7: V(a) = max_x (a x - x^2) = a^2/4; V'(a) = x*(a) = a/2."""
    return {"x": a / 2, "V": a * a / 4, "dV": a / 2}


def monopoly_pass(eps=2.0, c=10.0, tau=1.0):
    """Exercise 11: constant elasticity e, marginal cost c: p = (c + tau) e/(e - 1)."""
    m = eps / (eps - 1)
    return {"markup": m, "p0": c * m, "p1": (c + tau) * m, "pass": m}


# ---- the weekend problem: Kestria's cement ---------------------------------------
P0, Q0, ED, ES = 100.0, 1000.0, 0.5, 1.2


def cement_demand(p):
    return Q0 * (p / P0) ** -ED


def cement_supply(ps):
    return Q0 * (ps / P0) ** ES


def cement_exact(tau):
    """Constant-elasticity version: buyers pay p, sellers keep p - tau."""
    p = brentq(lambda x: cement_demand(x) - cement_supply(x - tau), tau + 1e-9, 1000.0)
    return {"p": p, "q": cement_demand(p), "ps": p - tau}


def cement_linear(tau):
    """Linear version, tangent at (100, 1000): Q = 1500 - 5p, Q = 12(p - tau) - 200."""
    p = (1700 + 12 * tau) / 17
    return {"p": p, "q": 1500 - 5 * p, "ps": p - tau}


def cement(tau=10.0):
    pt = ES / (ES + ED)
    dp = round(pt * tau, 2)
    dlnq = -ED * dp / P0
    exact = cement_exact(tau)
    lin = cement_linear(tau)
    # producers' profit: Pi(ps) with Pi'(ps) = S(ps) (envelope); exact loss = integral
    ps_r, p_r, q_r = round(exact["ps"], 2), round(exact["p"], 2), round(exact["q"], 1)
    loss_exact = quad(cement_supply, ps_r, P0)[0]
    return {
        "pass": round(pt, 4),
        "dp_first": dp,
        "p_first": P0 + dp,
        "ps_first": round(P0 + dp - tau, 2),
        "dq_first_pct": round(100 * dlnq, 2),
        "q_first": round(Q0 * (1 + dlnq), 1),
        "p_exact": round(exact["p"], 2),
        "q_exact": round(exact["q"], 1),
        "ps_exact": round(exact["ps"], 2),
        "p_lin": round(lin["p"], 2),
        "q_lin": round(lin["q"], 1),
        "profit_loss_first": round(Q0 * (tau - dp), 0),
        "profit_loss_exact": round(loss_exact, 0),
        "levy_revenue_exact": round(tau * exact["q"], 0),
        "spend_before": P0 * Q0,
        "spend_after_exact": round(p_r * q_r, 0),
        "buyers_loss_first": round(Q0 * dp, 0),
        "spend_first_pct": round(100 * (1 - ED) * dp / P0, 2),
    }


if __name__ == "__main__":
    print(linear_tax(), linear_tax(tau=5))
    print(tax_figure())
    print(pass_through(-0.3, 1.2), 10 * pass_through(-0.3, 1.2))
    print(ex_ce(), ex_envelope(), monopoly_pass())
    print(cement())
    print(
        "check eps at 100",
        math.log(cement_demand(101) / cement_demand(99)) / math.log(101 / 99),
    )

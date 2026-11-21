"""Worked numbers for the text, exercises and problem of Book 4, chapter 17."""


def two_outcome(ubar=5.0, d=2.0, p_high=0.8, p_low=0.4, y_high=100.0, y_low=20.0):
    """Principal-agent with sqrt utility, effort cost d, two outputs."""
    out_high = p_high * y_high + (1 - p_high) * y_low
    out_low = p_low * y_high + (1 - p_low) * y_low
    fb_wage = (ubar + d) ** 2
    low_wage = ubar**2
    gap = d / (p_high - p_low)  # u_H - u_L from the binding IC
    u_low = ubar + d - p_high * gap
    u_high = u_low + gap
    w_low, w_high = u_low**2, u_high**2
    expected = p_high * w_high + (1 - p_high) * w_low
    return {
        "out_high": out_high,
        "out_low": out_low,
        "fb_wage": fb_wage,
        "fb_profit": out_high - fb_wage,
        "low_profit": out_low - low_wage,
        "u": (u_low, u_high),
        "w": (w_low, w_high),
        "expected_wage": expected,
        "agency_cost": expected - fb_wage,
        "sb_profit": out_high - expected,
    }


def risk_neutral(ubar=5.0, d=2.0, p_high=0.8, p_low=0.4):
    gap = d / (p_high - p_low)
    w_low = ubar + d - p_high * gap
    return w_low, w_low + gap, p_high * (w_low + gap) + (1 - p_high) * w_low


def linear(r, c, var):
    b = 1 / (1 + r * c * var)
    effort = b / c
    surplus = b / (2 * c)
    return {
        "b": b,
        "effort": effort,
        "surplus": surplus,
        "agency": 1 / (2 * c) - surplus,
        "risk_premium": r * b * b * var / 2,
        "effort_cost": c * effort * effort / 2,
    }


def surplus_at(b, r, c, var):
    e = b / c
    return e - c * e * e / 2 - r * b * b * var / 2


def team(n):
    """Equal sharing of output sum(e), cost e^2/2: effort and per-person surplus."""
    e = 1 / n
    return e, e - e * e / 2, 0.5


def rpe_k(var_common, var_own, var_other=None, n=1):
    """Weight k on the average of n others' output that minimises the variance of
    y_1 - k * mean(y_others), and that variance."""
    if var_other is None:
        var_other = var_own
    k = var_common / (var_common + var_other / n)
    v = var_common * (1 - k) ** 2 + var_own + k * k * var_other / n
    return k, v


def holdup(invest=30.0, gain=50.0, share=0.5):
    return {
        "return": share * gain,
        "invests": share * gain >= invest,
        "min_share": invest / gain,
    }


def hie(free=3.555, c25=2.787, c95=2.112):
    return {
        "fall25": 100 * (1 - c25 / free),
        "fall95": 100 * (1 - c95 / free),
        "fall25_95": 100 * (1 - c95 / c25),
    }


def orchard():
    r, c = 0.05, 0.01
    var_common, var_own = 1800.0, 200.0
    total = var_common + var_own
    base = linear(r, c, total)
    fixed_rent = surplus_at(1.0, r, c, total)
    law = surplus_at(0.75, r, c, total)
    k1_var = 2 * var_own
    k1 = linear(r, c, k1_var)
    k_opt, v_opt = rpe_k(var_common, var_own)
    opt = linear(r, c, v_opt)
    law_rpe = surplus_at(0.75, r, c, v_opt)
    return {
        "first_best_effort": 1 / c,
        "first_best_surplus": 1 / (2 * c),
        "total_var": total,
        "base": base,
        "fixed_rent": fixed_rent,
        "law": law,
        "law_effort": 0.75 / c,
        "k1_var": k1_var,
        "k1": k1,
        "k_opt": k_opt,
        "v_opt": v_opt,
        "opt": opt,
        "law_rpe": law_rpe,
    }

"""Worked numbers for the exercises and the problem of Book 4, chapter 16."""

from math import exp, log, sqrt


def separating_range(low=10.0, high=20.0, c_low=4.0, c_high=2.0):
    """Schooling levels s* at which the separating equilibrium holds."""
    return (high - low) / c_low, (high - low) / c_high


def pooling_bound(low=10.0, high=20.0, c_low=4.0, share_high=0.5):
    """Largest common schooling level in a pooling equilibrium (pessimistic beliefs)."""
    pooled = share_high * high + (1 - share_high) * low
    return pooled, (pooled - low) / c_low


def waste(low=10.0, high=20.0, c_low=4.0, c_high=2.0, share_high=0.5):
    s = separating_range(low, high, c_low, c_high)[0]
    pooled = share_high * high + (1 - share_high) * low
    return {
        "s": s,
        "high_sep": high - c_high * s,
        "low_sep": low,
        "pooled": pooled,
    }


def rs_low_cover(wealth=100.0, loss=50.0, p_high=0.5, p_low=0.2):
    """Cover x for low risks at their fair price leaving high risks indifferent
    (log utility) with full fair insurance."""
    target = log(wealth - p_high * loss)
    # high risk's utility of (wealth - p_low x, wealth - loss + (1 - p_low) x)
    # (1 - p_high) ln W1 + p_high ln W2 = target; with p_high = 0.5 a quadratic
    a = -p_low * (1 - p_low)
    b = (1 - p_low) * wealth - p_low * (wealth - loss)
    c = wealth * (wealth - loss) - (wealth - p_high * loss) ** 2
    x = (-b + sqrt(b * b - 4 * a * c)) / (2 * a)
    x2 = (-b - sqrt(b * b - 4 * a * c)) / (2 * a)
    x = min(v for v in (x, x2) if v > 0)
    w1, w2 = wealth - p_low * x, wealth - loss + (1 - p_low) * x
    check = (1 - p_high) * log(w1) + p_high * log(w2) - target
    return x, w1, w2, check


def screen(light, heavy, cost, share_light):
    """Optimal two-plan menu with value theta q - q^2/2."""

    def value(theta, q):
        return theta * q - q * q / 2

    share_heavy = 1 - share_light
    q_h = heavy - cost
    q_l = max(light - cost - share_heavy / share_light * (heavy - light), 0.0)
    fee_l = value(light, q_l)
    rent = (heavy - light) * q_l
    fee_h = value(heavy, q_h) - rent
    profit = share_light * (fee_l - cost * q_l) + share_heavy * (fee_h - cost * q_h)
    full = {
        "q": (light - cost, heavy - cost),
        "fee": (value(light, light - cost), value(heavy, heavy - cost)),
    }
    full["profit"] = share_light * (
        full["fee"][0] - cost * full["q"][0]
    ) + share_heavy * (full["fee"][1] - cost * full["q"][1])
    return {
        "q_l": q_l,
        "q_h": q_h,
        "fee_l": fee_l,
        "fee_h": fee_h,
        "rent": rent,
        "profit": profit,
        "full": full,
    }


def phones(customers=9000):
    s = screen(30.0, 40.0, 10.0, 2 / 3)
    light, heavy = customers * 2 / 3, customers / 3
    full = s["full"]
    full_profit = light * (full["fee"][0] - 10 * full["q"][0]) + heavy * (
        full["fee"][1] - 10 * full["q"][1]
    )
    profit = light * (s["fee_l"] - 10 * s["q_l"]) + heavy * (s["fee_h"] - 10 * s["q_h"])
    rents = heavy * s["rent"]
    dwl = light * (20 - s["q_l"]) ** 2 / 2
    heavy_envy = 40 * 20 - 20 * 20 / 2 - full["fee"][0]
    half = screen(30.0, 40.0, 10.0, 0.5)["q_l"]
    return {
        "screen": s,
        "full_profit": full_profit,
        "profit": profit,
        "rents": rents,
        "dwl": dwl,
        "heavy_envy": heavy_envy,
        "q_l_half": half,
    }


def deviation(s_star=4.0, s_dev=3.0, low=10.0, high=20.0, c_low=4.0, c_high=2.0):
    """Payoffs in the intuitive-criterion argument: low type mimicking s_dev at the
    high wage, high type at s_dev and at s_star."""
    return high - c_low * s_dev, high - c_high * s_dev, high - c_high * s_star


def rs_utilities(p_low=0.2):
    x, w1, w2, _ = rs_low_cover()
    low_sep = (1 - p_low) * log(w1) + p_low * log(w2)
    return {"x": x, "premium": p_low * x, "low_sep": low_sep, "low_full_high": log(75)}


def pooling_breaks(share_low=0.9, wealth=100.0, loss=50.0, p_high=0.5, p_low=0.2):
    """Full cover at the pooled fair price, the low risks' utility of it, and the
    share of low risks above which they prefer it to their separating contract."""
    p_bar = share_low * p_low + (1 - share_low) * p_high
    u_pool = log(wealth - p_bar * loss)
    target = rs_utilities(p_low)["low_sep"]
    p_star = (wealth - exp(target)) / loss
    share_star = (p_high - p_star) / (p_high - p_low)
    return {
        "p_bar": p_bar,
        "premium": p_bar * loss,
        "u_pool": u_pool,
        "p_star": p_star,
        "share_star": share_star,
    }


def best_pooled(share_low, wealth=100.0, loss=50.0, p_high=0.5, p_low=0.2):
    """The low risks' best break-even pooled contract: cover x at the pooled fair price
    per unit of cover, from the first-order condition (partial cover when the price is
    above their own probability)."""
    p_bar = share_low * p_low + (1 - share_low) * p_high
    num = p_low * (1 - p_bar) * wealth - (1 - p_low) * p_bar * (wealth - loss)
    x = num / (p_bar * (1 - p_bar))
    x = min(max(x, 0.0), loss)
    w1, w2 = wealth - p_bar * x, wealth - loss + (1 - p_bar) * x

    def u(p):
        return (1 - p) * log(w1) + p * log(w2)

    return {"p_bar": p_bar, "x": x, "u_low": u(p_low), "u_high": u(p_high)}


def pooled_threshold(p_low=0.2):
    """Share of low risks above which the best pooled contract beats their separating
    contract (bisection on the share)."""
    target = rs_utilities(p_low)["low_sep"]
    lo, hi = 0.0, 1.0
    for _ in range(60):
        mid = (lo + hi) / 2
        lo, hi = (lo, mid) if best_pooled(mid)["u_low"] > target else (mid, hi)
    return hi


def menu_checks(light=6.0, heavy=10.0, q_l=2.0, fee_l=10.0, q_h=8.0, fee_h=40.0):
    def value(theta, q):
        return theta * q - q * q / 2

    return {
        "light_own": value(light, q_l) - fee_l,
        "light_other": value(light, q_h) - fee_h,
        "heavy_own": value(heavy, q_h) - fee_h,
        "heavy_other": value(heavy, q_l) - fee_l,
    }


def phones_more(customers=9000):
    """Problem numbers beyond phones(): per-user figures, the one-plan policies."""
    light_n, heavy_n = customers * 2 / 3, customers / 3
    # full-information plans offered openly: heavy users take the light plan
    open_menu = customers * (400 - 10 * 20)
    heavy_only = heavy_n * (750 - 10 * 30)
    # exclusion threshold: q_l = 0 when s_h / s_l >= (30 - 10) / (40 - 30)
    exclude_share_heavy = 2 / 3
    light_surplus_loss = (20 - 15) ** 2 / 2
    return {
        "light_n": light_n,
        "heavy_n": heavy_n,
        "open_menu": open_menu,
        "heavy_only": heavy_only,
        "exclude_share_heavy": exclude_share_heavy,
        "light_loss_each": light_surplus_loss,
        "heavy_value_light_plan": 40 * 15 - 15 * 15 / 2,
    }

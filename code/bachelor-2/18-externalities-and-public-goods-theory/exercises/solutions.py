"""Worked numbers for the text, exercises and problem of Book 4, chapter 18.

Emissions E; marginal benefit of emitting to the polluter (its marginal abatement
cost) a - b E; marginal damage d E.
"""


def externality(a, b, d):
    e_free = a / b
    e_star = a / (b + d)
    tax = d * e_star
    loss = (b + d) / 2 * (e_free - e_star) ** 2
    return {"free": e_free, "star": e_star, "tax": tax, "loss": loss}


def gain(a, b, lo, hi):
    """Polluter's benefit from emitting from lo to hi."""
    return a * (hi - lo) - b / 2 * (hi * hi - lo * lo)


def damage(d, lo, hi):
    return d / 2 * (hi * hi - lo * lo)


def weitzman(a, b, d, theta):
    """Losses at shocks +theta and -theta for the tax and the quota set at theta = 0."""
    base = externality(a, b, d)
    out = {}
    for name in ("tax", "quota"):
        losses = []
        for th in (theta, -theta):
            e_star = (a + th) / (b + d)
            e = (a + th - base["tax"]) / b if name == "tax" else base["star"]
            losses.append((b + d) / 2 * (e - e_star) ** 2)
        out[name] = losses
    out["e_star"] = ((a + theta) / (b + d), (a - theta) / (b + d))
    out["e_tax"] = ((a + theta - base["tax"]) / b, (a - theta - base["tax"]) / b)
    return out


def samuelson(a, mc):
    """Linear marginal benefits a_i - G, constant marginal cost mc."""
    n = len(a)
    g_star = (sum(a) - mc) / n
    g_vol = max(max(a) - mc, 0.0)
    prices = [ai - g_star for ai in a]
    # loss: integral from g_vol to g_star of (sum a - n G - mc)
    loss = (sum(a) - mc) * (g_star - g_vol) - n / 2 * (g_star**2 - g_vol**2)
    return {"g_star": g_star, "g_vol": g_vol, "prices": prices, "loss": loss}


def permits_two_firms(cap=50.0):
    """Firm A: MAC 120 - 2 E (free 60); firm B: MAC 60 - E (free 60)."""
    e_a = (120 - 60 + cap) / 3
    e_b = cap - e_a
    price = 120 - 2 * e_a

    def cost(e_a, e_b):
        return (60 - e_a) ** 2 + (60 - e_b) ** 2 / 2

    return {
        "e_a": e_a,
        "e_b": e_b,
        "price": price,
        "cost_trade": cost(e_a, e_b),
        "cost_equal": cost(cap / 2, cap / 2),
    }


def pivot(values, share):
    net = [v - share for v in values]
    build = sum(net) >= 0
    taxes = []
    for i in range(len(net)):
        others = sum(net) - net[i]
        taxes.append(abs(others) if build != (others >= 0) else 0)
    return build, taxes


def identical_gap(a, mc, n):
    return a - mc / n, a - mc


def river():
    a, b, d = 90.0, 3.0, 1.5
    base = externality(a, b, d)
    w = weitzman(a, b, d, 15.0)
    steep = weitzman(a, b, 4.5, 15.0)
    wrong = externality(a, b, 3.0)["star"]
    return {
        "base": base,
        "gain_free": gain(a, b, 0, 30),
        "damage_free": damage(d, 0, 30),
        "gain_star": gain(a, b, 0, 20),
        "damage_star": damage(d, 0, 20),
        "mill_loss_cut": gain(a, b, 20, 30),
        "fishery_gain_cut": damage(d, 20, 30),
        "revenue": base["tax"] * base["star"],
        "wrong_e": wrong,
        "wrong_loss": (b + d) / 2 * (wrong - base["star"]) ** 2,
        "weitzman": w,
        "steep": steep,
        "steep_star": externality(a, b, 4.5),
    }

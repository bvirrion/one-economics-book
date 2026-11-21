"""Worked numbers for the text, exercises and problem of Book 4, chapter 20."""

LIFE = 1.1 / 0.1  # value of 1 a year for ever, from today, at 10 per cent


def user_cost(price, r, delta, inflation=0.0):
    return price * (r + delta - inflation)


def desired_capital(alpha, y, cost):
    """Cobb-Douglas: alpha * Y / K = user cost."""
    return alpha * y / cost


def q_investment(q, chi=10.0, delta=0.08):
    """I/K = delta + (q - 1) / chi."""
    return delta + (q - 1) / chi


def now(x0, cost=100.0):
    return LIFE * x0 - cost


def wait(x0, u, cost=100.0):
    branches = (x0 * (1 + u), x0 * (1 - u))
    return sum(max(LIFE * x - cost, 0.0) for x in branches) / 2 / 1.1


def trigger(u, cost=100.0, r=0.10):
    """Closed form, valid while the low branch does not invest."""
    life = (1 + r) / r
    k = 2 * (1 + r)
    return cost * (1 - 1 / k) / (life * (1 - (1 + u) / k))


def grunfeld():
    import statsmodels.formula.api as smf
    from statsmodels.datasets import grunfeld as g

    d = g.load_pandas().data
    fe = smf.ols("invest ~ value + capital + C(firm)", d).fit()
    po = smf.ols("invest ~ value + capital", d).fit()
    return {
        "fe": (fe.params["value"], fe.params["capital"]),
        "fe_se": (fe.bse["value"], fe.bse["capital"]),
        "fe_r2": fe.rsquared,
        "pooled": (po.params["value"], po.params["capital"]),
        "pooled_r2": po.rsquared,
    }


def terminal():
    """The weekend problem."""
    uc = user_cost(50, 0.06, 0.08, 0.02)
    return {
        "uc": uc,
        "k": 20 - uc,
        "uc_r8": user_cost(50, 0.08, 0.08, 0.02),
        "uc_noinf": user_cost(50, 0.06, 0.08),
        "uc_sub": user_cost(45, 0.06, 0.08, 0.02),
        "q_avg": 900 / (10 * 50),
        "ik": q_investment(900 / 500),
        "ik_q1": q_investment(1.0),
        "ik_q08": q_investment(0.8),
        "now": now(12),
        "wait": wait(12, 0.5),
        "wait_25": wait(12, 0.25),
        "trig": trigger(0.5),
        "trig75": trigger(0.75),
        "breakeven": 100 / LIFE,
    }

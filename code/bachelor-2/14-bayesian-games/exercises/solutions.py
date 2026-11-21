"""Worked numbers for the exercises and the problem of Book 4, chapter 14."""

from math import sqrt


def cournot_private(a=12.0, c1=2.0, c_high=4.0, c_low=2.0, theta=0.5):
    """Cournot duopoly, p = a - Q; firm 2's cost is c_high with probability theta."""
    q1 = (a - 2 * c1 + theta * c_high + (1 - theta) * c_low) / 3
    q2_high = (a - c_high - q1) / 2
    q2_low = (a - c_low - q1) / 2
    return q1, q2_high, q2_low


def first_price_bid(v, n, r=0.0):
    """Equilibrium bid with n bidders, values uniform on [0, top], risk aversion r."""
    return (n - 1) / (n - r) * v


def risk_aversion_from_slope(slope, n):
    return n - (n - 1) / slope


def expected_max(n, top=1.0):
    return top * n / (n + 1)


def expected_second(n, top=1.0):
    return top * (n - 1) / (n + 1)


def revenue(n, top=1.0):
    """Expected revenue of both formats, risk-neutral bidders."""
    first = (n - 1) / n * expected_max(n, top)
    second = expected_second(n, top)
    return first, second


def sd_revenue(n, top=1.0):
    """Standard deviations of revenue: first-price and second-price."""
    var_max = n / ((n + 1) ** 2 * (n + 2))
    var_second = (n - 1) * 2 / ((n + 1) ** 2 * (n + 2))
    return (n - 1) / n * sqrt(var_max) * top, sqrt(var_second) * top


def win_probability(v, n, top=1.0):
    return (v / top) ** (n - 1)


def bayes(prior=0.3, hit=0.8, false_alarm=0.2):
    return prior * hit / (prior * hit + (1 - prior) * false_alarm)


def curse_correction(n, half_width):
    """Expected highest of n errors uniform on [-w, w]."""
    return half_width * (n - 1) / (n + 1)


def jar(value=8.0, mean_winning=10.01, mean_estimate=5.13):
    return mean_winning - value, value - mean_estimate


def signalling(wage=2.0, cost_good=1.0, cost_poor=3.0):
    """Separating check: good types certify, poor types do not."""
    good = wage - cost_good > 0
    poor = wage - cost_poor < 0
    return good and poor


def licence(top=800.0, n=4, v=600.0, w=100.0, signal=500.0):
    bid = first_price_bid(v, n)
    win = win_probability(v, n, top)
    others_max = (n - 1) / n * v  # expected max of n - 1 values below v
    return {
        "p_highest": 1 / n,
        "e_max": expected_max(n, top),
        "e_second": expected_second(n, top),
        "win": win,
        "bid": bid,
        "payoff_first": (v - bid) * win,
        "payoff_second": (v - others_max) * win,
        "revenue": revenue(n, top),
        "risk_bid": first_price_bid(v, n, 0.5),
        "sd": sd_revenue(n, top),
        "conditional": signal - curse_correction(n, w),
        "correction": curse_correction(n, w),
        "correction8": curse_correction(8, w),
    }


def bayes_poor_report(prior=0.3, hit=0.8, false_alarm=0.2):
    """Probability a ground reported poor is rich."""
    return prior * (1 - hit) / (prior * (1 - hit) + (1 - prior) * (1 - false_alarm))

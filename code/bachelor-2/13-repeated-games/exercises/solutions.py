"""Worked numbers for the exercises and the problem of Book 4, chapter 13."""

from math import exp, log, sqrt


def grim_threshold(t, r, p):
    """Critical discount factor for grim trigger in the prisoner's dilemma."""
    return (t - r) / (t - p)


def tft_threshold(t, r, s):
    """Tit for tat resists one defection followed by tit for tat iff beta >= this."""
    return (t - r) / (r - s)


def alternating_average(t, s, beta):
    """Discounted average payoff of the path T, S, T, S, ..."""
    return (t + beta * s) / (1 + beta)


def bertrand_threshold(n, lag=0, growth=1.0):
    """Critical beta for collusion among n Bertrand firms.

    lag: periods before a deviation is detected; growth: demand factor per period.
    The condition is (beta * growth) ** (lag + 1) >= 1 - 1 / n.
    """
    return (1 - 1 / n) ** (1 / (lag + 1)) / growth


def max_lag(n, beta):
    """Longest detection lag at which n Bertrand firms can still collude."""
    return int(log(1 - 1 / n) / log(beta)) - 1


def survival_beta(survive, interest):
    return survive / (1 + interest)


def max_firms(beta):
    """Largest n with 1 - 1/n <= beta."""
    return int(1 / (1 - beta) + 1e-9)


def ebay_levels(before=7.12, after=-6.76, weeks=4):
    """Sales level after four weeks of each average weekly log growth rate (%)."""
    return exp(weeks * before / 100), exp(weeks * after / 100)


# Cournot cement market: P = 200 - Q, unit cost 40 (a - c = 160)
A = 160.0


def cournot(n, a=A):
    q = a / (n + 1)
    return q, q * q


def collusive(n, a=A):
    q = a / (2 * n)
    return q, (a - n * q) * q


def deviation(n, q, a=A):
    """Best output and profit against n - 1 rivals producing q each."""
    qd = (a - (n - 1) * q) / 2
    return qd, qd * qd


def cournot_threshold(n, a=A):
    q, pc = collusive(n, a)
    _, pd = deviation(n, q, a)
    _, pn = cournot(n, a)
    return (pd - pc) / (pd - pn)


def condition(q, n, delta, a=A):
    """Collusive profit minus the deviation stream at effective factor delta."""
    pc = (a - n * q) * q
    _, pd = deviation(n, q, a)
    _, pn = cournot(n, a)
    return pc - ((1 - delta) * pd + delta * pn)


def lowest_output(n, delta, a=A):
    """Smallest per-firm output (highest price) sustainable at effective delta."""
    # condition is quadratic in q; solve exactly
    # pc = a q - n q^2 ; pd = (a - (n-1) q)^2 / 4 ; pn = (a/(n+1))^2
    pn = (a / (n + 1)) ** 2
    k = n - 1
    qa = -n - (1 - delta) * k * k / 4
    qb = a + (1 - delta) * a * k / 2
    qc = -(1 - delta) * a * a / 4 - delta * pn
    disc = qb * qb - 4 * qa * qc
    roots = sorted([(-qb + sqrt(disc)) / (2 * qa), (-qb - sqrt(disc)) / (2 * qa)])
    q_mon = a / (2 * n)
    return max(roots[0], q_mon)


def highest_price(n, delta, a=A, cost=40.0):
    q = lowest_output(n, delta, a)
    return a + cost - n * q, q


def cement(beta=0.8):
    q_n, p_n = cournot(2)
    q_c, p_c = collusive(2)
    q_d, p_d = deviation(2, q_c)
    return {
        "cournot": (q_n, p_n, 200 - 2 * q_n),
        "collude": (q_c, p_c),
        "deviate": (q_d, p_d, 200 - q_c - q_d, q_c * (200 - q_c - q_d - 40)),
        "threshold": cournot_threshold(2),
        "deviation_stream": (1 - beta) * p_d + beta * p_n,
        "lag1": beta**2,
        "lag2": beta**3,
        "max_lag": int(log(cournot_threshold(2)) / log(beta)) - 1,
        "price_lag2": highest_price(2, beta**3),
        "price_lag3": highest_price(2, beta**4),
        "three": (cournot(3), collusive(3), deviation(3, collusive(3)[0])),
        "threshold3": cournot_threshold(3),
    }

"""Invest now or wait a year? An irreversible project costs 100, sunk once spent, and
earns a profit x0 this year. From next year on the profit is x0 (1 + u) or x0 (1 - u),
equally likely, for ever. The interest rate is 10 per cent.
"""

COST, R = 100.0, 0.10
LIFE = (1 + R) / R  # value today of 1 a year for ever, starting today


def invest_now(x0):
    return LIFE * x0 - COST  # expected profit stays x0


def wait(x0, u):
    up, down = x0 * (1 + u), x0 * (1 - u)
    payoff = sum(max(LIFE * x - COST, 0.0) for x in (up, down)) / 2
    return payoff / (1 + R)


def trigger(u, lo=0.0, hi=100.0):
    for _ in range(60):  # bisection: below the trigger, waiting is worth more
        mid = (lo + hi) / 2
        lo, hi = (mid, hi) if invest_now(mid) < max(wait(mid, u), 0.0) else (lo, mid)
    return hi


print(f"break-even profit (net present value zero): {COST / LIFE:.2f}")
for u in (0.0, 0.25, 0.5, 0.75):
    print(f"u = {u:.2f}: invest at once if profit is at least {trigger(u):.2f}")
x0 = 12.0
print(f"at x0 = {x0:.0f}, u = 0.5: now {invest_now(x0):.2f}, wait {wait(x0, 0.5):.2f}")

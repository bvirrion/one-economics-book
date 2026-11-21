"""Worked numbers for Book 4, chapter 29: Diamond-Dybvig in closed form; D exercise."""


def u(c, g):
    from math import log

    return log(c) if g == 1 else c ** (1 - g) / (1 - g)


def contract(pi, r, g):
    c1 = 1 / (pi + (1 - pi) * r ** (1 / g - 1))
    return c1, r ** (1 / g) * c1


def expected_utility(pi, c1, c2, g):
    return pi * u(c1, g) + (1 - pi) * u(c2, g)


def run_threshold(c1, r):
    """Share of early withdrawals above which a patient depositor withdraws too."""
    return (r - c1) / (c1 * (r - 1))


def bank_empty(c1):
    return 1 / c1


def wait_payoff(c1, r, f):
    return max(1 - f * c1, 0.0) * r / (1 - f)


def leverage_loss(equity, assets, fall):
    """Share of equity lost when assets fall by `fall` (a fraction)."""
    return assets * fall / equity


def crises_and_credit():
    """D exercise: crises per decade; loans/GDP change in the five years before."""
    from econdata import jst

    d = jst(cols=["crisisJST", "tloans", "gdp"])
    per_decade = {}
    before = []
    for _iso, g in d.groupby("iso3"):
        g = g.set_index("year")
        ratio = 100 * g.tloans / g.gdp
        for year in g.index[g.crisisJST == 1]:
            dec = year // 10 * 10
            per_decade[dec] = per_decade.get(dec, 0) + 1
            # the five years ending the year before the crisis: year - 6 to year - 1
            window = range(year - 6, year + 1)
            if any(1914 <= y <= 1919 or 1939 <= y <= 1947 for y in window):
                continue
            if {year - 6, year - 1} <= set(ratio.index):
                if ratio[[year - 1, year - 6]].notna().all():
                    before.append(ratio[year - 1] - ratio[year - 6])
    return per_decade, round(sum(before) / len(before), 2), len(before)


BRENLAND = {"pi": 0.25, "r": 2.0, "g": 2.0}

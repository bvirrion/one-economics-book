"""Worked numbers of the exercises and weekend problem of b1 ch. 18.

Weekend problem: Brenland's statistician rebases the accounts (code/shared/country,
accounts.csv, millions of dalens), with the problem's assumptions for 2025: net primary
income from abroad -5,900, consumption of fixed capital 59,000, net current transfers
from abroad +1,200; a two-good split for chain-linking; an informal sector of 12.8% of
the old GDP in 2015 and 14% in 2025.
"""

import math

import country


def chain(goods, years):
    """Fixed-base (first-year prices) and chained Laspeyres volumes."""
    p0 = {g: goods[g][years[0]][1] for g in goods}

    def value(y, prices):
        return sum(goods[g][y][0] * prices[g] for g in goods)

    fixed = [value(y, p0) for y in years]
    ch = [fixed[0]]
    for a, b in zip(years, years[1:]):
        pa = {g: goods[g][a][1] for g in goods}
        ch.append(ch[-1] * value(b, pa) / value(a, pa))
    comp = {g: goods[g][years[-1]][0] * p0[g] for g in goods}
    return fixed, ch, comp


def problem():
    a = country.load("accounts").set_index("year")
    y = a.loc[2025]
    gdp = y.gdp
    npi, cfc, tr = -5900, 59000, 1200
    gni = gdp + npi
    nni = gni - cfc
    gndi = gni + tr
    s = gndi - y.C - y.G
    gov = y.revenue - y.spending
    ca = y.X - y.M + npi + tr
    priv = ca - gov
    goods = {
        "computers": {2015: (10, 10.0), 2020: (40, 4.0), 2025: (160, 1.6)},
        "other": {2015: (900, 1.0), 2020: (950, 1.1), 2025: (1000, 1.2)},
    }
    fixed, ch, comp = chain(goods, [2015, 2020, 2025])
    r15, r25 = a.loc[2015, "real_gdp"], y.real_gdp
    g_old = (r25 / r15) ** 0.1 - 1
    n15, n25 = r15 * 1.128, r25 * 1.14
    g_new = (n25 / n15) ** 0.1 - 1
    return {
        "gdp_check": y.C + y.I + y.G + y.X - y.M,
        "gni": gni,
        "nni": nni,
        "gndi": gndi,
        "saving": s,
        "saving_rate": round(100 * s / gndi, 2),
        "gov": gov,
        "gov_pct": round(100 * gov / gdp, 2),
        "ca": ca,
        "ca_pct": round(100 * ca / gdp, 2),
        "s_minus_i": s - y.I,
        "private": priv,
        "debt_ratio": round(100 * y.debt / gdp, 1),
        "nominal_factor": round(gdp / a.loc[2015, "gdp"], 4),
        "real_factor": round(r25 / r15, 4),
        "g_old": round(100 * g_old, 2),
        "deflator": round(100 * gdp / r25, 1),
        "fixed": fixed,
        "chained": [round(v, 1) for v in ch],
        "components": comp,
        "new15": round(n15, 1),
        "new25": round(n25, 1),
        "g_new": round(100 * g_new, 2),
        "g_diff": round(100 * (g_new - g_old), 2),
        "debt_ratio_new": round(100 * y.debt / (gdp * 1.14), 1),
    }


def exercises():
    a = country.load("accounts").set_index("year")
    goods = {
        "A": {0: (100, 1.0), 1: (110, 1.1), 2: (120, 1.2)},
        "B": {0: (10, 10.0), 1: (20, 6.0), 2: (40, 4.0)},
    }
    fixed, ch, comp = chain(goods, [0, 1, 2])
    cost_b = 100 * 2 + 10 * 20 + 1 * 300
    cost_k = 100 * 5 + 10 * 30 + 1 * 900
    ppp = cost_k / cost_b
    return {
        "gni": 500 - 20,
        "sectors": {"nation": 30 - 10 - 35, "row": 15},
        "fixed": fixed,
        "chained": [round(v, 2) for v in ch],
        "components": comp,
        "ppp": round(ppp, 4),
        "kestria_ppp": round(60000 / ppp, 0),
        "kestria_market": 60000 / 3,
        "price_level": round(ppp / 3, 3),
        "real_g": round(
            100 * (a.loc[2025, "real_gdp"] / a.loc[2024, "real_gdp"] - 1), 2
        ),
        "defl_g": round(
            100 * (a.loc[2025, "deflator"] / a.loc[2024, "deflator"] - 1), 2
        ),
        "nom_g": round(100 * (a.loc[2025, "gdp"] / a.loc[2024, "gdp"] - 1), 2),
        "pl": 20 / 50,
        "factors": [
            round(math.exp(g / 100 * 29), 2) for g in (1.495, 6.17, 5.779, 1.236)
        ],
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())

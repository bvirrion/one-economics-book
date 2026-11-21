"""Brenland's coal and its smoke (weekend problem). All data invented.

Coal: a known stock of 600 million tonnes in 2025; extraction cost 20 dalens a tonne;
demand q = 40 - 0.25 P (million tonnes a year); a backstop (solar power with storage)
supplies the same energy at a coal-equivalent price of 100 dalens; the interest rate
is 4 %. On the Hotelling path the scarcity rent rises at 4 % a year,
P_t = 20 + lam e^{0.04 t}, and the stock runs out exactly when P reaches 100.

Smoke: each tonne of coal emits 0.02 t of SO2; each kilotonne of SO2 a year causes
0.4 deaths; the value of a statistical life is 3.0 million dalens (as in the
cost-benefit chapter), so the marginal damage is 0.4 x 3.0e6 / 1,000 = 1,200 dalens a
tonne. Two power firms abate SO2 with marginal costs 10 x1 and 30 x2 (dalens a tonne,
x in kilotonnes abated).

Carbon: Brenland emits 40 million tonnes of CO2 a year, valued with the EPA's 2023
figures read as dalens per tonne (an assumption of the problem). Money in the stats:
damage and costs in millions of dalens, SCC totals in millions."""

import numpy as np
from scipy.optimize import brentq

STOCK, COST, BACKSTOP, R = 600.0, 20.0, 100.0, 0.04
A, B = 40.0, 0.25
SO2_PER_T, DEATHS_PER_KT, VSL = 0.02, 0.4, 3.0e6
MAC1, MAC2 = 10.0, 30.0
CO2 = 40.0


def demand(p):
    return np.maximum(A - B * p, 0.0)


def extraction_time(lam):
    """Years until the price reaches the backstop."""
    return np.log((BACKSTOP - COST) / lam) / R


def cumulative(lam):
    T = extraction_time(lam)
    t = np.linspace(0, T, 20001)
    q = demand(COST + lam * np.exp(R * t))
    return np.trapezoid(q, t)


def hotelling():
    lam = brentq(lambda x: cumulative(x) - STOCK, 1e-3, BACKSTOP - COST - 1e-9)
    T = extraction_time(lam)
    return lam, T


def marginal_damage():
    return DEATHS_PER_KT * VSL / 1000.0


def abatement(tax):
    return tax / MAC1, tax / MAC2


def costs(x1, x2):
    return 0.5 * MAC1 * x1**2 * 1000, 0.5 * MAC2 * x2**2 * 1000


def stats():
    from country import load

    lam, T = hotelling()
    q0 = float(demand(COST + lam))
    so2 = q0 * SO2_PER_T * 1000  # kilotonnes
    md = marginal_damage()
    x1, x2 = abatement(md)
    c1, c2 = costs(x1, x2)
    s1, s2 = costs((x1 + x2) / 2, (x1 + x2) / 2)
    gdp = float(load("accounts").set_index("year").gdp[2025])
    p10 = COST + lam * np.exp(R * 10)
    return {
        "lam0": lam,
        "T": T,
        "year_out": 2025 + T,
        "p0": COST + lam,
        "q0": q0,
        "p10": p10,
        "q10": float(demand(p10)),
        "lam10": lam * np.exp(R * 10),
        "so2_kt": so2,
        "deaths": so2 * DEATHS_PER_KT,
        "damage": so2 * md / 1000,
        "md": md,
        "x1": x1,
        "x2": x2,
        "abated": x1 + x2,
        "cost_eff": (c1 + c2) / 1e6,
        "cost_uniform": (s1 + s2) / 1e6,
        "saving": (s1 + s2 - c1 - c2) / 1e6,
        "so2_after": so2 - x1 - x2,
        "deaths_avoided": (x1 + x2) * DEATHS_PER_KT,
        "scc20": CO2 * 190,
        "scc25": CO2 * 120,
        "scc15": CO2 * 340,
        "gdp2025": gdp,
        "scc20_share": 100 * CO2 * 190 / gdp,
    }

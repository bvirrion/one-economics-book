"""Brenland before the factories (weekend problem). All data invented.

Income per person y (kilograms of grain a year) = A / sqrt(L), L the population in
thousands, on fixed land. Population grows at phi * ln(y / ybar), phi = 0.1,
ybar = 300 (subsistence), capped at a biological maximum of 1.2 % a year; as income
rises the cap falls, from 1.2 % at y = 600 to 0.4 % at y = 1,200 (the fertility
decline), and stays there. Technology A grows 0.1 % a year until 1780 and 1.5 % a
year after; A = 9,000 in 1500, when population is at its steady state for that
technology's growth (income 300 exp(0.002 / phi)). A plague in 1600 kills 40 % of
the people.

Households (part III) maximise ln c + a ln n + b ln q subject to c + n (tau + p q)
= I: n = I (a - b) / ((1 + a) tau), q = b tau / ((a - b) p)."""
import numpy as np
import pandas as pd

PHI, YBAR, CAP = 0.1, 300.0, 0.012
STEADY = YBAR * np.exp(2 * 0.001 / PHI)
A0 = 9000.0
L0 = (A0 / STEADY) ** 2
PLAGUE, DEATHS, TAKEOFF = 1600, 0.40, 1780


def cap(y):
    if y <= 600:
        return CAP
    return max(0.004, CAP - (CAP - 0.004) * (y - 600) / 600)


def path(start=1500, end=1900, plague=True):
    A, L = A0, L0
    rows = []
    for t in range(start, end + 1):
        if plague and t == PLAGUE:
            L *= 1 - DEATHS
        y = A / np.sqrt(L)
        rows.append((t, A, L, y))
        g = min(PHI * np.log(y / YBAR), cap(y))
        L *= np.exp(g)
        A *= np.exp(0.001 if t < TAKEOFF else 0.015)
    return pd.DataFrame(rows, columns=["year", "A", "L", "y"])


def becker_lewis(income, a, b, tau, p):
    n = income * (a - b) / ((1 + a) * tau)
    q = b * tau / ((a - b) * p)
    return n, q


def stats():
    d = path().set_index("year")
    n0 = path(plague=False).set_index("year")
    y = d.y
    half = next(t for t in range(PLAGUE, 1780)
                if np.log(y[t] / n0.y[t]) < 0.5 * np.log(y[PLAGUE] / n0.y[PLAGUE]))
    bl0 = becker_lewis(1.0, 0.5, 0.2, 0.04, 0.01)
    bl1 = becker_lewis(1.0, 0.5, 0.35, 0.04, 0.01)
    y2 = next(t for t in range(TAKEOFF, 1901) if y[t] > 2 * YBAR)
    return {"y1500": y[1500], "L1500": d.L[1500], "y1599": y[1599], "y1600": y[1600],
            "premium": 100 * (y[1600] / y[1599] - 1), "half_year": half,
            "L1599": d.L[1599], "L1600": d.L[1600], "L1700": d.L[1700],
            "y1700": y[1700], "y1780": y[1780], "L1780": d.L[1780],
            "y1850": y[1850], "L1850": d.L[1850], "y1900": y[1900], "L1900": d.L[1900],
            "steady": STEADY, "y_double_year": y2,
            "gL1850": 100 * np.log(d.L[1851] / d.L[1850]),
            "gL1899": 100 * np.log(d.L[1900] / d.L[1899]),
            "n0": bl0[0], "q0": bl0[1], "n1": bl1[0], "q1": bl1[1]}

"""Brenland's income support and the weekend problem's reform. The 2025 schedule of
the household survey (country.load("households")): a support of 6,000 + 1,500 per
member beyond the first, paid in full below gross income 12,000 and not at all
above it; a child benefit of 1,200 per member beyond two; the income tax of
TAX_BANDS. The reform withdraws the support at 50 % of gross income instead of all
at once, and adds an in-work credit of 20 % of earnings up to 2,000, withdrawn at
10 % of gross income above 20,000 (only households with hours worked)."""
import numpy as np
from country import TAX_BANDS, load

CLIFF, WITHDRAW = 12_000, 0.5
CREDIT_RATE, CREDIT_MAX, CREDIT_FROM, CREDIT_OUT = 0.20, 2_000, 20_000, 0.10
WAGE = 11.0


def tax(g):
    t = 0.0
    for (lo, r), nxt in zip(TAX_BANDS, TAX_BANDS[1:] + [(float("inf"), 0)]):
        if g > lo:
            t += (min(g, nxt[0]) - lo) * r
    return t


def support_full(size):
    return 6_000 + 1_500 * (size - 1)


def child(size):
    return 1_200 * max(size - 2, 0)


def old_transfers(g, size):
    return (support_full(size) if g < CLIFF else 0.0) + child(size)


def credit(earn):
    if earn <= 0:
        return 0.0
    c = min(CREDIT_RATE * earn, CREDIT_MAX)
    return max(0.0, c - CREDIT_OUT * max(0.0, earn - CREDIT_FROM))


def new_transfers(g, size, works=True):
    s = max(0.0, support_full(size) - WITHDRAW * g)
    return s + child(size) + (credit(g) if works else 0.0)


def net(g, size, reform=False, works=True):
    tr = new_transfers(g, size, works) if reform else old_transfers(g, size)
    return g - tax(g) + tr


def ptr(g, size, reform=False):
    return 1 - (net(g, size, reform) - net(0, size, reform, works=False)) / g


def gini(x):
    x = np.sort(np.asarray(x, dtype=float))
    n = len(x)
    return (2 * np.arange(1, n + 1) - n - 1).dot(x) / (n * x.sum())


def survey():
    h = load("households")
    works = h.hours > 0
    h["old"] = [old_transfers(g, s) for g, s in zip(h.gross_income, h["size"])]
    h["new"] = [new_transfers(g, s, w)
                for g, s, w in zip(h.gross_income, h["size"], works)]
    h["disp_old"] = h.gross_income - h.tax + h.old
    h["disp_new"] = h.gross_income - h.tax + h.new
    return h

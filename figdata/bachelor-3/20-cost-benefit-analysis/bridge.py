"""A new bridge for Brenmoor (weekend problem). All figures are assumptions of the
problem, in millions of 2025 dalens unless stated. Construction in years 0, 1, 2;
the bridge opens in year 3 and is appraised over 40 years of use."""
import numpy as np
from scipy.optimize import brentq

COST = [120.0, 160.0, 120.0]  # forecast construction cost by year
MAINT = 4.0  # a year, from opening
TRIPS = 30_000  # vehicle trips a day
SAVED_MIN, OCC, VTT = 10.0, 1.2, 13.1  # minutes per trip, persons, dalens an hour
DEATHS_AVOIDED, VSL = 1.0, 3.0  # a year; millions of dalens
OPEN, LIFE = 3, 40
UPLIFT = 0.338  # reference class: fixed links, mean cost overrun (FHB 2002 Table 1)


def time_benefit():
    hours = TRIPS * 365 * OCC * SAVED_MIN / 60
    return hours * VTT / 1e6


def flows(uplift=0.0):
    years = np.arange(OPEN + LIFE)
    cost = np.zeros(len(years))
    cost[:len(COST)] = np.array(COST) * (1 + uplift)
    use = years >= OPEN
    benefit = np.where(use, time_benefit() + DEATHS_AVOIDED * VSL, 0.0)
    return years, benefit - cost - np.where(use, MAINT, 0.0)


def npv(rate, uplift=0.0):
    t, f = flows(uplift)
    return float((f / (1 + rate) ** t).sum())


def irr(uplift=0.0):
    return brentq(lambda r: npv(r, uplift), 1e-6, 0.5)

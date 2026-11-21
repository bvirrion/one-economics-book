"""Worked numbers for the text, exercises and problem of Book 4, chapter 24."""

from math import exp, log


def ak_growth(s, a, delta):
    return s * a - delta


def semi_growth(n, phi):
    return n / (1 - phi)


def level_gain(phi, s_old, s_new):
    """Long-run ratio of output per worker after the research share changes."""
    return (s_new / s_old) ** (1 / (1 - phi)) * (1 - s_new) / (1 - s_old)


def growth_path(t, z0, n, phi):
    """Growth of ideas, dz/dt = z (n + (phi - 1) z), from z0."""
    a, b = n, 1 - phi
    return a / (b + (a / z0 - b) * exp(-a * t))


def time_to(z, z0, n, phi):
    a, b = n, 1 - phi
    return -log((a / z - b) / (a / z0 - b)) / a


def research_productivity(growth_old, growth_new, researchers_ratio):
    return (growth_new / growth_old) / researchers_ratio


def brenland():
    phi, n, s = 0.5, 0.01, 0.02
    return {
        "g": semi_growth(n, phi),
        "jump": 2 * semi_growth(n, phi),
        "level_a": 2 ** (1 / (1 - phi)),
        "level_y": level_gain(phi, s, 2 * s),
        "drop": (1 - 2 * s) / (1 - s),
        "t_half": time_to(0.03, 0.04, n, phi),
        "z50": growth_path(50, 0.04, n, phi),
        "g_n0": semi_growth(0.0, phi),
        "level_phi_075": level_gain(0.75, s, 2 * s),
        "g_phi_075": semi_growth(n, 0.75),
    }

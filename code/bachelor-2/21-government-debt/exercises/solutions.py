"""Worked numbers for the text, exercises and problem of Book 4, chapter 21."""

from math import log


def stabilising(b, i, g):
    """Primary surplus, share of GDP, that holds the debt ratio b steady."""
    return (i - g) / (1 + g) * b


def step(b, i, g, s):
    return (1 + i) / (1 + g) * b - s


def years_to(b, target, i, g, s, cap=500):
    n = 0
    while b > target and n < cap:
        b, n = step(b, i, g, s), n + 1
    return n, b


def surplus_for(b, target, i, g, years):
    """Constant surplus that brings b to target in the given number of years."""
    a = (1 + i) / (1 + g)
    annuity = sum(a**k for k in range(years))
    return (a**years * b - target) / annuity


def limit_with_deficit(d, i, g):
    """Ratio to which debt converges with a constant primary deficit d, i < g."""
    return d * (1 + g) / (g - i)


def bohn(rho=0.054, i=0.04, g=0.03):
    a = (1 + i) / (1 + g) - rho
    return a, log(0.5) / log(a)


def smoothing():
    return {"uneven": 0**2 + 20**2, "smooth": 10**2 + 10**2}


def eurostat_extended(geos=("ES", "PT"), growth_from=2019):
    from econdata import eurostat

    d = eurostat("gov_10dd_edpt1")
    d = d[d.unit == "MIO_EUR"]

    def series(item, sector, geo):
        rows = d[(d.na_item == item) & (d.sector == sector) & (d.geo == geo)]
        return rows.set_index("time").value

    out = {}
    for geo in geos:
        debt, gdp = series("GD", "S13", geo), series("B1GQ", "S1", geo)
        interest, bal = series("D41PAY", "S13", geo), series("B9", "S13", geo)
        i = interest[2024] / debt[2023]
        years = 2024 - growth_from
        g = (gdp[2024] / gdp[growth_from]) ** (1 / years) - 1
        b = debt[2024] / gdp[2024]
        out[geo] = {
            "b": b,
            "i": i,
            "g": g,
            "s": stabilising(b, i, g),
            "primary": (bal[2024] + interest[2024]) / gdp[2024],
        }
    return out


def brenland():
    debt24, debt25, gdp24, gdp25, deficit = 228953, 236818, 379562, 393264, 7865
    interest = 0.03 * debt24
    b, i, g = 0.602, 0.03, 0.036
    return {
        "deficit_ratio": deficit / gdp25,
        "ratio": debt25 / gdp25,
        "check": debt24 + deficit,
        "growth": gdp25 / gdp24 - 1,
        "interest": interest,
        "primary": deficit - interest,
        "primary_ratio": (deficit - interest) / gdp25,
        "s3": stabilising(b, i, g),
        "next3": step(b, i, g, -0.0025),
        "s5": stabilising(b, 0.05, g),
        "next5": step(b, 0.05, g, -0.0025),
        "years3": years_to(b, 0.50, i, g, 0.01)[0],
        "years5": years_to(b, 0.50, 0.05, g, 0.01)[0],
        "s_ten": surplus_for(b, 0.50, i, g, 10),
        "years_repressed": years_to(b, 0.50, i, 0.056, 0.01)[0],
    }

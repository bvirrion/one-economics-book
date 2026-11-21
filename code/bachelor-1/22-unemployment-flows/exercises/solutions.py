"""Worked numbers of the exercises and weekend problem of b1 ch. 22.

Weekend problem: Brenland's labour market after a factory closes. Monthly rates. The
job-finding rate is set at f = 0.30 and the separation rate calibrated so that the
steady state equals the 2025 unemployment rate of accounts.csv: s = u f / (1 - u).
No-shirking wage (continuous time): w = z + e + (e / q)(r + s + f).
"""

import math

import country


def ustar(s, f):
    return s / (s + f)


def nsw(z, e, q, r, s, f):
    return z + e + e / q * (r + s + f)


def problem():
    a = country.load("accounts").set_index("year").loc[2025]
    lf, emp = int(a.labour_force), int(a.employed)
    u = (lf - emp) / lf
    f = 0.30
    s = u * f / (1 - u)
    lay = 0.02 * emp
    u0 = (lf - emp + lay) / lf
    lam = s + f
    path = {
        m: round(100 * (u + (u0 - u) * math.exp(-lam * m)), 3) for m in (1, 3, 6, 12)
    }
    f2 = 0.25
    u2 = ustar(s, f2)
    z, e, q, r = 1.2, 0.5, 0.1, 0.005
    return {
        "lf": lf,
        "emp": emp,
        "unemp": lf - emp,
        "u": round(100 * u, 3),
        "s": round(s, 5),
        "inflow": round(s * emp, 1),
        "outflow": round(f * (lf - emp), 1),
        "dur": round(1 / f, 2),
        "lay": round(lay, 1),
        "u0": round(100 * u0, 3),
        "lam": round(lam, 5),
        "half": round(math.log(2) / lam, 2),
        "path": path,
        "w": round(nsw(z, e, q, r, s, f), 4),
        "w2": round(nsw(z, e, q, r, s, f2), 4),
        "w_z": round(nsw(1.5, e, q, r, s, f), 4),
        "rent": round(nsw(z, e, q, r, s, f) - z - e, 4),
        "u2": round(100 * u2, 3),
        "dur2": round(1 / f2, 2),
        "half2": round(math.log(2) / (s + f2), 2),
        "unemp2": round(u2 * lf, 1),
    }


def exercises():
    sa, fa, sb, fb = 0.015, 0.30, 0.017, 0.22
    return {
        "u1": round(100 * ustar(0.02, 0.28), 2),
        "dur": 1 / 0.25,
        "u4": round(100 * ustar(0.02, 0.20), 2),
        "half": round(math.log(2) / 0.30, 2),
        "uA": round(100 * ustar(sa, fa), 2),
        "uB": round(100 * ustar(sb, fb), 2),
        "u_s_only": round(100 * ustar(sb, fa), 2),
        "u_f_only": round(100 * ustar(sa, fb), 2),
        "nsw": round(nsw(1.0, 0.4, 0.2, 0.004, 0.02, 0.28), 4),
        "fire": round(100 * ustar(0.8 * 0.02, 0.8 * 0.28), 2),
        "half_fire": round(math.log(2) / (0.8 * 0.30), 2),
        "two_groups_mean": (1 / 0.4 + 1 / 0.05) / 2,
        "two_groups_long": round((1 / 0.05) / (1 / 0.4 + 1 / 0.05), 3),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())

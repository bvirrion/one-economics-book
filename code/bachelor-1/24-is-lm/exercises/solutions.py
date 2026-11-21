"""Worked numbers of the exercises and weekend problem of b1 ch. 24.

Weekend problem: Brenland's recession, billions of dalens, r in per cent. Calibrated to
the 2025 accounts (Y = 393.264, C = 225.014, I = 88.484, G = 78.653, NX = 1.113)
at r = 3: C = c0 + 0.6 (Y - T), T = 80; I = I0 - 5 r; LM: M/P = 0.5 Y - 5 r,
with a floor r >= 0.
"""

import country

MPC, B, K, H, T = 0.6, 5.0, 0.5, 5.0, 80.0


def calibrate():
    a = country.load("accounts").set_index("year").loc[2025] / 1000
    Y, C, Inv, G, NX = a.gdp, a.C, a.I, a.G, a.X - a.M
    r = 3.0
    c0 = C - MPC * (Y - T)
    i0 = Inv + B * r
    mp = K * Y - H * r
    return {
        "Y": Y,
        "C": C,
        "I": Inv,
        "G": G,
        "NX": NX,
        "r": r,
        "c0": c0,
        "i0": i0,
        "mp": mp,
    }


def solve(c0, i0, G, NX, mp, floor=True):
    """IS: Y = (c0 - MPC T + i0 - B r + G + NX) / (1 - MPC); LM: r = (K Y - mp) / H."""
    A = c0 - MPC * T + i0 + G + NX
    # substitute LM into IS: Y (1 - MPC) = A - B (K Y - mp) / H
    Y = (A + B * mp / H) / (1 - MPC + B * K / H)
    r = (K * Y - mp) / H
    if floor and r < 0:
        r = 0.0
        Y = A / (1 - MPC)
    return Y, r


def problem():
    p = calibrate()
    base = solve(p["c0"], p["i0"], p["G"], p["NX"], p["mp"])
    m_g = (1 / (1 - MPC)) / (1 + B * K / (H * (1 - MPC)))
    m_m = m_g * B / H
    exp = solve(p["c0"], p["i0"], p["G"], p["NX"] - 10, p["mp"])
    lost = base[0] - exp[0]
    mon = solve(p["c0"], p["i0"], p["G"], p["NX"] - 10, p["mp"] + lost / m_m)
    fis = solve(p["c0"], p["i0"], p["G"] + lost / m_g, p["NX"] - 10, p["mp"])
    unc = solve(p["c0"], p["i0"] - 20, p["G"], p["NX"] - 10, p["mp"], floor=False)
    zlb = solve(p["c0"], p["i0"] - 20, p["G"], p["NX"] - 10, p["mp"])
    zlb_m = solve(p["c0"], p["i0"] - 20, p["G"], p["NX"] - 10, p["mp"] + 20)
    zlb_g = solve(p["c0"], p["i0"] - 20, p["G"] + 1, p["NX"] - 10, p["mp"])
    gap = base[0] - zlb[0]
    return {
        "c0": round(p["c0"], 3),
        "i0": round(p["i0"], 3),
        "mp": round(p["mp"], 3),
        "Y0": round(base[0], 3),
        "r0": round(base[1], 3),
        "is_slope": round(-(1 - MPC) / B, 3),
        "lm_slope": K / H,
        "simple": 1 / (1 - MPC),
        "m_g": round(m_g, 4),
        "m_m": round(m_m, 4),
        "exp": (round(exp[0], 3), round(exp[1], 3)),
        "lost": round(lost, 3),
        "mon_dm": round(lost / m_m, 3),
        "mon": (round(mon[0], 3), round(mon[1], 3)),
        "fis_dg": round(lost / m_g, 3),
        "fis": (round(fis[0], 3), round(fis[1], 3)),
        "unc": (round(unc[0], 3), round(unc[1], 3)),
        "zlb": (round(zlb[0], 3), zlb[1]),
        "zlb_m": (round(zlb_m[0], 3), zlb_m[1]),
        "zlb_g": (round(zlb_g[0], 3), zlb_g[1]),
        "zlb_mult": round(zlb_g[0] - zlb[0], 3),
        "y_exit": round(p["mp"] / K, 3),
        "g_exit": round((p["mp"] / K - zlb[0]) / 2.5, 3),
        "g_restore": round(
            (p["mp"] / K - zlb[0]) / 2.5 + (base[0] - p["mp"] / K) / m_g, 3
        ),
        "gap": round(gap, 3),
        "g_needed_flat": round(gap / 2.5, 3),
    }


def exercises():
    # IS: Y = 1500 - 100 r; LM: Y = 500 + 100 r
    r = (1500 - 500) / 200
    Y = 500 + 100 * r
    # confidence fall: I0 down by 40 -> IS: Y = 1340 - 100 r; MP holds Y at 1000
    r_mp = (1340 - 1000) / 100
    # trap: IS Y = 400 - 100 r against LM Y = 500 + 100 r
    r_trap = (400 - 500) / 200
    return {
        "r": r,
        "Y": Y,
        "m_g": 4 / 2,
        "m_m": 1 / 2,
        "dr_dg": 4 / 200,
        "r_mp": r_mp,
        "r_cut": 5 - r_mp,
        "r_trap_unc": r_trap,
        "Y_trap": 400,
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())

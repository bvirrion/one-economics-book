"""Worked numbers of the exercises and weekend problem of b1 ch. 9 (technology).

Weekend problem: bakeries with the CES technology
Y = 100 * (0.5 K**RHO + 0.5 L**RHO) ** (NU / RHO), RHO = -2/3 (sigma = 0.6),
K ovens and L workers; bakery A has (K, L) = (2, 8), bakery B (4, 4).
"""

import math

RHO = -2 / 3


def ces(k, lab, nu=1.0, scale=100.0, b=1.0):
    return scale * (0.5 * (b * k) ** RHO + 0.5 * lab**RHO) ** (nu / RHO)


def mrts(k, lab):
    """f_L / f_K, ovens per worker, for the equal-weight CES."""
    return (k / lab) ** (1 - RHO)


def iso_k(y, lab):
    """Ovens needed with lab workers to bake y loaves (nu = 1)."""
    return (2 * (y / 100) ** RHO - lab**RHO) ** (1 / RHO)


def share_k(w_over_r, sigma=0.6):
    return 1 / (1 + w_over_r ** (1 - sigma))


def problem():
    """Two bakeries: A in Kestria (2 ovens, 8 bakers), B in Brenland (4, 4)."""
    ya, yb = ces(2, 8), ces(4, 4)
    b = 1.5
    return {
        "ya": round(ya, 2),
        "yb": round(yb, 2),
        "mrts_a": round(mrts(2, 8), 4),
        "mrts_b": mrts(4, 4),
        "k_iso": round(iso_k(400, 8), 3),
        "k_min": round(4 * 2 ** (1 / RHO), 3),
        "ya2": round(ces(4, 16), 2),
        "apl_a": round(ya / 8, 2),
        "mpl_a": round(0.5 * 100**RHO * (ya / 8) ** (1 - RHO), 2),
        "mpk_a": round(0.5 * 100**RHO * (ya / 2) ** (1 - RHO), 2),
        "euler_a": round(
            0.5 * 100**RHO * ((ya / 8) ** (1 - RHO) * 8 + (ya / 2) ** (1 - RHO) * 2), 2
        ),
        "apk_a": round(ya / 2, 2),
        "apl_b": round(yb / 4, 2),
        "g44": round(ces(4, 4, nu=1.2), 1),
        "g22": round(ces(2, 2, nu=1.2), 1),
        "sigma": round(1 / (1 - RHO), 3),
        "sigma_hat": round(math.log(4) / math.log(10), 3),
        "kl_kest": round(0.1**0.6, 4),
        "kl_up10": round(1.1**0.6 - 1, 4),
        "sh_kest0": round(share_k(0.1), 3),
        "sh_bren0": round(share_k(1.0), 3),
        "ya_new": round(ces(2, 8, b=b), 2),
        "eff_kest": round((b * 0.1) ** 0.6, 4),
        "kl_kest1": round((b * 0.1) ** 0.6 / b, 4),
        "eff_bren": round(b**0.6, 4),
        "kl_bren1": round(b**0.6 / b, 4),
        "sh_kest1": round(share_k(b * 0.1), 3),
        "sh_bren1": round(share_k(b), 3),
    }


def exercises():
    return {
        "mrts_cd": round((0.7 / 0.3) * (8 / 27), 4),
        "kl_half": round(2**0.5, 3),
        "scale_8": 2.0,
        "scale_16": round(16 / 14, 3),
        "sig_kor": round(math.log(12.872) / math.log(15.61), 2),
        "sig_usa": round(math.log(1.656) / math.log(1.445), 2),
        "usa_ind_k": round(256.58 / 27.98, 2),
        "usa_ind_w": round(45.86 / 3.97, 2),
    }


if __name__ == "__main__":
    print(problem())
    print(exercises())

"""Worked numbers of the exercises and weekend problem of b1 ch. 21.

Weekend problem: Brenland's growth review. Real GDP and employment from accounts.csv;
real investment = I / deflator x 100; capital by perpetual inventory from K(2000) = 3 x
Y(2000) with depreciation 0.05: K(t + 1) = 0.95 K(t) + I(t). Human capital is taken as
constant. Misallocation: each firm of the 2025 census produces
y_i = A_i (k_i^0.35 l_i^0.65)^0.85; A_i is backed out, and the efficient allocation
gives firm i the share A_i^(1/0.15) / sum of the same, of both K and L.
"""

import math

import country
import numpy as np


def capital_series(a, k0_ratio=3.0, delta=0.05):
    real_i = a.I / a.deflator * 100
    k = [k0_ratio * a.real_gdp.iloc[0]]
    for inv in real_i.iloc[:-1]:
        k.append((1 - delta) * k[-1] + inv)
    return np.array(k)


def accounting(a, alpha):
    k = capital_series(a)
    n = len(a) - 1
    gy = math.log(a.real_gdp.iloc[-1] / a.real_gdp.iloc[0]) / n
    gk = math.log(k[-1] / k[0]) / n
    gl = math.log(a.employed.iloc[-1] / a.employed.iloc[0]) / n
    tfp = gy - alpha * gk - (1 - alpha) * gl
    return {
        "gy": round(100 * gy, 3),
        "gk": round(100 * gk, 3),
        "gl": round(100 * gl, 3),
        "cap": round(100 * alpha * gk, 3),
        "lab": round(100 * (1 - alpha) * gl, 3),
        "tfp": round(100 * tfp, 3),
        "tfp_share": round(tfp / gy, 3),
        "K2000": round(k[0]),
        "K2025": round(k[-1]),
        "KY2025": round(k[-1] / a.real_gdp.iloc[-1], 3),
        "gy_pw": round(100 * (gy - gl), 3),
    }


def misallocation(eta=0.85, ak=0.35):
    f = country.load("firms")
    x = f.capital**ak * f.workers ** (1 - ak)
    A = f.output / x**eta
    K, L = f.capital.sum(), f.workers.sum()
    share = A ** (1 / (1 - eta)) / (A ** (1 / (1 - eta))).sum()
    y_eff = (A ** (1 / (1 - eta))).sum() ** (1 - eta) * (K**ak * L ** (1 - ak)) ** eta
    mp = eta * f.output / x
    big = share.idxmax()
    return {
        "Y": int(f.output.sum()),
        "K": int(K),
        "L": int(L),
        "Y_eff": round(y_eff),
        "gain": round(y_eff / f.output.sum() - 1, 4),
        "sd_log_mp": round(float(np.log(mp).std()), 3),
        "mp_p10": round(float(mp.quantile(0.1)), 2),
        "mp_p90": round(float(mp.quantile(0.9)), 2),
        "top_share": round(float(share.max()), 4),
        "top_firm": int(f.firm[big]),
    }


def problem():
    a = country.load("accounts")
    r35 = accounting(a, 0.35)
    r30 = accounting(a, 0.30)
    m = misallocation()
    m9 = misallocation(eta=0.9)
    # levels: Kestria relative to Brenland (given in the problem)
    y, k, h = 0.6, 0.5, 0.8
    ykh = k ** (1 / 3) * h ** (2 / 3)
    return {
        "a35": r35,
        "a30": r30,
        "mis": m,
        "gain_09": m9["gain"],
        "ykh": round(ykh, 3),
        "A": round(y / ykh, 3),
        "kh_part": round(math.log(ykh) / math.log(y), 3),
    }


def exercises():
    res = 4 - 0.35 * 6 - 0.65 * 1
    # development accounting: country B relative to A
    yB, kB, hB = 0.25, 0.2, 0.6
    ykh = kB ** (1 / 3) * hB ** (2 / 3)
    # two-firm misallocation: y_i = A_i l_i^0.5, L = 100, A = (1, 2), l = (50, 50)
    y0 = 1 * 50**0.5 + 2 * 50**0.5
    l1 = 100 / (1 + 4)
    y1 = 1 * l1**0.5 + 2 * (100 - l1) ** 0.5
    return {
        "residual": round(res, 2),
        "ykh": round(ykh, 3),
        "A": round(yB / ykh, 3),
        "kh_part": round(math.log(ykh) / math.log(yB), 3),
        "two_y0": round(y0, 3),
        "two_l1": l1,
        "two_y1": round(y1, 3),
        "two_gain": round(y1 / y0 - 1, 4),
        "mp0": (round(0.5 * 50**-0.5, 4), round(1.0 * 50**-0.5, 4)),
        "mp1": round(0.5 * l1**-0.5, 4),
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(problem())
    pprint.pprint(exercises())

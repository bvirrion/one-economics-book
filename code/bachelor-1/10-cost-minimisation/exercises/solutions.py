"""Worked numbers of the exercises and weekend problem of b1 ch. 10 (cost minimisation).

Weekend problem: a battery plant with q = A * K**0.5 * L**0.5 (kWh a year), A = 2,
wage w = 50 and line rental r = 200 dalens; learning: unit cost 100 * (X / 1000)**(-B)
with X the cumulative output before the year and a learning rate of 18%.
"""

import math

B = -math.log2(0.82)


def cd_cost(q, w, r, a=2.0):
    return 2 / a * q * math.sqrt(w * r)


def problem():
    q = 1000
    k_bar = 250
    outputs = [1000, 2000, 4000, 8000, 16000, 16000, 16000]
    cum = [1000]
    for y in outputs:
        cum.append(cum[-1] + y)
    unit = [round(100 * (x / 1000) ** (-B), 2) for x in cum]
    return {
        "L": q * 0.5 * math.sqrt(200 / 50),
        "K": q * 0.5 * math.sqrt(50 / 200),
        "C": cd_cost(q, 50, 200),
        "C_w72": cd_cost(q, 72, 200),
        "L_w72": round(0.5 * math.sqrt(200 / 72), 4),
        "K_w72": round(0.5 * math.sqrt(72 / 200), 4),
        "sr_fixed": 200 * k_bar,
        "sr_coef": 50 / (4 * k_bar),
        "srac_1200": round(50000 / 1200 + 0.05 * 1200, 2),
        "srmc_1200": 0.1 * 1200,
        "srac_800": round(50000 / 800 + 0.05 * 800, 2),
        "cum": cum,
        "unit": unit,
        "b": round(B, 4),
        "lr_two_points": round((45.21 / 100) ** 0.25, 4),
        "a_year5": round(2 * 100 / 45.21, 2),
        "unit_y8": unit[7],
        "moore_y8": round(100 * 0.82**7, 2),
        "price_y8": round(1.1 * unit[7], 2),
    }


def exercises():
    w, r = 8, 1
    return {
        "ex1": (10 * math.sqrt(1 / 4), 10 * math.sqrt(4 / 1), 2 * 10 * math.sqrt(4)),
        "ex2": 10 * 300 + 5 * 200,
        "ex5_unit": round((r / (1 / 3)) ** (1 / 3) * (w / (2 / 3)) ** (2 / 3), 4),
        "ex6": (4 + 36 / 4, 2 * 6),
        "ex7_mes": 100,
        "ex8": round(100 * (1 - 0.8**3), 1),
        "ex9": round(1 - (120 / 200) ** (1 / 3), 4),
    }


if __name__ == "__main__":
    print(problem())
    print(exercises())

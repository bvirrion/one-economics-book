"""Worked numbers of the exercises and weekend problem of b1 ch. 27.

Weekend problem: Brenland pegs to the kest. Part I uses Brenland's 2025 accounts and
trade tables (millions of dalens). Parts II-III reuse the ch. 24 calibration (billions):
C = c0 + 0.6(Y - 80), I = 103.484 - 5r, G = 78.653, money demand 0.5Y - 5r, now with
net exports NX = 50e - 48.887 (e = 1 in 2025, a rise is a depreciation) and r = r* = 3.
"""

from country import load

MPC, T, I0, IR, G = 0.6, 80.0, 103.484, 5.0, 78.653
Y0, C0 = 393.264, 225.014
NXA, NXB = -48.887, 50.0
RSTAR = 3.0


def accounts():
    a = load("accounts").set_index("year").loc[2025]
    t = load("trade").set_index("year")
    s = a.gdp - a.C - a.G
    return {
        "nx": int(a.X - a.M),
        "S": int(s),
        "S_minus_I": int(s - a.I),
        "public": int(a.revenue - a.spending),
        "private": int(s - (a.revenue - a.spending)),
        "bilateral": int(
            t.loc[2025, "exports_to_kestria"] - t.loc[2025, "imports_from_kestria"]
        ),
        "rest": int(
            (a.X - a.M)
            - (t.loc[2025, "exports_to_kestria"] - t.loc[2025, "imports_from_kestria"])
        ),
        "rate": t.loc[2025, "rate"],
        "dep": round(100 * (t.loc[2025, "rate"] / t.loc[2024, "rate"] - 1), 1),
    }


def long_run(rstar=RSTAR, dG=0.0):
    s = Y0 - C0 - G - dG  # national saving, output at full employment, C unchanged
    i = I0 - IR * rstar
    nx = s - i
    return {
        "S": round(s, 3),
        "I": round(i, 3),
        "NX": round(nx, 3),
        "eps": round((nx - NXA) / NXB, 3),
    }


c0 = C0 - MPC * (Y0 - T)
MP = 0.5 * Y0 - IR * RSTAR


def mf(dG=0.0, dM=0.0, peg=False):
    auto = c0 - MPC * T + I0 - IR * RSTAR + G + dG + NXA
    if peg:  # e = 1, IS* gives Y; money adjusts
        y = (auto + NXB) / (1 - MPC)
        return {"Y": round(y, 3), "e": 1.0, "dM": round(0.5 * y - IR * RSTAR - MP, 3)}
    y = (MP + dM + IR * RSTAR) / 0.5  # LM* vertical
    e = ((1 - MPC) * y - auto) / NXB
    return {"Y": round(y, 3), "e": round(e, 3)}


def attack(dep=0.05, reserves=30.0, outflow=4.0, rate=1.242):
    prem = 100 * ((1 + dep) ** 12 - 1)
    per_day = outflow / rate
    return {
        "premium": round(prem, 1),
        "rate": round(RSTAR + round(prem, 1), 1),
        "per_day": round(per_day, 2),
        "days": round(reserves / round(per_day, 2), 1),
        "invest": round(I0 - IR * (RSTAR + prem), 1),
    }


def exercises():
    return {
        "nx": 400 - 350,
        "eps": round(1.25 * 100 / 110, 3),
        "small": {
            "I": 500 - 20 * 4,
            "NX": 400 - (500 - 20 * 4),
            "eps": ((400 - (500 - 20 * 4)) + 100) / 50,
        },
        "ml": (0.6 + 0.7, 0.3 + 0.4),
        "float": {"dY": 0, "de": -50 / 25, "dNX": -50},
        "sweden": 52 * 10,
    }


if __name__ == "__main__":
    import pprint

    pprint.pprint(accounts())
    for k in [(3, 0), (4, 0), (3, 10)]:
        print(k, long_run(*k))
    print(round(c0, 4), MP)
    print(
        mf(),
        mf(dG=10),
        mf(dM=10),
        mf(peg=True),
        mf(dG=10, peg=True),
        mf(dM=10, peg=True),
    )
    print(attack())
    pprint.pprint(exercises())

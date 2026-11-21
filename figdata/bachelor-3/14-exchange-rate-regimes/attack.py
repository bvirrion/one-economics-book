"""The first-generation crisis model in levels (the weekend problem's numbers).

Money supply M = D + R, domestic credit D = D0 + mu t; money demand M = k S - c dS/dt.
Under the peg S = S_bar. The shadow rate (the float with no reserves left) is
S~ = D / k + c mu / k^2; the attack comes when S~ reaches S_bar, at
T = (R0 - c mu / k) / mu, and takes the remaining reserves c mu / k at once.
"""
import pandas as pd

S_BAR, K, C, D0, MU = 1.20, 100.0, 200.0, 90.0, 3.0


def attack_time(s_bar=S_BAR, k=K, c=C, d0=D0, mu=MU):
    r0 = k * s_bar - d0
    return (r0 - c * mu / k) / mu


def path(step=0.25, until=10.0, **kw):
    p = dict(s_bar=S_BAR, k=K, c=C, d0=D0, mu=MU) | kw
    t_star = attack_time(**p)
    rows = []
    t = 0.0
    while t <= until + 1e-9:
        d = p["d0"] + p["mu"] * t
        shadow = d / p["k"] + p["c"] * p["mu"] / p["k"] ** 2
        reserves = p["k"] * p["s_bar"] - d if t < t_star else 0.0
        rate = p["s_bar"] if t < t_star else shadow
        rows.append({"t": t, "credit": d, "reserves": reserves, "shadow": shadow,
                     "rate": rate})
        t += step
    return pd.DataFrame(rows)

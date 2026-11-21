"""Brenland's steel tariff (invented, linear). Quantities in millions of tonnes,
prices in dalens per tonne, welfare in millions of dalens.

Brenland steel: demand 100 - 2P, supply -20 + 2P, so imports M(P) = 120 - 4P.
Kestria's export supply of steel: X*(P*) = -40 + 4P*.
Grain (retaliation): Brenland's export supply -20 + 2p, Kestria's import demand
100 - 3 p_K. An ad valorem tariff t makes the importer's price (1 + t) times the
exporter's.
"""


def steel(t):
    """Steel market with Brenland's tariff t: world price, Brenland price, quantities
    and welfare changes relative to free trade (Brenland and Kestria)."""
    pw = 160 / (4 + 4 * (1 + t))  # 120 - 4(1+t)P* = -40 + 4P*
    p = (1 + t) * pw
    m = -40 + 4 * pw
    p0, m0 = 20.0, 40.0
    cs = -((100 - 2 * p0) + (100 - 2 * p)) / 2 * (p - p0)
    ps = ((-20 + 2 * p0) + (-20 + 2 * p)) / 2 * (p - p0)
    rev = (p - pw) * m
    tot = (p0 - pw) * m
    dwl = 0.5 * (p - p0) * (m0 - m)
    kestria = -((-40 + 4 * pw) + (-40 + 4 * p0)) / 2 * (p0 - pw)
    return {"t": t, "p_world": pw, "p_home": p, "imports": m,
            "q_supply": -20 + 2 * p, "q_demand": 100 - 2 * p, "cs": cs, "ps": ps,
            "revenue": rev, "tot_gain": tot, "dwl": dwl, "brenland": cs + ps + rev,
            "kestria": kestria}


def grain(t):
    """Grain market with Kestria's retaliatory tariff t on Brenland's grain."""
    p = 120 / (2 + 3 * (1 + t))  # -20 + 2p = 100 - 3(1+t)p
    pk = (1 + t) * p
    x = -20 + 2 * p
    p0, x0 = 24.0, 28.0
    brenland = -((-20 + 2 * p) + x0) / 2 * (p0 - p)
    rev = (pk - p) * x
    cons = -((100 - 3 * pk) + x0) / 2 * (pk - p0)
    return {"t": t, "p_brenland": p, "p_kestria": pk, "exports": x,
            "brenland": brenland, "kestria": cons + rev, "revenue": rev,
            "tot_gain": (p0 - p) * x, "dwl": 0.5 * (pk - p0) * (x0 - x)}

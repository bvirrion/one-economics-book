"""Weekend problem: Brenland's steel tariff (model in steel.py). Writes
out/steel_cases.csv (free trade, the small-country benchmark at a fixed world price of
20, the 25 % tariff in the large-country model, and the optimal tariff),
out/grain_cases.csv (free trade and Kestria's 25 % retaliation) and out/payoffs.csv
(welfare changes from free trade for the four combinations of the two tariffs)."""
import numpy as np
import pandas as pd
from figout import write_table
from steel import grain, steel


def small(t, pw=20.0):
    """Small-country benchmark: Brenland takes the world price pw as given."""
    p = (1 + t) * pw
    m = 120 - 4 * p
    cs = -((100 - 2 * pw) + (100 - 2 * p)) / 2 * (p - pw)
    ps = ((-20 + 2 * pw) + (-20 + 2 * p)) / 2 * (p - pw)
    return {"t": t, "p_world": pw, "p_home": p, "imports": m, "q_supply": -20 + 2 * p,
            "q_demand": 100 - 2 * p, "cs": cs, "ps": ps, "revenue": (p - pw) * m,
            "tot_gain": 0.0, "dwl": 0.5 * (p - pw) * (40 - m),
            "brenland": cs + ps + (p - pw) * m, "kestria": 0.0}


def optimal():
    ts = np.round(np.linspace(0, 1, 1001), 3)
    return ts[int(np.argmax([steel(t)["brenland"] for t in ts]))]


def tables():
    cases = [("free trade", steel(0.0)), ("small country", small(0.25)),
             ("large country", steel(0.25)), ("optimal tariff", steel(optimal()))]
    s = pd.DataFrame([{"case": n, **v} for n, v in cases])
    g = pd.DataFrame([{"case": "free trade", **grain(0.0)},
                      {"case": "retaliation", **grain(0.25)}])
    rows = []
    for b in (0.0, 0.25):
        for k in (0.0, 0.25):
            rows.append({"brenland_tariff": b, "kestria_tariff": k,
                         "brenland": steel(b)["brenland"] + grain(k)["brenland"],
                         "kestria": steel(b)["kestria"] + grain(k)["kestria"]})
    return s, g, pd.DataFrame(rows)


if __name__ == "__main__":
    s, g, p = tables()
    write_table(s, __file__, "steel_cases")
    write_table(g, __file__, "grain_cases")
    write_table(p, __file__, "payoffs")

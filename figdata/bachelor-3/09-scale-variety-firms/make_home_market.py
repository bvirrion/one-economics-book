"""Chart 3: the home-market effect in the two-country Krugman model with an outside good
(wages equal). Home's share of the differentiated industry's firms against its share of
world spending, s_n = (s_E (1 + lam) - lam) / (1 - lam), clipped to [0, 1], for the
freeness of trade lam = tau^(1 - sigma) = 0.2, 0.5 and 0.8. Writes out/hme.csv."""
import numpy as np
import pandas as pd
from figout import write_table

LAMS = (0.2, 0.5, 0.8)


def share(s_e, lam):
    """Home's share of firms; 0 or 1 when one country has the whole industry."""
    return np.clip((s_e * (1 + lam) - lam) / (1 - lam), 0.0, 1.0)


def table():
    s = np.round(np.linspace(0, 1, 201), 4)
    d = pd.DataFrame({"s_e": s})
    for lam in LAMS:
        d[f"lam{int(lam * 10)}"] = share(s, lam)
    return d


if __name__ == "__main__":
    write_table(table(), __file__, "hme")

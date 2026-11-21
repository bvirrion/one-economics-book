"""Kestria's capital boom (invented): the weekend problem of chapter 8.

Fixed coefficients per unit of output: machines need 3 units of capital and 1 worker,
textiles 1 unit of capital and 2 workers. World prices: 4 kests a machine, 3 a unit
of textiles. Endowments (millions): Kestria K = 60, L = 40; Brenland K = 30, L = 50;
the world K = 1300, L = 1100. Everyone spends half of income on each good.
Writes out/boom_params.csv and out/boom_results.csv (one row per item)."""
import numpy as np
import pandas as pd
from figout import write_table

A = np.array([[3.0, 1.0], [1.0, 2.0]])      # rows: capital, labour; cols: machines, textiles
P = np.array([4.0, 3.0])
WORLD = np.array([1300.0, 1100.0])


def outputs(V):
    return np.linalg.solve(A, V)


def factor_prices(p):
    r, w = np.linalg.solve(A.T, p)            # p_j = r a_Kj + w a_Lj
    return r, w


def trade(V, p=P):
    Q = outputs(V)
    y = p @ Q
    C = 0.5 * y / p
    return Q, y, C, Q - C


def autarky(V):
    Q = outputs(V)
    pm = Q[1] / Q[0]                          # p_M / p_T with p_T = 1, equal spending
    r, w = factor_prices(np.array([pm, 1.0]))
    return Q, pm, r, w


def tables():
    rows = []
    add = rows.append
    Qa, pm, ra, wa = autarky(np.array([60.0, 40.0]))
    add(("autarky p_M/p_T", pm)); add(("autarky r", ra)); add(("autarky w", wa))
    r, w = factor_prices(P)
    add(("trade r", r)); add(("trade w", w))
    for name, V in [("Kestria", np.array([60.0, 40.0])), ("Brenland", np.array([30.0, 50.0])),
                    ("Kestria boom", np.array([75.0, 40.0]))]:
        Q, y, C, T = trade(V)
        F = A @ T
        s = y / (P @ outputs(WORLD))
        hov = V - s * WORLD
        for lab, v in [("Q_M", Q[0]), ("Q_T", Q[1]), ("GDP", y), ("T_M", T[0]),
                       ("T_T", T[1]), ("F_K", F[0]), ("F_L", F[1]), ("s", s),
                       ("HOV_K", hov[0]), ("HOV_L", hov[1])]:
            add((f"{name} {lab}", v))
    res = pd.DataFrame(rows, columns=["item", "value"])
    params = pd.DataFrame({"item": ["machines", "textiles"], "capital": A[0], "labour": A[1],
                           "price": P})
    return params, res


if __name__ == "__main__":
    p, r = tables()
    write_table(p, __file__, "boom_params")
    write_table(r, __file__, "boom_results")

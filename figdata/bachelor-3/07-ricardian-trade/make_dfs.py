"""The Dornbusch--Fischer--Samuelson diagram from a computed example (simulated): 200
goods with ln A(z) = 1.2 - 2.4 z + noise, sorted so that A falls with z (seed 1977);
equal expenditure shares, so theta(z) = z; Foreign's labour force 1.5 times Home's:
B(z) = 1.5 z / (1 - z). The equilibrium is the first good at which B reaches A.
Writes out/dfs_A.csv (z, A), out/dfs_B.csv (z, B), out/dfs_eq.csv (stat, value)."""
import numpy as np
import pandas as pd
from figout import write_table

N, RATIO = 200, 1.5


def curves():
    rng = np.random.default_rng(1977)
    z = (np.arange(N) + 0.5) / N
    A = np.sort(np.exp(1.2 - 2.4 * z + rng.normal(0, 0.15, N)))[::-1]
    B = RATIO * z / (1 - z)
    k = int(np.argmax(B >= A))
    return z, A, B, k


def tables():
    z, A, B, k = curves()
    zb = np.linspace(0.005, 0.8, 160)
    eq = pd.DataFrame({"stat": ["z_bar", "omega", "home_goods"],
                       "value": [z[k], A[k], k]})
    return (pd.DataFrame({"z": z, "A": A}), pd.DataFrame({"z": zb, "B": RATIO * zb / (1 - zb)}),
            eq)


if __name__ == "__main__":
    a, b, e = tables()
    write_table(a, __file__, "dfs_A")
    write_table(b, __file__, "dfs_B")
    write_table(e, __file__, "dfs_eq")

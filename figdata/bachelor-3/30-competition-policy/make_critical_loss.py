"""Chart 2: critical loss of a hypothetical monopolist's price rise, X / (X + m),
against the margin m, for price rises of 5 % and 10 %. Writes out/critical_loss.csv."""
import numpy as np
import pandas as pd
from figout import write_table


def critical_loss(x, m):
    return x / (x + m)


def table():
    m = np.linspace(0.05, 0.8, 76)
    return pd.DataFrame({"m": 100 * m, "x5": 100 * critical_loss(0.05, m),
                         "x10": 100 * critical_loss(0.10, m)})


if __name__ == "__main__":
    write_table(table(), __file__, "critical_loss")

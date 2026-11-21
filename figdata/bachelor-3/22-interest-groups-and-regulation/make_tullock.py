"""Chart 2: share of the rent dissipated in a symmetric Tullock contest against the
number of players. Writes out/tullock.csv."""
import pandas as pd
from figout import write_table
from tullock import dissipation


def table():
    n = list(range(1, 21))
    return pd.DataFrame({"n": n, "share": [100 * dissipation(k) for k in n]})


if __name__ == "__main__":
    write_table(table(), __file__, "tullock")

"""Chart 2: the smallest discount factor at which grim-trigger collusion is
sustainable in a Bertrand market with n identical firms, 1 - 1/n. Writes
out/collusion.csv."""
import pandas as pd
from figout import write_table


def table():
    n = list(range(2, 21))
    return pd.DataFrame({"n": n, "delta": [1 - 1 / k for k in n]})


if __name__ == "__main__":
    write_table(table(), __file__, "collusion")

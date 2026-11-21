"""Chart 2: expected revenue against the reserve price, uniform values on [0, 1],
for 2 and 5 bidders. Writes out/reserve.csv."""
import numpy as np
import pandas as pd
from auctions import revenue_reserve
from figout import write_table


def table():
    r = np.linspace(0, 1, 101)
    return pd.DataFrame({"r": r, "n2": revenue_reserve(r, 2),
                         "n5": revenue_reserve(r, 5)})


if __name__ == "__main__":
    write_table(table(), __file__, "reserve")

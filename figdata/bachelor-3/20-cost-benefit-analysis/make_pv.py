"""Chart 2: present value of 1 dalen received in year t, t = 0..100, at discount
rates of 1.4 %, 3 % and 7 %. Writes out/pv.csv and out/pv_points.csv."""
import numpy as np
import pandas as pd
from figout import write_table

RATES = {"r14": 0.014, "r3": 0.03, "r7": 0.07}


def table():
    t = np.arange(0, 101)
    return pd.DataFrame({"t": t, **{k: (1 + r) ** -t for k, r in RATES.items()}})


if __name__ == "__main__":
    d = table()
    write_table(d, __file__, "pv")
    write_table(d[d.t.isin([30, 50, 100])].reset_index(drop=True), __file__,
                "pv_points")

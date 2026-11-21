"""Weekend problem: Brenland's water company. Writes out/water_stats.csv."""
import pandas as pd
from figout import write_table
from water import aj, average_cost, cap, marginal_cost, monopoly, sharing_x

if __name__ == "__main__":
    x = sharing_x()
    parts = {"mon": monopoly(), "ac": average_cost(), "mc": marginal_cost(),
             "aj": aj(), "cap0": cap(0.0, 16.0, 150.0), "capx": cap(x, 16.0, 150.0),
             "ac16": average_cost(16.0)}
    rows = [(f"{k}_{s}", v) for k, d in parts.items() for s, v in d.items()]
    rows.append(("x_share", x))
    write_table(pd.DataFrame(rows, columns=["stat", "value"]), __file__, "water_stats")

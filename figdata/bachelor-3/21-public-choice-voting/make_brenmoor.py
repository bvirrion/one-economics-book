"""Weekend problem: Brenmoor votes on a pool. Writes out/brenmoor_stats.csv and
out/brenmoor_u.csv (the median household's net benefit by pool size)."""
import numpy as np
import pandas as pd
from brenmoor import capitalisation, ideal, mr_rate, setter, utility
from country import load
from figout import write_table


def stats():
    h = load("households")
    sizes = h["size"]
    med_n = float(sizes.median())
    share_le2 = 100 * (sizes <= 2).mean()
    med_y, mean_y = h.gross_income.median(), h.gross_income.mean()
    rows = {"median_size": med_n, "share_size1": 100 * (sizes <= 1).mean(),
            "share_le_2b": share_le2, "q_median": ideal(med_n),
            "q_mean_size": ideal(sizes.mean()), "u_reversion": utility(2.0, med_n),
            "q_setter": setter(med_n), "q_setter_q0_1": setter(med_n, 1.0),
            "median_income": med_y, "mean_income": mean_y, "ratio": med_y / mean_y,
            "t_mr": 100 * mr_rate(med_y, mean_y), "transfer": mr_rate(med_y, mean_y)
            * mean_y * (1 - 0.25 * mr_rate(med_y, mean_y)),
            "capitalisation": capitalisation()}
    return pd.DataFrame({"stat": list(rows), "value": list(rows.values())})


def curve():
    q = np.linspace(0.5, 20, 196)
    return pd.DataFrame({"q": q, "u": utility(q, 2.0)})


if __name__ == "__main__":
    write_table(stats(), __file__, "brenmoor_stats")
    write_table(curve(), __file__, "brenmoor_u")

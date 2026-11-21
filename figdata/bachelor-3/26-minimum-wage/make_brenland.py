"""Weekend problem: a minimum wage for Brenland. Data: hourly wages of the working
heads in the household survey (gross income over hours). Assumptions: a floor of 12
dalens an hour; a labour-demand elasticity of 1.0 for the competitive prediction;
the firm of monopsony.py; after the floor, a tenth of the jobs below 12 disappear and
the rest move to 12-13; border-region employment index 100 to 99.0 in Brenland and 100
to 100.5 in Kestria. Writes out/brenland_stats.csv and out/brenland_hist.csv."""
import numpy as np
import pandas as pd
from country import load
from figout import write_table
from monopsony import competitive, employment, monopsony, supply_elasticity

FLOOR, E_DEMAND, LOSS = 12.0, 1.0, 0.10


def wages():
    h = load("households")
    w = h[h.hours > 0]
    return (w.gross_income / w.hours).to_numpy()


def stats():
    w = wages()
    below = w < FLOOR
    gap = (FLOOR - w[below]) / w[below]
    lm, wm = monopsony()
    lc, wc = competitive()
    n_below = int(below.sum())
    missing, excess = n_below, (1 - LOSS) * n_below
    did = (99.0 - 100) - (100.5 - 100)
    rows = {"n": len(w), "median": float(np.median(w)), "kaitz": FLOOR / np.median(w),
            "share_below": 100 * below.mean(), "n_below": n_below,
            "mean_raise": 100 * gap.mean(),
            "comp_loss": E_DEMAND * 100 * gap.mean(),
            "l_mon": lm, "w_mon": wm, "l_comp": lc, "w_comp": wc,
            "eps": supply_elasticity(lm), "markdown": 1 / (1 + supply_elasticity(lm)),
            "mrp_mon": 20 - 0.1 * lm, "l_floor12": employment(12.0),
            "l_floor15": employment(15.0), "l_floor17": employment(17.0),
            "w_back": 20 - 0.1 * lm, "missing": missing, "excess": excess,
            "bunch_change": excess - missing,
            "bunch_pct": 100 * (excess - missing) / len(w), "did": did,
            "own_wage": did / (100 * gap.mean() * below.mean())}
    return pd.DataFrame({"stat": list(rows), "value": list(rows.values())})


def hist():
    w = wages()
    bins = np.arange(2, 31)
    before, _ = np.histogram(w, bins)
    after = before.astype(float).copy()
    below = bins[:-1] < FLOOR
    moved = before[below].sum() * (1 - LOSS)
    after[below] = 0
    after[bins[:-1] == FLOOR] += moved
    return pd.DataFrame({"bin": bins[:-1] + 0.5, "before": before, "after": after})


if __name__ == "__main__":
    write_table(stats(), __file__, "brenland_stats")
    write_table(hist(), __file__, "brenland_hist")

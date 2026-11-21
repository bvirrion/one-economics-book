"""Weekend problem: reforming Brenland's income support. Writes
out/brenland_stats.csv and out/brenland_budget.csv (net income of a single parent
with two children, household size 3, before and after the reform)."""
import numpy as np
import pandas as pd
from brenland_benefit import WAGE, gini, net, ptr, support_full, survey
from figout import write_table


def escape_income(size=3):
    """Lowest gross income above the cliff at which net income matches the net
    just below it (search in steps of 10 dalens)."""
    below = net(11_990, size)
    for g in np.arange(12_000, 60_000, 10):
        if net(g, size) >= below:
            return float(g)
    return float("nan")


def stats():
    h = survey()
    esc = escape_income()
    rows = {"support_3": support_full(3), "net0_old": net(0, 3),
            "net11990_old": net(11_990, 3), "net12000_old": net(12_000, 3),
            "cliff_loss": net(11_990, 3) - net(12_000, 3), "escape": esc,
            "escape_hours": esc / WAGE, "ptr15_old": 100 * ptr(15_000, 3),
            "ptr15_new": 100 * ptr(15_000, 3, True), "net15_new": net(15_000, 3, True),
            "net15_old": net(15_000, 3), "ptr8_old": 100 * ptr(8_000, 3),
            "ptr8_new": 100 * ptr(8_000, 3, True), "breakeven_3": support_full(3) / 0.5,
            "cost_total": (h.new - h.old).sum(), "cost_per_hh": (h.new - h.old).mean(),
            "gainers": int((h.new > h.old).sum()), "losers": int((h.new < h.old).sum()),
            "gini_gross": gini(h.gross_income), "gini_old": gini(h.disp_old),
            "gini_new": gini(h.disp_new), "n_below_cliff": int((h.gross_income
                                                               < 12_000).sum())}
    return pd.DataFrame({"stat": list(rows), "value": list(rows.values())})


def budget():
    g = np.arange(0, 40_001, 100, dtype=float)
    return pd.DataFrame({"gross": g, "old": [net(x, 3) for x in g],
                         "new": [net(x, 3, True, x > 0) for x in g]})


if __name__ == "__main__":
    write_table(stats(), __file__, "brenland_stats")
    write_table(budget(), __file__, "brenland_budget")

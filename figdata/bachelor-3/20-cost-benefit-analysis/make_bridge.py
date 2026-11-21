"""Weekend problem: the Brenmoor bridge. Writes out/bridge_stats.csv and
out/bridge_npv.csv (NPV against the discount rate, before and after the
reference-class correction)."""
import numpy as np
import pandas as pd
from bridge import (COST, DEATHS_AVOIDED, MAINT, UPLIFT, VSL, irr, npv,
                    time_benefit)
from figout import write_table


def stats():
    tb = time_benefit()
    rows = {"cost_forecast": sum(COST), "cost_corrected": sum(COST) * (1 + UPLIFT),
            "time_benefit": tb, "safety_benefit": DEATHS_AVOIDED * VSL,
            "net_annual": tb + DEATHS_AVOIDED * VSL - MAINT,
            "npv2": npv(0.02), "npv35": npv(0.035), "npv7": npv(0.07),
            "npv2_c": npv(0.02, UPLIFT), "npv35_c": npv(0.035, UPLIFT),
            "npv7_c": npv(0.07, UPLIFT), "irr": 100 * irr(), "irr_c": 100 * irr(UPLIFT),
            "uplift": 100 * UPLIFT}
    return pd.DataFrame({"stat": list(rows), "value": list(rows.values())})


def curve():
    r = np.linspace(0.005, 0.10, 96)
    return pd.DataFrame({"rate": 100 * r, "npv": [npv(x) for x in r],
                         "npv_c": [npv(x, UPLIFT) for x in r]})


if __name__ == "__main__":
    write_table(stats(), __file__, "bridge_stats")
    write_table(curve(), __file__, "bridge_npv")

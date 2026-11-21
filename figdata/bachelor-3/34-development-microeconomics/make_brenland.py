"""Weekend problem: writes out/cash_assets.csv (treated households: assets before
plus transfer, assets after two years) and out/cash_stats.csv."""
import pandas as pd
from cashprog import experiment, stats
from figout import write_table

if __name__ == "__main__":
    e = experiment()
    t = e[e.treat]
    write_table(pd.DataFrame({"before": (t.a0 + t["T"]) / 1000, "after": t.a2 / 1000}),
                __file__, "cash_assets")
    st = stats()
    write_table(pd.DataFrame({"stat": list(st), "value": list(st.values())}),
                __file__, "cash_stats")

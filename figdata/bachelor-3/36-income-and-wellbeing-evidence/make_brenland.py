"""Weekend problem: writes out/brenland_stats.csv."""

import pandas as pd
from brenland import stats
from figout import write_table

if __name__ == "__main__":
    st = stats()
    write_table(
        pd.DataFrame({"stat": list(st), "value": list(st.values())}),
        __file__,
        "brenland_stats",
    )

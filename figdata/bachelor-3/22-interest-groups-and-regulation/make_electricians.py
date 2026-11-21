"""Weekend problem: Brenland licenses its electricians. Writes
out/electricians_stats.csv."""
import pandas as pd
from electricians import stats
from figout import write_table

if __name__ == "__main__":
    s = stats()
    write_table(pd.DataFrame({"stat": list(s), "value": list(s.values())}),
                __file__, "electricians_stats")

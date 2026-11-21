"""Weekend problem: Brenland's graduates. Writes out/brenland_series.csv and
out/brenland_stats.csv."""
import pandas as pd
from brenland import series, stats
from figout import write_table

if __name__ == "__main__":
    write_table(series(), __file__, "brenland_series")
    s = stats()
    write_table(pd.DataFrame({"stat": list(s), "value": list(s.values())}),
                __file__, "brenland_stats")

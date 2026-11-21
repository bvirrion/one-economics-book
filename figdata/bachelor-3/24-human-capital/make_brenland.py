"""Weekend problem: the last year of school in Brenland. Writes
out/brenland_stats.csv."""
import pandas as pd
from brenland import stats
from figout import write_table

if __name__ == "__main__":
    s = stats()
    write_table(pd.DataFrame({"stat": list(s), "value": list(s.values())}),
                __file__, "brenland_stats")

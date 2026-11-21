"""Weekend problem: three bakeries in Brenmoor. Writes out/bakeries_stats.csv."""
import pandas as pd
from bakeries import stats
from figout import write_table

if __name__ == "__main__":
    s = stats()
    write_table(pd.DataFrame({"stat": list(s), "value": list(s.values())}),
                __file__, "bakeries_stats")

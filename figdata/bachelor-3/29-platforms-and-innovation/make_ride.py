"""Weekend problem: Brenmoor's ride platform. Writes out/ride_stats.csv."""
import pandas as pd
from figout import write_table
from ride import decomposition, network, platform

if __name__ == "__main__":
    s = {**network(), **platform(), **decomposition()}
    write_table(pd.DataFrame({"stat": list(s), "value": list(s.values())}),
                __file__, "ride_stats")

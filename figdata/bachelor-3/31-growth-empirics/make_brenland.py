"""Weekend problem: Brenland's fifty years. Writes out/brenland_series.csv,
out/brenland_peers.csv and out/brenland_stats.csv."""
import pandas as pd
from brenland import peers, series, stats
from figout import write_table

if __name__ == "__main__":
    s = series()
    write_table(pd.DataFrame({"year": s.index, "y": s.values}), __file__,
                "brenland_series")
    write_table(peers(), __file__, "brenland_peers")
    st = stats()
    write_table(pd.DataFrame({"stat": list(st), "value": list(st.values())}),
                __file__, "brenland_stats")

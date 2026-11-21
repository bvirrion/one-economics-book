"""Weekend problem: writes out/river_north.csv, out/river_south.csv,
out/river_synth.csv (income per person, thousands of dalens) and
out/river_stats.csv."""
import numpy as np
import pandas as pd
from figout import write_table
from river import panel, stats, synth

if __name__ == "__main__":
    p = panel()
    _, sc = synth(p)
    for name, s in [("north", p.North), ("south", p.South), ("synth", sc)]:
        write_table(pd.DataFrame({"year": p.index, "y": np.exp(s.values) / 1000}),
                    __file__, f"river_{name}")
    st = stats()
    write_table(pd.DataFrame({"stat": list(st), "value": list(st.values())}),
                __file__, "river_stats")

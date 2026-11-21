"""Opening chart: share of firms that export, by manufacturing industry, United States
2002 (Bernard, Jensen, Redding and Schott 2007, Table 2; cited numbers, ledger
b3sv:bjrs.t2.<naics>). Industries sorted by the share that export; `pos` 1 is the
highest. Writes out/exporters.csv and out/exporters_all.csv (the aggregate row)."""
import pandas as pd
from cited import load_cited
from figout import write_table


def tables():
    d = load_cited(__file__, "exporters").drop(columns="ledger")
    is_all = d.industry == "All manufacturing"
    agg = d[is_all].reset_index(drop=True)
    d = d[~is_all].sort_values(["exporting", "industry"], ascending=[False, True])
    d = d.reset_index(drop=True)
    d.insert(0, "pos", range(1, len(d) + 1))
    return d, agg


if __name__ == "__main__":
    d, agg = tables()
    write_table(d, __file__, "exporters")
    write_table(agg, __file__, "exporters_all")

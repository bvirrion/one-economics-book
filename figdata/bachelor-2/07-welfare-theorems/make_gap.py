"""The London-New York wheat price gap and its parts, Book 4, chapter 7 opening chart.

Reads src/persson2002.csv, Table 3 of Persson (2002): for four periods, the London
price of American wheat minus the New York price, in per cent of the New York price
(differential), split into freight (transport), insurance and port charges (charges,
the author's assumed 3.75 and 2.75 per cent) and the residual (ledger
b2:persson2002-t3). Writes
  out/gap.csv          pos, period, transport, charges, residual, differential
  out/gap_summary.csv  one row: fall in the differential, fall in transport cost and
                       the share of the fall due to transport (first to last period),
                       residual first and last, and the largest gap between a printed
                       differential and the sum of its printed parts (rounding)
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "persson2002").drop(columns="ledger")
    for c in ["differential", "transport", "charges", "residual"]:
        d[c] = d[c].astype(float)
    d.insert(0, "pos", range(1, len(d) + 1))
    return d


def summary():
    d = table()
    first, last = d.iloc[0], d.iloc[-1]
    fall = first.differential - last.differential
    tfall = first.transport - last.transport
    parts = d.transport + d.charges + d.residual
    return pd.DataFrame(
        [
            {
                "fall": round(fall, 1),
                "transport_fall": round(tfall, 1),
                "share_transport": round(100 * tfall / fall, 0),
                "residual_first": first.residual,
                "residual_last": last.residual,
                "max_rounding": round((parts - d.differential).abs().max(), 2),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "gap")
    write_table(summary(), __file__, "gap_summary")

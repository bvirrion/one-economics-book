"""Contributions in a public-goods experiment, chapter 10 opening chart.

Reads src/fg2000.csv, the mean contributions of Tables 3 and 4 of Fehr and Gaechter
(1999/2000), in tokens out of an endowment of 20 (src/fg2000_design.csv), for groups
re-formed each period (Strangers) and fixed groups (Partners), without and with
punishment, over all ten periods and in the final period (ledgers b2:fg2000-*).
Writes
  out/contrib.csv          pos, label, all (mean over ten periods) and final (final
                           period), both in per cent of the endowment
  out/contrib_summary.csv  the four no-punishment shares, and the largest one
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def endowment():
    return float(load_cited(__file__, "fg2000_design").endowment.iloc[0])


def table():
    d = load_cited(__file__, "fg2000").drop(columns="ledger")
    y = endowment()
    rows = []
    for _, r in d.iterrows():
        for cond, tag in [("no punishment", "without"), ("punishment", "with")]:
            rows.append(
                {
                    "label": f"{r.treatment}: {cond}",
                    "all": round(100 * float(r[f"all_{tag}"]) / y, 1),
                    "final": round(100 * float(r[f"final_{tag}"]) / y, 1),
                }
            )
    out = pd.DataFrame(rows)
    out.insert(0, "pos", range(1, len(out) + 1))
    return out


def summary():
    d = table().set_index("label")
    s = d.loc[["Strangers: no punishment", "Partners: no punishment"]]
    return pd.DataFrame(
        [
            {
                "strangers_all": s["all"].iloc[0],
                "strangers_final": s["final"].iloc[0],
                "partners_all": s["all"].iloc[1],
                "partners_final": s["final"].iloc[1],
                "largest": d["final"].max(),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "contrib")
    write_table(summary(), __file__, "contrib_summary")

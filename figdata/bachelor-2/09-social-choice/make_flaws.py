"""How often voting theory's flaws appear in real elections, chapter 9 opening chart.

Reads src/gsm2023.csv, the failure rates of Table 7 of Graham-Squire and McCune
(2023) for 182 US ranked-choice elections of 2004--2022, and src/gsm2023_counts.csv,
the number of those elections without a Condorcet winner (ledger b2:gsm2023-t7).
Writes
  out/flaws.csv          pos, flaw, rate (per cent), the computed row "No Condorcet
                         winner" first
  out/flaws_summary.csv  the share without a Condorcet winner, in per cent, and the
                         largest printed rate
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def no_winner_rate():
    c = load_cited(__file__, "gsm2023_counts").iloc[0]
    return round(100 * int(c.without_winner) / int(c.elections), 2)


def table():
    d = load_cited(__file__, "gsm2023").drop(columns="ledger")
    d["rate"] = d["rate"].astype(float)
    top = pd.DataFrame([{"flaw": "No Condorcet winner", "rate": no_winner_rate()}])
    d = pd.concat([top, d], ignore_index=True)
    d.insert(0, "pos", range(1, len(d) + 1))
    return d


def summary():
    d = table()
    return pd.DataFrame([{"no_winner": no_winner_rate(), "largest": d.rate.max()}])


if __name__ == "__main__":
    write_table(table(), __file__, "flaws")
    write_table(summary(), __file__, "flaws_summary")

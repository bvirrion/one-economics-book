"""The Allais pairs: shares choosing the less risky option, Kahneman and Tversky (1979).

Reads src/kt1979.csv (typed from the article's text: Problems 1-4, with N and the
percentage choosing each option; ledger rows b2:kt1979-p1 ... p4) and writes
  out/allais.csv  pos, certain, scaled, gap, n
one row per pair of problems: pos 1 = Problems 1-2 (common consequence),
pos 2 = Problems 3-4 (common ratio). `certain` is the percentage choosing the
option with the sure prize, `scaled` the percentage choosing the matching option
once both are scaled down; expected utility says each respondent makes the same
choice in both, so the two shares should match. `gap` = certain - scaled.
Book 4, chapter 1, opening chart.
"""

import pandas as pd
from cited import load_cited
from figout import write_table

PAIRS = ["common_consequence", "common_ratio"]


def table():
    d = load_cited(__file__, "kt1979").drop(columns="ledger")
    rows = []
    for pos, pair in enumerate(PAIRS, start=1):
        g = d[d.pair == pair].set_index("version")
        assert (g.safer + g.riskier == 100).all()
        rows.append(
            {
                "pos": pos,
                "certain": g.safer["certain"],
                "scaled": g.safer["scaled"],
                "gap": g.safer["certain"] - g.safer["scaled"],
                "n": g.n["certain"],
            }
        )
    return pd.DataFrame(rows)


if __name__ == "__main__":
    write_table(table(), __file__, "allais")

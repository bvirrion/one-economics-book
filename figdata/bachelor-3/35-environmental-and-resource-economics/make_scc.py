"""Chart 3: the U.S. EPA's 2023 social cost of carbon dioxide by emission year at three
near-term discount rates (2020 dollars per tonne; cited table src/scc.csv). Writes
out/scc.csv."""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "scc")
    for c in ("year", "r25", "r20", "r15"):
        d[c] = d[c].astype(float)
    return d[["year", "r25", "r20", "r15"]]


if __name__ == "__main__":
    write_table(table(), __file__, "scc")

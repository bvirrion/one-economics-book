"""Chart of cited numbers: cumulative changes in yields over the eight announcement
days of the Federal Reserve's first asset purchases, and over the whole period from
24 November 2008 to 28 January 2010 (basis points; Gagnon, Raskin, Remache and Sack
2010, Table 1; ledger b3cb:grrs.t1). Writes out/lsap.csv."""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "lsap").drop(columns="ledger")
    for c in ("events", "whole"):
        d[c] = d[c].astype(float)
    d.insert(1, "pos", range(1, len(d) + 1))
    return d


if __name__ == "__main__":
    write_table(table(), __file__, "lsap")

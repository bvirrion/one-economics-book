"""Opening chart: revenue of the European third-generation mobile licence auctions,
2000--2001, euros per head (Klemperer 2002, Table 1; cited numbers). Writes
out/spectrum.csv with a position, the 2000 auctions first."""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "spectrum").drop(columns="ledger")
    d = d.iloc[::-1].reset_index(drop=True)
    d["pos"] = range(len(d))
    return d


if __name__ == "__main__":
    write_table(table(), __file__, "spectrum")

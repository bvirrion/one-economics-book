"""Opening chart: estimated price changes after two U.S. consumer-product mergers
(Pennzoil/Quaker State; Procter & Gamble/Tambrands), by product, against two control
groups: private-label products and other branded products (Ashenfelter and Hosken
2008, section 5; cited numbers, percent). Writes out/mergers.csv with a position."""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "mergers").drop(columns="ledger")
    d["pos"] = range(len(d))
    return d


if __name__ == "__main__":
    write_table(table(), __file__, "mergers")

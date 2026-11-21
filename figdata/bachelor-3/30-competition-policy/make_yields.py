"""Opening chart: U.S. domestic airlines, annual rates of change of the real average
yield (revenue per passenger-mile) and of traffic (revenue passenger-miles), before
and after the 1978 deregulation (Borenstein and Rose 2007, section on price levels;
cited numbers, percent a year). Writes out/yields.csv with a position."""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "yields").drop(columns="ledger")
    d["pos"] = range(len(d))
    return d


if __name__ == "__main__":
    write_table(table(), __file__, "yields")

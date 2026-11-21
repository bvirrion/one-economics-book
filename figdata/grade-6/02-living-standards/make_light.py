"""g6-02: the labour price of light, 1800-1992 (cited numbers, Nordhaus 1996, Table 1.6).

light.csv  year, hours (hours of work per 1,000 lumen-hours), device, pos (label anchor)
"""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "light").drop(columns="ledger")
    # label anchor: below the point where the line rises after it, beside it elsewhere
    d["pos"] = ["north west" if y == 1800 else "west" for y in d.year]
    return d


if __name__ == "__main__":
    write_table(table(), __file__, "light")

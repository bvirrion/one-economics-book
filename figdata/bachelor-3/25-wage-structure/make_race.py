"""Opening chart: the race between education and technology, United States,
1914-2017: annual log changes (x 100) in the college wage premium, the relative
supply of college equivalents and their relative demand (sigma = 1.62), by period
(Autor, Goldin and Katz 2020, Table A2; cited numbers). Writes out/race.csv with a
position for each period."""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "race").drop(columns="ledger")
    d["pos"] = range(len(d))
    return d


if __name__ == "__main__":
    write_table(table(), __file__, "race")

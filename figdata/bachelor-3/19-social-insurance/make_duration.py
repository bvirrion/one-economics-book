"""Opening chart: extra weeks out of work per extra week of potential benefit
duration, by study (cited abstracts; ranges where the study gives one; Lalive's
are lower bounds). Writes out/duration.csv."""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "duration").drop(columns="ledger").reset_index(drop=True)
    d["pos"] = range(len(d))
    d["mid"] = (d.low + d.high) / 2
    d["err"] = (d.high - d.low) / 2
    return d


if __name__ == "__main__":
    write_table(table(), __file__, "duration")

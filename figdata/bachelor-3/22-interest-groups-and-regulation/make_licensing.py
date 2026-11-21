"""Opening chart: share of U.S. workers who need a licence, by three measures (cited
numbers): State licensing laws (less than 5 % in the early 1950s, drawn at 5; 25 %
in 2008), a commissioned survey counting all levels of government (29 %, 2008) and the
Current Population Survey's licence question (2015 on). Writes out/lic_<measure>.csv."""
from cited import load_cited
from figout import write_table


def tables():
    d = load_cited(__file__, "licensing").drop(columns="ledger")
    return {m: g[["year", "share"]].reset_index(drop=True)
            for m, g in d.groupby("measure")}


if __name__ == "__main__":
    for m, t in tables().items():
        write_table(t, __file__, f"lic_{m}")

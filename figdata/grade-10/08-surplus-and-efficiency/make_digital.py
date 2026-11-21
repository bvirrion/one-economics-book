"""Median willingness to accept to give up a free digital good for a year (United States, 2016 and 2017).

Grade 10, chapter 8 (surplus-and-efficiency): consumer surplus that GDP does not count. The numbers are
typed from Table 1 of Brynjolfsson, Collis and Eggers (2019, PNAS) and each row is a ledger fact
(figdata/lib/cited.py checks them).
Writes:
  out/digital_wta.csv  rank (1 = largest), category, wta2016, wta2017 (dollars a year)
"""
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "digital_wta").drop(columns="ledger")
    d["wta2016"] = d.wta2016.astype(int)
    d["wta2017"] = d.wta2017.astype(int)
    d = d.sort_values("wta2017", ascending=True).reset_index(drop=True)
    d.insert(0, "rank", range(len(d), 0, -1))
    return d


if __name__ == "__main__":
    write_table(table(), __file__, "digital_wta")

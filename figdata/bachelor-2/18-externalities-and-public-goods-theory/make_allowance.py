"""Spot prices of US sulphur-dioxide allowances at EPA's annual auctions, as quoted by
Schmalensee and Stavins (2012/2013): 2004, 2005, 2008, 2009 and 2012 (dollars a ton).
Chapter 18, chart 2. Reads src/ss2013.csv (ledger b2:ss2013-prices); writes
out/allowance.csv (year, price).
"""

from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "ss2013")
    d["price"] = d.price.astype(float)
    d["year"] = d.year.astype(int)
    return d[["year", "price"]]


if __name__ == "__main__":
    write_table(table(), __file__, "allowance")

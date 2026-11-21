"""Join two sources on (iso3, year) and count what did not match."""

from econdata import pwt, wdi

w = wdi("NY.GDP.PCAP.PP.KD", since=2019, until=2019)  # World Bank
p = pwt(since=2019, until=2019, cols=["rgdpe", "pop"])  # Penn World Table
m = w.merge(p, on=["iso3", "year"], how="outer", indicator=True)
print(m["_merge"].value_counts())

left = m[m["_merge"] == "left_only"]
print("only in the World Bank table:", sorted(left.iso3)[:8])
right = m[m["_merge"] == "right_only"]
print("only in the Penn table:", sorted(right.iso3))

"""A merge on too few keys multiplies rows without any error."""

from econdata import pwt, wdi

w = wdi("NY.GDP.PCAP.PP.KD", since=2015, until=2019, countries_only=True)
p = pwt(since=2015, until=2019, cols=["rgdpe", "pop"])
print("rows:", len(w), len(p))

bad = w.merge(p, on="iso3")  # forgot the year
print("merged on iso3 alone:", len(bad))

good = w.merge(p, on=["iso3", "year"], validate="one_to_one")
print("merged on (iso3, year):", len(good))

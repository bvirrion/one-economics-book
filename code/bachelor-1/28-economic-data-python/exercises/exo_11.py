"""Exercise 11: a silent error, codes in lower case in one table."""

from econdata import pwt, wdi

w = wdi("NY.GDP.PCAP.PP.KD", since=2019, until=2019, countries_only=True)
p = pwt(since=2019, until=2019, cols=["rgdpe", "pop"])
p_bad = p.assign(iso3=p.iso3.str.lower())  # as a careless export might write them
bad = w.merge(p_bad, on=["iso3", "year"], how="left")
fixed = w.merge(
    p_bad.assign(iso3=p_bad.iso3.str.upper()), on=["iso3", "year"], how="left"
)

if __name__ == "__main__":
    print("rows:", len(bad), "with Penn data:", bad.rgdpe.notna().sum())
    print("after the fix:", fixed.rgdpe.notna().sum())

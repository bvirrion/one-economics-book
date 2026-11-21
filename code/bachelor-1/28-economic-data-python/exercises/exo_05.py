"""Exercise 5: merge Penn World Table and Maddison GDP per person, 2019."""

from econdata import maddison, pwt

p = pwt(since=2019, until=2019, cols=["rgdpe", "pop"])
m = maddison(since=2019, until=2019)
j = p.merge(m, on=["iso3", "year"], how="outer", indicator=True)
counts = j["_merge"].value_counts()

if __name__ == "__main__":
    print(counts)
    print("only Penn:", sorted(j.loc[j["_merge"] == "left_only", "iso3"]))
    print("only Maddison:", sorted(j.loc[j["_merge"] == "right_only", "iso3"]))

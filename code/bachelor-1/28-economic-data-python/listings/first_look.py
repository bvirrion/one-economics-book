"""A first look at a table: Penn World Table rows for France and Germany."""

from econdata import pwt

d = pwt(["FRA", "DEU"], since=2015, cols=["rgdpe", "pop", "emp"])
print(d.shape)  # (rows, columns)
print(d.dtypes)
print(d.head(4))

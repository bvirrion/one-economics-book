"""Long and wide: GDP per person of five countries, 2019-2023."""

from econdata import pwt

d = pwt(["BRA", "CHN", "DEU", "IND", "USA"], since=2019, cols=["rgdpe", "pop"])
d["gdppc"] = (d.rgdpe / d["pop"]).round(0)  # dollars per person
long = d[["iso3", "year", "gdppc"]]
print("long:", long.shape)
print(long.head(3))

wide = long.pivot(index="iso3", columns="year", values="gdppc")
print("wide:", wide.shape)
print(wide)

back = wide.reset_index().melt(id_vars="iso3", value_name="gdppc")
print("back to long:", back.shape)

"""Euro area, 2000-2023: three growth rates from the same accounts."""

from econdata import eurostat, wdi

g = eurostat("nama_10_gdp")
g = g[(g.geo == "EA20") & (g.na_item == "B1GQ")]
g = g.assign(time=g.time.astype(int))
real = g[g.unit == "CLV20_MEUR"].set_index("time").value  # chained volumes
nominal = g[g.unit == "CP_MEUR"].set_index("time").value  # current prices
pop = wdi("SP.POP.TOTL", isos=["EMU"]).set_index("year").value


def yearly(x, a=2000, b=2023):
    return 100 * ((x[b] / x[a]) ** (1 / (b - a)) - 1)


print(f"GDP, current prices     {yearly(nominal):.2f} % a year")
print(f"GDP, volumes            {yearly(real):.2f} % a year")
print(f"GDP per person, volumes {yearly(real / pop):.2f} % a year")

"""Exercise 9: the euro-area growth rates for 2000-2019, before the pandemic."""

from econdata import eurostat, wdi

g = eurostat("nama_10_gdp")
g = g[(g.geo == "EA20") & (g.na_item == "B1GQ")]
g = g.assign(time=g.time.astype(int))
real = g[g.unit == "CLV20_MEUR"].set_index("time").value
nominal = g[g.unit == "CP_MEUR"].set_index("time").value
pop = wdi("SP.POP.TOTL", isos=["EMU"]).set_index("year").value


def yearly(x, a=2000, b=2019):
    return round(100 * ((x[b] / x[a]) ** (1 / (b - a)) - 1), 2)


rates = {
    "nominal": yearly(nominal),
    "real": yearly(real),
    "per_person": yearly(real / pop),
}

if __name__ == "__main__":
    print(rates)

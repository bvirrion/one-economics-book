"""Exercise 9: fertility and income, between and within countries, 1990-2022."""
import numpy as np
from econdata import wdi

tfr = wdi("SP.DYN.TFRT.IN", since=1990, until=2022, countries_only=True)
gdp = wdi("NY.GDP.PCAP.KD", since=1990, until=2022, countries_only=True)
d = tfr.merge(gdp, on=["iso3", "year"], suffixes=("_tfr", "_gdp")).dropna()
d["ly"] = np.log(d.value_gdp)
d = d.rename(columns={"value_tfr": "tfr"})


def slope(x, y):
    x, y = x - x.mean(), y - y.mean()
    return (x @ y) / (x @ x)


m = d.groupby("iso3")[["tfr", "ly"]].mean()
w = d[["tfr", "ly"]] - d.groupby("iso3")[["tfr", "ly"]].transform("mean")
print(f"countries {len(m)}, country-years {len(d)}")
print(f"between slope {slope(m.ly, m.tfr):.3f}")
print(f"within slope  {slope(w.ly, w.tfr):.3f}")

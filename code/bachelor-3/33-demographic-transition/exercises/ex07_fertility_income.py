"""Exercise 7: the fertility--income slope across countries, 1960 and 2023. Regress
the total fertility rate (WDI SP.DYN.TFRT.IN) on log10 of GDP per person in
constant 2015 dollars (NY.GDP.PCAP.KD)."""
import numpy as np
from econdata import wdi

for year in (1960, 2023):
    f = wdi("SP.DYN.TFRT.IN", since=year, until=year, countries_only=True)
    g = wdi("NY.GDP.PCAP.KD", since=year, until=year, countries_only=True)
    d = f[["iso3", "value"]].merge(g[["iso3", "value"]], on="iso3",
                                   suffixes=("_tfr", "_gdp")).dropna()
    b, a = np.polyfit(np.log10(d.value_gdp), d.value_tfr, 1)
    print(f"{year}: {len(d)} countries, mean TFR {d.value_tfr.mean():.2f}, "
          f"slope {b:+.2f} per tenfold income")

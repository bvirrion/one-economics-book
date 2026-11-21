"""Exercise 5: country and year effects, with iid and country-clustered errors."""
import numpy as np
from econdata import wdi
from paneltools import ols_cluster, twoway_demean

co2 = wdi("EN.GHG.CO2.PC.CE.AR5", since=1990, until=2022, countries_only=True)
gdp = wdi("NY.GDP.PCAP.KD", since=1990, until=2022, countries_only=True)
d = co2.merge(gdp, on=["iso3", "year"], suffixes=("_co2", "_gdp"))
d = d.rename(columns={"value_co2": "co2"}).dropna(subset=["co2", "value_gdp"])
d["ly"] = np.log(d.value_gdp).astype(float)
d = d.reset_index(drop=True)
w = d[["co2", "ly"]] - d.groupby("iso3")[["co2", "ly"]].transform("mean")
tw = twoway_demean(d, ["co2", "ly"], "iso3", "year")
for name, frame in (("country effects", w), ("country and year", tw)):
    r = ols_cluster(frame.co2, frame[["ly"]], d.iso3)
    print(f"{name:17s} slope {r['beta'][0]:.3f}   iid s.e. {r['se_iid'][0]:.3f}"
          f"   clustered s.e. {r['se_cluster'][0]:.3f}")
years = d.groupby("year").ly.mean()
print(f"mean log income rose by {years.iloc[-1] - years.iloc[0]:.3f} from 1990 to 2022")

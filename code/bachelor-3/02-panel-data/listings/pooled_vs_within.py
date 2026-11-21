"""Carbon dioxide and income: pooled, between, within and two-way slopes."""
import numpy as np
import statsmodels.formula.api as smf
from econdata import wdi

co2 = wdi("EN.GHG.CO2.PC.CE.AR5", since=1990, until=2022, countries_only=True)
gdp = wdi("NY.GDP.PCAP.KD", since=1990, until=2022, countries_only=True)
d = co2.merge(gdp, on=["iso3", "year"], suffixes=("_co2", "_gdp"))
d = d.rename(columns={"value_co2": "co2"}).dropna(subset=["co2", "value_gdp"])
d["ly"] = np.log(d.value_gdp)
print(f"countries {d.iso3.nunique()}, country-years {len(d)}")

pooled = smf.ols("co2 ~ ly", d).fit().params["ly"]
means = d.groupby("iso3")[["co2", "ly"]].mean()
between = smf.ols("co2 ~ ly", means).fit().params["ly"]
w = d[["co2", "ly"]] - d.groupby("iso3")[["co2", "ly"]].transform("mean")
within = (w.ly @ w.co2) / (w.ly @ w.ly)
dummies = smf.ols("co2 ~ ly + C(iso3)", d).fit().params["ly"]
twoway = smf.ols("co2 ~ ly + C(iso3) + C(year)", d).fit().params["ly"]

for name, b in [("pooled", pooled), ("between", between), ("within", within),
                ("country dummies", dummies), ("country and year", twoway)]:
    print(f"{name:18s}{b:8.3f}")
share = (w.ly @ w.ly) / ((d.ly - d.ly.mean()) @ (d.ly - d.ly.mean()))
print(f"share of the variance of log income that is within: {share:.3f}")

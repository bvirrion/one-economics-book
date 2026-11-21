"""Exercise 7: the income elasticity of energy use, 2019, by a log-log regression."""

import numpy as np  # noqa: F401 -- np.log is used inside the formula strings
import statsmodels.formula.api as smf
from econdata import eia_energy, wdi

e = eia_energy("Energy consumption per capita", since=2019, until=2019)
e = e[~e.iso3.str.contains(r"\+") & (e.iso3 != "WLD")][["iso3", "value"]]
e = e.drop_duplicates("iso3").rename(columns={"value": "energy"})
g = wdi("NY.GDP.PCAP.PP.KD", None, 2019, 2019, countries_only=True)[["iso3", "value"]]
d = e.merge(g.rename(columns={"value": "gdppc"}), on="iso3")
d = d[(d.energy > 0) & (d.gdppc > 0)].dropna()
fit = smf.ols("np.log(energy) ~ np.log(gdppc)", data=d).fit()
result = {
    "n": len(d),
    "slope": round(fit.params.iloc[1], 3),
    "se": round(fit.bse.iloc[1], 3),
}

if __name__ == "__main__":
    print(result)

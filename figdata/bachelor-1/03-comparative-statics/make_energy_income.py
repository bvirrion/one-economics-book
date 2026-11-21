"""Opening chart and second chart of b1 ch. 3: energy use per person against GDP per
person, logarithmic axes, 2019 and 1990, with least-squares lines in logarithms.

EIA "Energy consumption per capita" (million Btu per person) and WDI
NY.GDP.PCAP.PP.KD (GDP per person, constant 2021 international dollars), countries
only. The slope of each line is the income elasticity read off the chart.
"""
import numpy as np
import pandas as pd
from econdata import eia_energy, wdi
from figout import write_table


def year_table(year):
    e = eia_energy("Energy consumption per capita", since=year, until=year)
    e = e[~e.iso3.str.contains(r"\+") & (e.iso3 != "WLD")][["iso3", "value"]]
    e = e.drop_duplicates("iso3")  # the derived EIA table repeats 12 country rows
    g = wdi("NY.GDP.PCAP.PP.KD", None, year, year, countries_only=True)[["iso3", "value"]]
    d = e.rename(columns={"value": "energy"}).merge(
        g.rename(columns={"value": "gdppc"}), on="iso3")
    d = d[(d.energy > 0) & (d.gdppc > 0)].dropna().sort_values("gdppc")
    return d.reset_index(drop=True)


rows = []
for year in (2019, 1990):
    d = year_table(year)
    b, a = np.polyfit(np.log(d.gdppc), np.log(d.energy), 1)
    t = d.assign(gdppc=d.gdppc.round(0), energy=d.energy.round(2))
    write_table(t, __file__, f"energy_income_{year}")
    xs = np.array([d.gdppc.min(), d.gdppc.max()])
    write_table(pd.DataFrame({"gdppc": xs.round(0), "fit": np.exp(a + b * np.log(xs)).round(3)}),
                __file__, f"energy_fit_{year}")
    rows.append({"year": year, "n": len(d), "slope": round(b, 2), "intercept": round(a, 3),
                 "corr": round(np.corrcoef(np.log(d.gdppc), np.log(d.energy))[0, 1], 2)})
write_table(pd.DataFrame(rows), __file__, "energy_income_stats")

# the same countries in both years: the slope on the common sample
d19, d90 = year_table(2019), year_table(1990)
common = sorted(set(d19.iso3) & set(d90.iso3))
cs = []
for year, d in ((2019, d19), (1990, d90)):
    c = d[d.iso3.isin(common)]
    cs.append({"year": year, "n": len(c),
               "slope": round(np.polyfit(np.log(c.gdppc), np.log(c.energy), 1)[0], 2)})
write_table(pd.DataFrame(cs), __file__, "energy_income_common")

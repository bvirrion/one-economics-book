"""Exercise 11: how the welfare comparison depends on the value of a year of life
(kappa, the flow utility of a U.S. year in units of log consumption): welfare relative
to the United States for six countries with kappa = 3, 5 and 7."""

import numpy as np
from welfare_data import countries, log_welfare

d = countries()
shown = ["FRA", "DEU", "JPN", "BRA", "CHN", "IND"]
table = {k: np.exp(log_welfare(d, k)) for k in (3.0, 5.0, 7.0)}
print("country   kappa 3  kappa 5  kappa 7")
for iso in shown:
    i = d.index[d.iso3 == iso][0]
    print(f"{iso:8s}" + "".join(f"{100 * table[k][i]:8.1f}" for k in table))

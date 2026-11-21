"""Brenland's GDP: nominal to real, an index with 2020 = 100, log growth."""

import numpy as np
from country import load

a = load("accounts").set_index("year")
real = a.gdp / a.deflator * 100  # millions of 2015 dalens
index = (100 * real / real.loc[2020]).round(1)
growth = 100 * np.log(real).diff()  # log points per year
print(index.loc[[2015, 2020, 2025]].to_string())
print("mean log growth 2016-2025:", round(growth.loc[2016:2025].mean(), 2))
print(
    "check against the published real GDP:", round((real - a.real_gdp).abs().max(), 0)
)

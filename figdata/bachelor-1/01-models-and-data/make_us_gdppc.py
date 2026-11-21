"""Nominal and real GDP per person, United States, 1960-2024 (WDI), and their ratio.

Real is in constant local currency (WDI's base year); the implicit deflator is
nominal / real, rescaled to 100 in the base year where the two series meet.
"""
import numpy as np
import pandas as pd
from econdata import wdi
from figout import write_table

nom = wdi("NY.GDP.PCAP.CN", ["USA"], 1960, 2024)[["year", "value"]].rename(columns={"value": "nominal"})
real = wdi("NY.GDP.PCAP.KN", ["USA"], 1960, 2024)[["year", "value"]].rename(columns={"value": "real"})
t = nom.merge(real, on="year").sort_values("year").dropna()
t["deflator"] = 100 * t["nominal"] / t["real"]
t["nominal"] = t["nominal"].round(0)
t["real"] = t["real"].round(0)
t["deflator"] = t["deflator"].round(2)
write_table(t.reset_index(drop=True), __file__, "us_gdppc")

# average continuous growth rates over 1960-2024, per cent per year
first, last = t.iloc[0], t.iloc[-1]
n = last.year - first.year
g = {c: round(100 * np.log(last[c] / first[c]) / n, 2) for c in ["nominal", "real", "deflator"]}
write_table(pd.DataFrame({"years": [n], "g_nominal": [g["nominal"]], "g_real": [g["real"]],
                          "g_deflator": [g["deflator"]],
                          "ratio_nominal": [round(last.nominal / first.nominal, 1)],
                          "ratio_real": [round(last.real / first.real, 2)]}),
            __file__, "us_gdppc_growth")

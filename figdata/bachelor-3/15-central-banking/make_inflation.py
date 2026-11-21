"""Chart 3: twelve-month inflation, January 2019 to December 2025: United States CPI-U
(BLS CUUR0000SA0, computed from the index) and the euro area HICP (Eurostat
prc_hicp_manr, all items, EA, the area of each month). Writes out/inflation.csv
(t = year + (month - 0.5) / 12) and out/inflation_peaks.csv."""
import pandas as pd
from econdata import bls_cpi, eurostat
from figout import write_table


def table():
    c = bls_cpi()
    c = c[c.period.str.match(r"M(0[1-9]|1[0-2])")].copy()
    c["month"] = c.period.str[1:].astype(int)
    c = c.sort_values(["year", "month"]).reset_index(drop=True)
    c["us"] = 100 * (c.value / c.value.shift(12) - 1)
    h = eurostat("prc_hicp_manr")
    h = h[(h.unit == "RCH_A") & (h.coicop == "CP00") & (h.geo == "EA")].copy()
    h["year"] = h.time.str[:4].astype(int)
    h["month"] = h.time.str[5:7].astype(int)
    d = c[["year", "month", "us"]].merge(h[["year", "month", "value"]],
                                         on=["year", "month"])
    d = d.rename(columns={"value": "ea"})
    d = d[d.year.between(2019, 2025)].reset_index(drop=True)
    d["t"] = d.year + (d.month - 0.5) / 12
    return d[["t", "year", "month", "us", "ea"]]


def peaks(d):
    rows = []
    for col in ("us", "ea"):
        i = d[col].idxmax()
        rows.append({"series": col, "peak": d.loc[i, col], "year": d.loc[i, "year"],
                     "month": d.loc[i, "month"],
                     "dec2025": d[(d.year == 2025) & (d.month == 12)][col].iloc[0]})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    d = table()
    write_table(d, __file__, "inflation")
    write_table(peaks(d), __file__, "inflation_peaks")

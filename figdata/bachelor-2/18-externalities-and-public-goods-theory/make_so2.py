"""United States sulphur-dioxide emissions, 1970 to the last CEDS year, chapter 18
opening chart.

CEDS by country and sector: electricity and heat (sectors 1A1a_*) against all other
sectors, million tonnes a year.
Writes
  out/so2.csv          year, power, other, total (Mt)
  out/so2_summary.csv  one row: power and total in 1980, 1990, 1995, 2000, 2010 and
                       the last year; the fall in power-sector emissions 1990 to the
                       last year in per cent; the last year
"""

import pandas as pd
from econdata import ceds
from figout import write_table


def table():
    d = ceds("so2", by="country_sector", isos=["USA"], since=1970)
    d["power"] = d.sector.str.startswith("1A1a")
    t = d.groupby(["year", "power"]).value.sum().unstack() / 1000
    out = pd.DataFrame(
        {"year": t.index, "power": t[True].values, "other": t[False].values}
    )
    out["total"] = out.power + out.other
    return out.round(3)


def summary():
    t = table().set_index("year")
    last = int(t.index.max())
    row = {"last": last}
    for y in [1980, 1990, 1995, 2000, 2010, last]:
        key = "last" if y == last else str(y)
        row[f"power_{key}"] = round(t.loc[y, "power"], 2)
        row[f"total_{key}"] = round(t.loc[y, "total"], 2)
    row["power_fall_pct"] = round(
        100 * (1 - t.loc[last, "power"] / t.loc[1990, "power"])
    )
    return pd.DataFrame([row])


if __name__ == "__main__":
    write_table(table(), __file__, "so2")
    write_table(summary(), __file__, "so2_summary")

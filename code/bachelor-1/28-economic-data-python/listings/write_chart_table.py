# capture: scratch
"""A chart is a table a script wrote: write it twice, compare the bytes."""

import hashlib
from pathlib import Path

from country import load

a = load("accounts")
t = a[["year", "real_gdp", "unemp_rate"]]
for run in (1, 2):
    t.to_csv("chart.csv", index=False, lineterminator="\n")
    digest = hashlib.sha256(Path("chart.csv").read_bytes()).hexdigest()
    print(f"run {run}: sha256 {digest[:16]}")
print(Path("chart.csv").read_text().splitlines()[:3])

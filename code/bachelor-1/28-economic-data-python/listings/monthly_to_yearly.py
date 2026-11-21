"""From monthly to yearly: the average, the end of the year, the published average."""

from cpi_tools import monthly
from econdata import bls_cpi

cpi = monthly("CUUR0000SA0", since=2020, until=2024)
by_year = cpi.groupby(level="year")
out = by_year.mean().round(3).to_frame("average")
out["december"] = by_year.last()

d = bls_cpi("CUUR0000SA0")
published = d[d.period == "M13"].set_index("year").value  # BLS annual average
out["published"] = published.loc[2020:2024]
print(out)

"""The primary balance that holds the debt ratio steady, against the actual one, 2024.

s = (i - g) / (1 + g) * b: i the interest paid in 2024 over the debt at the end of 2023,
g the average growth of nominal GDP over 2019-2024, b the debt ratio at the end of 2024.
"""

from econdata import eurostat

d = eurostat("gov_10dd_edpt1")


def series(item, sector, geo):
    rows = d[(d.na_item == item) & (d.unit == "MIO_EUR")]
    rows = rows[(rows.sector == sector) & (rows.geo == geo)]
    return rows.set_index("time").value


print("country  debt %GDP  interest %  growth %  stabilising  actual primary")
for geo in ["DE", "FR", "IT", "EL"]:
    debt, gdp = series("GD", "S13", geo), series("B1GQ", "S1", geo)
    interest, balance = series("D41PAY", "S13", geo), series("B9", "S13", geo)
    i = interest[2024] / debt[2023]
    g = (gdp[2024] / gdp[2019]) ** (1 / 5) - 1
    b = debt[2024] / gdp[2024]
    s = (i - g) / (1 + g) * b
    primary = (balance[2024] + interest[2024]) / gdp[2024]
    print(
        f"{geo:7}  {100 * b:9.1f}  {100 * i:10.2f}  {100 * g:8.2f}"
        f"  {100 * s:11.2f}  {100 * primary:14.2f}"
    )

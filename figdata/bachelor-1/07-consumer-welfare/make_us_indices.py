"""Opening chart of b1 ch. 7: the US consumer price index (CPI-U, all items, annual average)
and the deflator of household final consumption (current over constant prices, World
Development Indicators), 1990-2024, both 1990 = 100; and their average yearly growth."""
import pandas as pd
from econdata import bls_cpi, wdi
from figout import write_table

c = bls_cpi("CUUR0000SA0")
c = c[(c.period == "M13") & c.year.between(1990, 2024)][["year", "value"]]
c = c.rename(columns={"value": "cpi"}).set_index("year").cpi
cn = wdi("NE.CON.PRVT.CN", ["USA"], 1990, 2024).set_index("year").value
kn = wdi("NE.CON.PRVT.KN", ["USA"], 1990, 2024).set_index("year").value
defl = cn / kn
d = pd.DataFrame({"cpi": 100 * c / c.loc[1990], "deflator": 100 * defl / defl.loc[1990]})
d.index = d.index.astype(int)
d = d.round(2).reset_index().rename(columns={"index": "year"})
assert len(d) == 35 and d.notna().all().all()
write_table(d, __file__, "us_indices")
n = 2024 - 1990
g = pd.DataFrame([{
    "cpi_2024": d.cpi.iloc[-1], "defl_2024": d.deflator.iloc[-1],
    "cpi_growth": round(100 * ((d.cpi.iloc[-1] / 100) ** (1 / n) - 1), 2),
    "defl_growth": round(100 * ((d.deflator.iloc[-1] / 100) ** (1 / n) - 1), 2),
}])
write_table(g, __file__, "us_growth")

"""Second chart of b1 ch. 8: labour-force participation of women and men aged 15-64,
1991-2024, six countries (World Bank WDI, modelled ILO estimates)."""
import pandas as pd
from econdata import wdi
from figout import write_table

ISOS = ["FRA", "DEU", "JPN", "NLD", "GBR", "USA"]
out = []
for code, sex in [("SL.TLF.ACTI.FE.ZS", "women"), ("SL.TLF.ACTI.MA.ZS", "men")]:
    x = wdi(code, ISOS, 1991, 2024)[["iso3", "year", "value"]]
    x["sex"] = sex
    out.append(x)
d = pd.concat(out)
w = d.pivot_table(index="year", columns=["sex", "iso3"], values="value").round(1)
w.columns = [f"{s}_{i.lower()}" for s, i in w.columns]
write_table(w.reset_index(), __file__, "participation")
pts = d[d.year.isin([1991, 2024])].pivot_table(index=["iso3", "sex"], columns="year",
                                                values="value").round(1)
pts.columns = [f"y{c}" for c in pts.columns]
write_table(pts.reset_index(), __file__, "participation_points")

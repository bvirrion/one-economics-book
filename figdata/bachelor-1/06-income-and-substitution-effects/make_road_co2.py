"""Opening chart of b1 ch. 6: carbon dioxide from road transport per person, Sweden against
the unweighted mean of ten western European countries, 1960-2022 (CEDS sector 1A3b_Road,
kt; World Bank population). Also the values in 1960, 1990, 2005 and 2019."""
import pandas as pd
from econdata import ceds, wdi
from figout import write_table

PEERS = ["DNK", "NOR", "FIN", "NLD", "BEL", "DEU", "FRA", "AUT", "CHE", "GBR"]
ISOS = ["SWE", *PEERS]
e = ceds("co2", "country_sector", isos=ISOS, since=1960, until=2022)
e = e[e.sector == "1A3b_Road"][["iso3", "year", "value"]]
p = wdi("SP.POP.TOTL", ISOS, 1960, 2022)[["iso3", "year", "value"]]
d = e.merge(p, on=["iso3", "year"], suffixes=("_kt", "_pop"))
d["t"] = d.value_kt * 1000 / d.value_pop  # tonnes per person
w = d.pivot(index="year", columns="iso3", values="t")
assert w.notna().all().all() and len(w) == 63
out = pd.DataFrame({"year": w.index, "sweden": w.SWE.round(3),
                    "peers": w[PEERS].mean(axis=1).round(3)})
write_table(out, __file__, "road_co2")
write_table(out[out.year.isin([1960, 1990, 2005, 2019])], __file__, "road_co2_points")

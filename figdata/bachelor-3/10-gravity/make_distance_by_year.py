"""Chart 2: the distance elasticity by year, 1996--2020 every four years, by OLS on logs
and by PPML, both with exporter and importer fixed effects (specification of
gravfit.py). Writes out/distance_by_year.csv."""
import pandas as pd
from figout import write_table
from gravfit import load, ols_fe, ppml_fe

YEARS = range(1996, 2021, 4)


def table():
    rows = []
    for y in YEARS:
        d = load(y)
        o, p = ols_fe(d), ppml_fe(d)
        rows.append({"year": y, "pairs": len(d), "ols": o.params["ln_dist"],
                     "ols_se": o.bse["ln_dist"], "ppml": p.params["ln_dist"],
                     "ppml_se": p.bse["ln_dist"]})
    return pd.DataFrame(rows)


if __name__ == "__main__":
    write_table(table(), __file__, "distance_by_year")

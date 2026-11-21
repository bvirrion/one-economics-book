"""Weekend problem: the dalen against the kest. Writes out/dalen.csv (every year),
out/dalen_points.csv (selected years), out/dalen_forecasts.csv and out/dalen_stats.csv:
the AR(1) of the real rate and its half-life, the forecast contest's root mean
squared errors, and the Dornbusch overshoot after a 10 % Kestrian money expansion
with money-demand semi-elasticity LAMBDA (years) and a price-adjustment half-life
HL (years), so theta = ln 2 / HL and the impact change is 10 (1 + 1/(lambda theta))."""
import numpy as np
import pandas as pd
from dalen import K_INFL, K_RATE, ar1, forecasts, table
from figout import write_table

POINTS = [2000, 2007, 2015, 2020, 2025]
LAMBDA, HL, SHOCK = 4.0, 2.5, 10.0


def stats(d, f):
    rho, hl = ar1(d)
    theta = np.log(2) / HL
    impact = SHOCK * (1 + 1 / (LAMBDA * theta))
    rows = [("k_infl", K_INFL), ("k_rate", K_RATE), ("rho", rho), ("half_life", hl),
            ("real_mean", d.real.mean()), ("real_max", d.real.max()),
            ("real_min", d.real.min())]
    rows += [(f"rmse_{m}", np.sqrt((f[f"err_{m}"] ** 2).mean()))
             for m in ("rw", "uip", "ppp")]
    rows += [("lambda", LAMBDA), ("hl_dornbusch", HL), ("theta", theta),
             ("impact", impact), ("overshoot", impact - SHOCK)]
    return pd.DataFrame(rows, columns=["stat", "value"])


if __name__ == "__main__":
    d = table()
    f = forecasts(d)
    write_table(d, __file__, "dalen")
    write_table(d[d.year.isin(POINTS)].reset_index(drop=True), __file__, "dalen_points")
    write_table(f, __file__, "dalen_forecasts")
    write_table(stats(d, f), __file__, "dalen_stats")

"""Weekend problem: Brenland before the factories. Writes out/agrarian_y.csv,
out/agrarian_L.csv (1500--1900) and out/agrarian_stats.csv, which also holds the
pay-as-you-go arithmetic of 2025: employment from accounts.csv and an invented count
of 1,950 thousand people aged 65 and over, with a replacement rate of 40 %."""
import pandas as pd
from agrarian import path, stats
from country import load
from figout import write_table

OLD_2025, REPLACEMENT = 1950.0, 0.40


def payg():
    a = load("accounts").set_index("year")
    emp, pop = a.employed[2025], a["pop"][2025]
    ratio = OLD_2025 / emp
    return {"emp2025": emp, "pop2025": pop, "old2025": OLD_2025,
            "pens_per_worker": ratio, "payg_rate": 100 * REPLACEMENT * ratio}


if __name__ == "__main__":
    d = path()
    write_table(d[["year", "y"]], __file__, "agrarian_y")
    write_table(d[["year", "L"]], __file__, "agrarian_L")
    st = {**stats(), **payg()}
    write_table(pd.DataFrame({"stat": list(st), "value": list(st.values())}),
                __file__, "agrarian_stats")

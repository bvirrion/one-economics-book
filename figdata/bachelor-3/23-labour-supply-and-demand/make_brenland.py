"""Weekend problem: Brenland's working hours. Data: the household survey (hours of
the head, gross income) and the firm census. Assumptions of the problem: an
elasticity of substitution of 0.7 between labour and other inputs, a product-demand
elasticity of 1.5, Hicksian supply elasticities of 0.33 (hours) and 0.25
(participation), and a payroll-tax cut of 5 % of the wage. Writes
out/brenland_stats.csv."""
import numpy as np
import pandas as pd
import statsmodels.api as sm
from country import load
from figout import write_table
from hicks import hicks_marshall, wedge_cut

SIGMA, ETA, E_INT, E_EXT, CUT = 0.7, 1.5, 0.33, 0.25, 0.05


def stats():
    h = load("households")
    young = h[h.age_head < 65]
    work = h[h.hours > 0]
    lw = np.log(work.gross_income / work.hours)
    r = sm.OLS(np.log(work.hours), sm.add_constant(lw)).fit(cov_type="HC1")
    f = load("firms")
    s = f.wage_bill.sum() / f.output.sum()
    e_d = -hicks_marshall(s, SIGMA, ETA)
    th, cost, hrs = wedge_cut(CUT, E_INT + E_EXT, e_d)
    emp = float(load("accounts").set_index("year").loc[2025, "employed"])
    rows = {"zero_hours": 100 * (h.hours == 0).mean(),
            "part_under65": 100 * (young.hours > 0).mean(),
            "part_65": 100 * (h[h.age_head >= 65].hours > 0).mean(),
            "mean_hours": work.hours.mean(), "median_wage": np.exp(lw).median(),
            "slope": r.params.iloc[1], "slope_se": r.bse.iloc[1],
            "labour_share": s, "e_demand": e_d, "take_home": 100 * th,
            "cost": 100 * cost, "hours_total": 100 * hrs,
            "ext": 100 * E_EXT * th, "int": 100 * E_INT * th, "employed": emp,
            "ext_workers": emp * E_EXT * th, "fte_total": emp * hrs}
    return pd.DataFrame({"stat": list(rows), "value": list(rows.values())})


if __name__ == "__main__":
    write_table(stats(), __file__, "brenland_stats")

"""Weekend problem and chart 3: the Baily-Chetty condition for Brenland. Writes
out/fund_curve.csv and out/fund_stats.csv."""
import pandas as pd
from country import load
from figout import write_table
from fund import (ELASTICITY, GAMMA, R_NOW, contribution, cost, curve, drop,
                  optimum)

WAGE = 31_000  # mean annual earnings of Brenland's workers, rounded (problem)
RD_JUMP, RD_EXTRA = 0.9, 6.0  # months of nonemployment, months of entitlement


def tables():
    a = load("accounts").set_index("year").loc[2025]
    u = a.unemp_rate / 100
    unemployed = a.labour_force - a.employed
    r, lhs, rhs = curve(u)
    c = pd.DataFrame({"r": 100 * r, "lhs": lhs, "rhs": rhs})
    r_star = optimum(u)
    rows = {"u": 100 * u, "labour_force": a.labour_force, "unemployed": unemployed,
            "benefit_now": R_NOW * WAGE,
            "spending_now": unemployed * R_NOW * WAGE / 1e3,
            "t_now": 100 * contribution(R_NOW, u), "drop_now": 100 * drop(R_NOW),
            "drop_zero": 100 * drop(0), "gain_now": GAMMA * drop(R_NOW),
            "cost": cost(u), "r_star": 100 * r_star,
            "r_star_exact": 100 * optimum(u, exact=True),
            "t_star": 100 * contribution(r_star, u), "drop_star": 100 * drop(r_star),
            "r_star_eps02": 100 * optimum(u, eps=0.2),
            "r_star_gamma2": 100 * optimum(u, gamma=2.0),
            "duration_change": 100 * ((r_star / R_NOW) ** ELASTICITY - 1),
            "rd_per_month": RD_JUMP / RD_EXTRA, "wage": WAGE}
    return c, pd.DataFrame({"stat": list(rows), "value": list(rows.values())})


if __name__ == "__main__":
    c, s = tables()
    write_table(c, __file__, "fund_curve")
    write_table(s, __file__, "fund_stats")

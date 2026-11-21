"""Weekend problem: the Bank of Brenland. Writes out/bank_years.csv (policy rate,
inflation, the rule's rate, net interest income at the actual and the rule's rate)
and out/bank_stats.csv."""
import pandas as pd
from bank import data, income_corridor, income_floor, overnight, rule
from figout import write_table


def tables():
    d = data()
    d["rule"] = d.infl.apply(rule)
    d["nii_actual"] = d.policy_rate.apply(income_floor)
    d["nii_rule"] = d.rule.apply(income_floor)
    i19 = d.loc[d.year == 2019, "policy_rate"].iloc[0]
    r22 = d[d.year == 2022].iloc[0]
    stats = pd.DataFrame({"stat": ["i_2019", "overnight_2019", "overnight_after_qe",
                                   "nii_2019_corridor", "rule_2022", "nii_2022_actual",
                                   "nii_2022_rule", "nii_2022_rule_pct_gdp",
                                   "overnight_supply_30"],
                          "value": [i19, overnight(i19, 40.0), overnight(i19, 80.0),
                                    income_corridor(i19), r22.rule, r22.nii_actual,
                                    r22.nii_rule, 100 * r22.nii_rule / (r22.gdp / 1000),
                                    overnight(i19, 30.0)]})
    return d[["year", "policy_rate", "infl", "rule", "nii_actual", "nii_rule"]], stats


if __name__ == "__main__":
    d, s = tables()
    write_table(d, __file__, "bank_years")
    write_table(s, __file__, "bank_stats")

"""Income and spending by age of the household's reference person, United States, 2023.

Reads src/bls_ce_age.csv, typed from the BLS Consumer Expenditure Surveys' published
Table 1300 for 2023 (ledger rows b2:bls-ce-age-*), and writes
  out/ce_age.csv   group, pos, age, income_after, spending, ratio,
                   income_pp, spending_pp
one row per age group. `spending` is average annual expenditures less "personal
insurance and pensions" (pension and Social Security contributions are saving, not
consumption), in thousands of dollars; `income_after` is income after taxes, in
thousands; `ratio` = spending / income_after; the _pp columns divide by the average
number of people in the consumer unit (thousands of dollars per person).
  out/ce_summary.csv  one row: peak_income_ratio (income after taxes, 45-54 over
                   under 25), peak_spending_ratio (the same for spending),
                   peak_pp_spending_ratio (spending per person, 55-64 over under 25).
Book 4, chapter 3, opening chart.
"""

import pandas as pd
from cited import load_cited
from figout import write_table


def table():
    d = load_cited(__file__, "bls_ce_age").drop(columns="ledger")
    spend = d.expenditures - d.insurance_pensions
    return pd.DataFrame(
        {
            "group": d.group,
            "pos": range(1, len(d) + 1),
            "age": d.age,
            "income_after": (d.income_after / 1000).round(3),
            "spending": (spend / 1000).round(3),
            "ratio": (spend / d.income_after).round(3),
            "income_pp": (d.income_after / d.people / 1000).round(2),
            "spending_pp": (spend / d.people / 1000).round(2),
        }
    )


def summary():
    t = table().set_index("group")
    return pd.DataFrame(
        [
            {
                "peak_income_ratio": round(
                    t.income_after["45-54"] / t.income_after["under 25"], 2
                ),
                "peak_spending_ratio": round(
                    t.spending["45-54"] / t.spending["under 25"], 2
                ),
                "peak_pp_spending_ratio": round(
                    t.spending_pp["55-64"] / t.spending_pp["under 25"], 2
                ),
            }
        ]
    )


if __name__ == "__main__":
    write_table(table(), __file__, "ce_age")
    write_table(summary(), __file__, "ce_summary")

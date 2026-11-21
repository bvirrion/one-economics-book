"""g7-07 Households: Income, Spending and Saving.

budget_shares.csv   group, food, housing, health, insurance: share of annual spending (percent) by fifth of US
                    households ranked by income before taxes, 2025 (BLS Consumer Expenditure Surveys, Table 1101)
income_sources.csv  group, wages, business, property, retirement, other: share of income before taxes (percent) by
                    source, same fifths; "other" is public assistance, unemployment and other benefits, other income
                    ("b/", under 0.05, counted as 0)
engel_points.csv    disp, share: Brenland's 2,000 households, disposable income (thousands of dalens) and food share of
                    disposable income (percent) (invented survey, code/shared/country)
engel_quarters.csv  disp, share: the same by quarter of disposable income (mean income; total food / total income)
problem_rows.csv    hh, size, gross, tax, transfers, disposable, food, consumption, saving: five households of the survey
facts.csv           name, value
"""
import pandas as pd

from country import load
from econdata import cex_table
from figout import write_table

GROUPS = ["Lowest", "Second", "Third", "Fourth", "Highest"]
PROBLEM_HH = [1, 2, 4, 6, 9]


def _cex():
    t = cex_table("mean-item-share-average-standard-error", 2025).fillna("")
    return t, t.iloc[:, 0].astype(str).str.strip()


def _row(label, which, start=0):
    """Mean (which=1) or share (which=2) of the five fifths for the first row named `label` after `start`."""
    t, lab = _cex()
    i = next(k for k in range(start, len(lab)) if lab[k] == label)
    vals = t.iloc[i + which, 2:7].tolist()
    return [0.0 if str(v).strip() == "b/" else float(v) for v in vals]


def _income_start():
    _, lab = _cex()
    return next(k for k in range(len(lab)) if lab[k] == "Sources of pretax income:")


def budget_shares():
    d = {"group": GROUPS}
    for col, lab in [("food", "Food"), ("housing", "Housing"), ("health", "Healthcare"),
                     ("insurance", "Personal insurance and pensions")]:
        d[col] = _row(lab, 2)
    return pd.DataFrame(d)


def income_sources():
    s = _income_start()
    d = {"group": GROUPS,
         "wages": _row("Wages and salaries", 2, s),
         "business": _row("Self-employment income", 2, s),
         "property": _row("Interest, dividends, rental income, and other property income", 2, s),
         "retirement": _row("Social Security, private and government retirement", 2, s)}
    other = [0.0] * 5
    for lab in ["Public assistance, Supplemental Security Income, Supplementary Nutrition Assistance Program (SNAP)",
                "Unemployment and workers' compensation, veterans' benefits, and regular contributions for support",
                "Other income"]:
        other = [a + b for a, b in zip(other, _row(lab, 2, s))]
    d["other"] = [round(x, 1) for x in other]
    return pd.DataFrame(d)


def _hh():
    h = load("households").copy()
    h["saving"] = h.disposable - h.consumption
    h["quarter"] = pd.qcut(h.disposable, 4, labels=[1, 2, 3, 4]).astype(int)
    return h


def engel_points():
    h = _hh()
    return pd.DataFrame({"disp": (h.disposable / 1000).round(2), "share": (100 * h.food / h.disposable).round(1)})


def engel_quarters():
    g = _hh().groupby("quarter")[["disposable", "food", "consumption", "saving"]].agg(["sum", "mean"])
    return pd.DataFrame({"quarter": g.index,
                         "disp": (g[("disposable", "mean")] / 1000).round(1).values,
                         "food": g[("food", "mean")].round(-1).astype(int).values,
                         "share": (100 * g[("food", "sum")] / g[("disposable", "sum")]).round(1).values,
                         "saving_rate": (100 * g[("saving", "sum")] / g[("disposable", "sum")]).round(1).values})


def problem_rows():
    h = _hh().set_index("hh").loc[PROBLEM_HH]
    return h.rename(columns={"gross_income": "gross"})[
        ["size", "gross", "tax", "transfers", "disposable", "food", "consumption", "saving"]].reset_index()


def facts():
    h = _hh()
    cuts = h.disposable.quantile([0.25, 0.5, 0.75]).round(-1)
    t, lab = _cex()
    rows = [("cex_units_thousands", float(t.iloc[3, 1])),
            ("cex_income_lowest", _row("Income before taxes", 1)[0]), ("cex_income_highest", _row("Income before taxes", 1)[4]),
            ("cex_spend_lowest", _row("Average annual expenditures", 1)[0]),
            ("cex_spend_highest", _row("Average annual expenditures", 1)[4]),
            ("cex_food_lowest", _row("Food", 1)[0]), ("cex_food_highest", _row("Food", 1)[4]),
            ("n_hh", len(h)),
            ("cut_q1", cuts[0.25]), ("cut_median", cuts[0.5]), ("cut_q3", cuts[0.75])]
    return pd.DataFrame(rows, columns=["name", "value"])


if __name__ == "__main__":
    write_table(budget_shares(), __file__, "budget_shares")
    write_table(income_sources(), __file__, "income_sources")
    write_table(engel_points(), __file__, "engel_points")
    write_table(engel_quarters(), __file__, "engel_quarters")
    write_table(problem_rows(), __file__, "problem_rows")
    write_table(facts(), __file__, "facts")

"""Chart 3: Maimonides' rule (cap of 40, ledger b3rd:al.rule) and simulated schools, the
same as the chapter's listing rd_fuzzy.py (seed 1999; 4,000 schools; 75 % follow the rule,
the rest a school target drawn between 28 and 38).
Writes out/rule.csv (enrol, rule) for enrolments 1-160 and out/schools.csv (enrol, size):
mean class size at each enrolment. Book 5, chapter 4, chart 3.
"""
import numpy as np
import pandas as pd
from figout import write_table


def rule(r):
    return r / ((r - 1) // 40 + 1)


def tables():
    rng = np.random.default_rng(1999)
    S = 4000
    enrol = rng.integers(15, 131, S)
    target = rng.uniform(28, 38, S)
    own = enrol / np.ceil(enrol / target)
    size = np.where(rng.uniform(size=S) < 0.75, rule(enrol), own)
    r = np.arange(1, 161)
    schools = (pd.DataFrame({"enrol": enrol, "size": size})
               .groupby("enrol", as_index=False)["size"].mean())
    return pd.DataFrame({"enrol": r, "rule": rule(r)}), schools


if __name__ == "__main__":
    a, b = tables()
    write_table(a, __file__, "rule")
    write_table(b, __file__, "schools")

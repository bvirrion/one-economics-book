"""Exercise 6: Brenland's CPI rebased to 2025 = 100, and its average log growth."""

import numpy as np
from country import load

cpi = load("accounts").set_index("year").cpi
rebased = (100 * cpi / cpi.loc[2025]).round(1)
growth = 100 * np.log(cpi).diff().loc[2016:2025].mean()

if __name__ == "__main__":
    print(rebased.loc[[2015, 2020, 2025]].to_string())
    print("mean log growth 2016-2025:", round(growth, 2))

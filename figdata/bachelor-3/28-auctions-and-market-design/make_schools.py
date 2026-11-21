"""Weekend problem: outcomes of deferred acceptance and of the old mechanism.
Writes out/schools.csv."""
import pandas as pd
from figout import write_table
from schools import PREFS, blocking_pairs, boston, deferred_acceptance

if __name__ == "__main__":
    da, _ = deferred_acceptance()
    bo = boston()
    write_table(pd.DataFrame({"pupil": list(PREFS),
                              "da": [da[i] for i in PREFS],
                              "boston": [bo[i] for i in PREFS]}),
                __file__, "schools")
    print(blocking_pairs(da), blocking_pairs(bo))

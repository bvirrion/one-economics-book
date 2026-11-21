"""Granger causality between money growth and inflation, US 1959-2009."""

import numpy as np
import pandas as pd
from econdata import sm_dataset
from statsmodels.tsa.stattools import grangercausalitytests

d = sm_dataset("macrodata")
m = 400 * np.diff(np.log(d.m1.to_numpy()))  # M1 growth, annualised
infl = d.infl.to_numpy()[1:]
data = pd.DataFrame({"infl": infl, "money": m})

for target, cause in (("infl", "money"), ("money", "infl")):
    res = grangercausalitytests(data[[target, cause]], maxlag=4)
    F, p = res[4][0]["ssr_ftest"][:2]
    print(f"does {cause} help predict {target}? F {F:.2f}, p-value {p:.3f}")

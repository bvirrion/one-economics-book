"""Monthly CPI series as a pandas Series indexed by (year, month)."""

import warnings

import pandas as pd
from econdata import bls_cpi

# the loader's file has a column of mixed types that we never use
warnings.filterwarnings("ignore", category=pd.errors.DtypeWarning)


def monthly(series_id="CUUR0000SA0", since=2014, until=2025):
    d = bls_cpi(series_id)
    d = d[
        d.period.str.match(r"M(0[1-9]|1[0-2])")
    ].copy()  # drop M13, the annual average
    d["month"] = d.period.str[1:].astype(int)
    d = d[(d.year >= since) & (d.year <= until)]
    return d.sort_values(["year", "month"]).set_index(["year", "month"]).value

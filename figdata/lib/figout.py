"""Write a chart table the way every figdata script does.

    from figout import write_table
    write_table(df, __file__, "world_gdppc")   # -> <chapter dir>/out/world_gdppc.csv

The table is a CSV with a header row (styles/oneeconomics.sty sets pgfplots to
read one), numbers with at most 6 significant digits, rows in the order given.
Columns used by pgfplots must be plain ASCII names without spaces.
A script must be deterministic: running it twice gives the same bytes
(tools/figdata.sh checks it).
"""
from __future__ import annotations

from pathlib import Path

import pandas as pd


def write_table(df: pd.DataFrame, script: str, name: str, float_format: str = "%.6g") -> Path:
    for c in df.columns:
        if not str(c).replace("_", "").isalnum() or not str(c).isascii():
            raise ValueError(f"column {c!r}: use ASCII letters, digits and _ only")
    out = Path(script).resolve().parent / "out"
    out.mkdir(exist_ok=True)
    p = out / f"{name}.csv"
    df.to_csv(p, index=False, float_format=float_format, lineterminator="\n")
    return p

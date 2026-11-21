"""Charts of b1 ch. 28.

cpi_mom: US CPI-U all items, month-on-month change (%), 2015-2024, not seasonally adjusted
(CUUR0000SA0), seasonally adjusted by BLS (CUSR0000SA0), and adjusted by hand with the
chapter's listing seasonal_by_hand.adjust (imported, so chart and listing cannot drift).
"""
import sys
from pathlib import Path

import pandas as pd
from figout import write_table

LST = Path(__file__).resolve().parents[3] / "code/bachelor-1/28-economic-data-python/listings"
sys.path.insert(0, str(LST))
from cpi_tools import monthly  # noqa: E402
from seasonal_by_hand import adjust  # noqa: E402

nsa = monthly("CUUR0000SA0")
sa = monthly("CUSR0000SA0")
factors, hand = adjust(nsa)
d = pd.DataFrame({"nsa": 100 * nsa.pct_change(), "sa": 100 * sa.pct_change(),
                  "hand": 100 * hand.pct_change()}).loc[2015:2024].round(3)
d = d.reset_index()
d["t"] = (d.year + (d.month - 0.5) / 12).round(3)
write_table(d[["t", "year", "month", "nsa", "sa", "hand"]], __file__, "cpi_mom")
st = {"n": len(d), "sd_nsa": round(d.nsa.std(), 3), "sd_sa": round(d.sa.std(), 3),
      "corr_hand": round(d.hand.corr(d.sa), 3)}
write_table(pd.DataFrame([st]), __file__, "cpi_stats")

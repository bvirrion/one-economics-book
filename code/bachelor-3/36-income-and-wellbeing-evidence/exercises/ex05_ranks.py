"""Exercise 5: rank countries by GDP per person and by consumption-equivalent welfare
(2019, relative to the United States) and print the five that rise most and the five
that fall most in the welfare ranking."""

import numpy as np
from welfare_data import countries, log_welfare

d = countries()
d["lw"] = log_welfare(d, 5.0)
d["rank_y"] = d.y.rank(ascending=False).astype(int)
d["rank_w"] = d.lw.rank(ascending=False).astype(int)
d["move"] = d.rank_y - d.rank_w
print(f"{len(d)} countries")
for label, rows in (("rise", d.nlargest(5, "move")), ("fall", d.nsmallest(5, "move"))):
    for r in rows.itertuples():
        print(
            f"{label} {r.country:22s} GDP rank {r.rank_y:3d}, "
            f"welfare rank {r.rank_w:3d}, "
            f"welfare {100 * np.exp(r.lw):5.1f} % of the U.S."
        )

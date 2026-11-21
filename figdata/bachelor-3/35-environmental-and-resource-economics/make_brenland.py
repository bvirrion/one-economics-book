"""Weekend problem: writes out/coal_price.csv (the Hotelling price path, 2025 to
exhaustion, then the backstop) and out/coal_stats.csv."""
import numpy as np
import pandas as pd
from coal import BACKSTOP, COST, R, hotelling, stats
from figout import write_table

if __name__ == "__main__":
    lam, T = hotelling()
    t = np.arange(0, 41)
    p = np.where(t <= T, COST + lam * np.exp(R * t), BACKSTOP)
    write_table(pd.DataFrame({"year": 2025 + t, "price": p}), __file__, "coal_price")
    st = stats()
    write_table(pd.DataFrame({"stat": list(st), "value": list(st.values())}),
                __file__, "coal_stats")

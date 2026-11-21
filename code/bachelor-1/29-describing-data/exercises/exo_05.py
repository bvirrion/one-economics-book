"""Exercise 5: skewness of earnings and of their log, for earnings of 5,000 or more."""

import numpy as np
from econdata import nsw
from scipy.stats import skew

earn = nsw("psid_controls").re78
x = earn[earn >= 5_000]
result = {"n": len(x), "skew": round(skew(x), 3), "skew_log": round(skew(np.log(x)), 3)}

if __name__ == "__main__":
    print(result)

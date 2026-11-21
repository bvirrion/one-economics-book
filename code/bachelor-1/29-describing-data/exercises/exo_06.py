"""Exercise 6: the CPS mean if the capped men earned 1.5 times the cap."""

from econdata import nsw

earn = nsw("cps_controls").re78
cap = earn.max()
alt = earn.where(earn < cap, 1.5 * cap)
result = {
    "recorded": round(earn.mean(), 0),
    "alt": round(alt.mean(), 0),
    "rise": round(100 * (alt.mean() / earn.mean() - 1), 1),
    "median_alt": round(alt.median(), 0),
}

if __name__ == "__main__":
    print(result)

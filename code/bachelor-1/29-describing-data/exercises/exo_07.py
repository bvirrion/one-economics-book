"""Exercise 7: mean earnings by schooling, and the step from 11 to 12 years."""

from econdata import nsw

d = nsw("psid_controls")
m = d.groupby("education").re78.mean()
step = round(m[12] - m[11], 0)

if __name__ == "__main__":
    print(m.loc[10:13].round(0).to_dict(), step)

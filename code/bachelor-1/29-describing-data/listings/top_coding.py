"""The CPS sample: earnings above a cap were recorded at the cap."""

from econdata import nsw

earn = nsw("cps_controls").re78
cap = earn.max()
at_cap = earn == cap
n_cap = at_cap.sum()
print(f"cap {cap:,.2f}; men at the cap {n_cap} of {len(earn)} ({at_cap.mean():.3f})")
print(f"mean as recorded       {earn.mean():10,.0f}")
print(f"mean without the capped {earn[~at_cap].mean():10,.0f}")
print(f"median                 {earn.median():10,.0f}")
print(
    "the true mean is at least", f"{earn.mean():,.0f}"
)  # capped values are lower bounds

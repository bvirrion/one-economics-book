"""A sharp regression discontinuity: does winning a close election raise the party's
vote share next time? Local linear fits at three windows, then a balance test."""
from elections import draw
from rdtools import local_linear

margin, share, past = draw()
near = abs(margin) < 0.05
print(f"elections {len(margin)}, within 0.05 of the cutoff {near.sum()}")
print("window   jump    s.e.   elections used")
for h in (0.05, 0.10, 0.25):
    r = local_linear(margin, share, cutoff=0, h=h)
    print(f"{h:5.2f}  {r['jump']:6.3f}  {r['se']:6.3f}  {r['n']:6d}")

means = share[near & (margin >= 0)].mean() - share[near & (margin < 0)].mean()
print(f"difference of means within 0.05: {means:.3f}")

r = local_linear(margin, past, cutoff=0, h=0.10)
print(f"balance: jump in the PAST vote share {r['jump']:6.3f} (s.e. {r['se']:.3f})")

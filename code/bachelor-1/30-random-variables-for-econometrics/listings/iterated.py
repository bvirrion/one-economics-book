"""The law of iterated expectations, checked on the PSID sample."""

from econdata import nsw

d = nsw("psid_controls")
cond = d.groupby("education").re78.mean()  # E[Y | X = x] for each x
weight = d.education.value_counts(normalize=True)  # P(X = x)
print(f"E[E[Y|X]] = {(cond * weight).sum():.6f}")
print(f"E[Y]      = {d.re78.mean():.6f}")

"""Brenland's survey: older and younger households, overall and by work."""

from country import load

h = load("households")
h["older"] = h.age_head >= 50  # head aged 50 or more
h["works"] = h.hours > 0
overall = h.groupby("older").disposable.mean().round(0)
print("overall:", overall.to_dict())
by_work = h.groupby(["works", "older"]).disposable.agg(["count", "mean"]).round(0)
print(by_work.to_string())
print("share working:", h.groupby("older").works.mean().round(3).to_dict())

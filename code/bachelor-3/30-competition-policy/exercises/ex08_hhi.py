"""Exercise 8: concentration screens for four invented mergers. For each market
(shares in percent) and merging pair, the script prints the HHI before and after,
the change, the merged share, and whether the 2023 U.S. guidelines' structural
presumption applies (post-merger HHI above 1,800 with a change above 100, or a merged
share above 30 % with a change above 100)."""

MARKETS = {
    "cement": ([30, 25, 20, 15, 10], (3, 4)),
    "flour": ([20, 20, 20, 20, 20], (0, 1)),
    "paint": ([12, 10, 8, 8, 6, 6, 50], (0, 1)),
    "glass": ([40, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5], (1, 2)),
}

for name, (shares, (i, j)) in MARKETS.items():
    before = sum(s * s for s in shares)
    merged = shares[i] + shares[j]
    after = before - shares[i] ** 2 - shares[j] ** 2 + merged ** 2
    change = after - before
    presumed = change > 100 and (after > 1800 or merged > 30)
    print(f"{name:7s} HHI {before:5d} -> {after:5d} (+{change:4d}), "
          f"merged share {merged:3d} %, presumed: {'yes' if presumed else 'no'}")

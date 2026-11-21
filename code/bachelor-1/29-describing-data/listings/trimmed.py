"""Mean, median and trimmed mean, with and without the largest earnings."""

from econdata import nsw
from scipy.stats import trim_mean

earn = nsw("nsw_dw").re78  # the 445 men of the experiment
top = earn.idxmax()
for name, x in [("all", earn), ("without the largest", earn.drop(top))]:
    print(
        f"{name:20s} n {len(x)}  mean {x.mean():7,.0f}  median {x.median():7,.0f}"
        f"  5% trimmed {trim_mean(x, 0.05):7,.0f}"
    )
print(f"largest {earn.max():,.0f}")

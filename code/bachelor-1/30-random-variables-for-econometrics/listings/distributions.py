"""Critical values the next chapters use (upper tails)."""

from scipy import stats

print("            5%      2.5%")
print(f"N(0,1)  {stats.norm.ppf(0.95):7.3f}  {stats.norm.ppf(0.975):7.3f}")
for k in (1, 5, 30):
    print(
        f"chi2({k:2d}) {stats.chi2.ppf(0.95, k):6.3f}  {stats.chi2.ppf(0.975, k):7.3f}"
    )
for k in (5, 30, 100):
    print(f"t({k:3d})  {stats.t.ppf(0.95, k):7.3f}  {stats.t.ppf(0.975, k):7.3f}")
for k, m in ((2, 30), (5, 100)):
    print(
        f"F({k},{m:3d}) {stats.f.ppf(0.95, k, m):6.3f}  {stats.f.ppf(0.975, k, m):7.3f}"
    )

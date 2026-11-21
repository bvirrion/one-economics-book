"""A results table: three nested regressions of 1978 earnings on the job-training offer,
in the experimental sample of chapter 3, printed by statsmodels' summary_col."""
import statsmodels.formula.api as smf
from econdata import nsw
from statsmodels.iolib.summary2 import summary_col

d = nsw("nsw_dw")
d["earn78"] = d.re78 / 1000                       # thousands of dollars
d["earn75"] = d.re75 / 1000
forms = ["earn78 ~ treat",
         "earn78 ~ treat + age + education + black + married",
         "earn78 ~ treat + age + education + black + married + earn75"]
fits = [smf.ols(f, d).fit(cov_type="HC1") for f in forms]
table = summary_col(fits, stars=True, float_format="%.3f",
                    model_names=["(1)", "(2)", "(3)"],
                    regressor_order=["treat", "earn75"], drop_omitted=True,
                    info_dict={"N": lambda r: f"{int(r.nobs)}"})
print(table.tables[0].to_string())

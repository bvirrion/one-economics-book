"""Chart 4 and the weekend problem: reserves, the shadow exchange rate and the
actual rate in the first-generation model with the problem's numbers. Writes
out/attack.csv and out/attack_stats.csv."""
import pandas as pd
from attack import C, D0, K, MU, S_BAR, attack_time, path
from figout import write_table


def stats():
    t_star = attack_time()
    r0 = K * S_BAR - D0
    return pd.DataFrame({"stat": ["r0", "t_attack", "t_exhaust", "r_at_attack",
                                  "money_before", "money_after", "dep_rate_after",
                                  "t_attack_mu6"],
                         "value": [r0, t_star, r0 / MU, C * MU / K, K * S_BAR,
                                   K * S_BAR - C * MU / K, 100 * MU / K / S_BAR,
                                   attack_time(mu=6.0)]})


if __name__ == "__main__":
    write_table(path(), __file__, "attack")
    write_table(stats(), __file__, "attack_stats")

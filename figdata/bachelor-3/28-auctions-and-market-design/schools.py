"""Brenmoor's school choice (weekend problem, Part IV). Four pupils, three schools.
Deferred acceptance (pupils propose) and the old priority mechanism, in which each
round's applications are accepted for good."""

PREFS = {"Ana": ["North", "South", "West"], "Ben": ["North", "West", "South"],
         "Cai": ["South", "North", "West"], "Dee": ["North", "South", "West"]}
PRIORITY = {"North": ["Cai", "Dee", "Ana", "Ben"],
            "South": ["Ana", "Dee", "Ben", "Cai"],
            "West": ["Ben", "Ana", "Cai", "Dee"]}
SEATS = {"North": 1, "South": 1, "West": 2}


def deferred_acceptance(prefs=PREFS, priority=PRIORITY, seats=SEATS):
    nxt = {i: 0 for i in prefs}
    held = {s: [] for s in seats}
    free, rounds = list(prefs), 0
    while free:
        rounds += 1
        for i in free:
            held[prefs[i][nxt[i]]].append(i)
            nxt[i] += 1
        free = []
        for s in held:
            held[s].sort(key=priority[s].index)
            free += held[s][seats[s]:]
            held[s] = held[s][:seats[s]]
    return {i: s for s in held for i in held[s]}, rounds


def boston(prefs=PREFS, priority=PRIORITY, seats=SEATS):
    left, match = dict(seats), {}
    for k in range(3):
        apps = {}
        for i in prefs:
            if i not in match:
                apps.setdefault(prefs[i][k], []).append(i)
        for s, a in apps.items():
            for i in sorted(a, key=priority[s].index)[:left[s]]:
                match[i] = s
                left[s] -= 1
    return match


def blocking_pairs(match, prefs=PREFS, priority=PRIORITY, seats=SEATS):
    out = []
    for i, ranking in prefs.items():
        for s in ranking[:ranking.index(match[i])]:
            there = [j for j in match if match[j] == s]
            if len(there) < seats[s] or any(
                    priority[s].index(i) < priority[s].index(j) for j in there):
                out.append((i, s))
    return out

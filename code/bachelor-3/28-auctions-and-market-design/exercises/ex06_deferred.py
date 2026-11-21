"""Exercise 6: deferred acceptance on an invented 4 x 4 market, one seat per school,
run with the pupils proposing and then with the schools proposing."""

PUPILS = {"p1": ["A", "B", "C", "D"], "p2": ["B", "A", "C", "D"],
          "p3": ["C", "A", "D", "B"], "p4": ["C", "D", "B", "A"]}
SCHOOLS = {"A": ["p2", "p1", "p3", "p4"], "B": ["p1", "p2", "p3", "p4"],
           "C": ["p4", "p3", "p1", "p2"], "D": ["p3", "p4", "p1", "p2"]}


def deferred_acceptance(proposers, receivers):
    nxt = {i: 0 for i in proposers}
    held, free = {}, list(proposers)
    while free:
        i = free.pop(0)
        r = proposers[i][nxt[i]]
        nxt[i] += 1
        if r not in held:
            held[r] = i
        elif receivers[r].index(i) < receivers[r].index(held[r]):
            free.append(held[r])
            held[r] = i
        else:
            free.append(i)
    return {i: r for r, i in held.items()}


pupils_propose = deferred_acceptance(PUPILS, SCHOOLS)
schools_propose = deferred_acceptance(SCHOOLS, PUPILS)
print("pupils propose:", dict(sorted(pupils_propose.items())))
print("schools propose:", dict(sorted((p, s) for s, p in schools_propose.items())))

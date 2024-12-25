from itertools import combinations

with open("inputs/2024/23.txt", "r") as f:
    content = f.read().split('\n')

computers, pt1, pt2 = dict(), 0, 0
for line in content:
    a, b = line.split('-')
    if a not in computers: computers[a] = set()
    if b not in computers: computers[b] = set()
    computers[a].add(b)
    computers[b].add(a)


def all_connected(_computers):
    for n, c in enumerate(_computers):
        for c2 in _computers[n + 1:]:
            if c2 not in computers[c]: return False
    return True


def build(start):
    so_far = set()
    so_far.add(start)
    queue = [start]
    checked = set()
    while queue:
        curr = queue.pop(0)
        checked.add(curr)
        for c in computers[curr]:
            if c in so_far: continue
            valid = True
            for c2 in so_far:
                if c2 not in computers[c]:
                    valid = False
                    break
            if not valid: continue
            so_far.add(c)

        for _c in computers[c]:
            if _c not in checked: queue.append(_c)
    return so_far


for combo in combinations(computers.keys(), 3):
    a, b, c = combo
    if not (a.startswith('t') or b.startswith('t') or c.startswith('t')): continue
    if all_connected(list([a, b, c])): pt1 += 1

pt2_longest = []
for i, computer in enumerate(computers.keys()):
    largest = build(computer)
    if len(largest) > len(pt2_longest): pt2_longest = largest

pt2_longest = list(pt2_longest)
pt2_longest.sort()

print('part 1', pt1)
print('part 2', ','.join(pt2_longest))

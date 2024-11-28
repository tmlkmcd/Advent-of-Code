import sys

crabs = []
part = 2

for line in sys.stdin:
    crabs = [int(n) for n in line.strip().split(',')]

min_possible = min(crabs) + 1
max_possible = max(crabs) - 1

best = -1

def triangular_number(n):
    return (n * (n + 1) // 2)

for n in range(min_possible, max_possible):
    tot = 0

    for c in crabs:
        if (part == 1): tot += abs(c - n)
        else: tot += triangular_number(abs(c - n))

    if best == -1 or tot < best: best = tot

print('part', part, ':', best)

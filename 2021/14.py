import sys
from collections import Counter

inp = [l.strip() for l in sys.stdin]
start = inp[0]
changes = {}

for a, b in [i.split(' -> ') for i in inp[2:]]: changes[a] = b

part = 1

def iterate(formula):
    n = ''
    for i, c in enumerate(formula):
        if i == 0: continue
        n += formula[i - 1] + changes[formula[i - 1:i + 1]]
    n += formula[-1]
    return n

m = start

for _ in range(10 if part == 1 else 40): m = iterate(m)

c = Counter(m)
print('part', part, max([c[b] for b in c]) - min([c[b] for b in c]))

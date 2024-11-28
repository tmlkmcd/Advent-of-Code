import sys
from collections import Counter

inp = [l.strip() for l in sys.stdin]
start = inp[0]
changes = {}
last_char = start[-1]

for a, b in [i.split(' -> ') for i in inp[2:]]: changes[a] = b

pair_frequencies = Counter()

for c in range(len(start)):
    if c == 0: continue
    pair_frequencies[start[c - 1:c + 1]] += 1

def calc(pf, part):
    c = Counter()
    for k in pf:
        c[k[0]] += pf[k]
    c[last_char] += 1
    print('part', part, max([c[b] for b in c]) - min([c[b] for b in c]))

for n in range(40):
    n_counter = Counter()

    for pair in pair_frequencies:
        insert = changes[pair]
        n_counter[pair[0] + insert] += pair_frequencies[pair]
        n_counter[insert + pair[1]] += pair_frequencies[pair]

    pair_frequencies = n_counter

    if n == 9 or n == 39:
        calc(pair_frequencies, 1 if n == 9 else 2)






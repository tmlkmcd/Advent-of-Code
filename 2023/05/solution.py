import sys
import math

lines_in = [line.strip() for line in sys.stdin]
seeds = [int(a) for a in lines_in[0].split(': ')[1].split(' ')]
maps = {}

def sort():
    global maps
    for m in maps: maps[m] = sorted(maps[m], key=lambda x: x[1])

current = ''

for line in lines_in[2:]:
    initial = line.split(' ')[0]
    if initial == '': continue
    if initial.isdigit():
        if current not in maps: maps[current] = []
        maps[current].append([int(d) for d in line.split(' ')])
        continue

    current = initial

sort()

def fetch(seed):
    # print('scanning', seed)
    current = seed
    for k in maps:
        if current < maps[k][0][1]: continue
        for _range in maps[k]:
            if _range[1] <= current < (_range[1] + _range[2]):
                current = _range[0] + (current - _range[1])
                break

    return current


# print('part 1', min([fetch(seed) for seed in seeds]))

seed_pairs = []
seeds_copy = [s for s in seeds]

for _ in seeds_copy:
    if len(seeds_copy) == 0: break
    seed_pairs.append([seeds_copy[0], seeds_copy[1]])
    seeds_copy = seeds_copy[2:]

def search_sp(seed_pair, skip=500000):
    start, length = seed_pair
    highest = start + length
    lowest = 1e12
    prev = -1

    current = start

    while current <= highest:
        v = fetch(current)
        lowest = min(v, lowest)

        if prev > -1 and v - prev != skip:
            for n in range(skip):
                lowest = min(fetch((current - skip) + 1 + n), lowest)

        n_next = current + skip
        if n_next > highest:
            while current <= highest:
                current += 1
                lowest = min(lowest, fetch(current))
            current += 1
        else:
            current = n_next
            prev = v

    return lowest





print(seed_pairs)
lowest = 1e12
for m, i in enumerate(seed_pairs):
    print('scanning seed pair', m + 1, 'out of', len(seed_pairs))
    v = search_sp(i)
    lowest = min(v, lowest)
    # break

print('part 2', lowest)

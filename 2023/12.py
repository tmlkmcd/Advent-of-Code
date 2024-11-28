import sys

lines_in = [line.strip() for line in sys.stdin]


def test(seen, a, b, block=0, i=0, block_i=0):
    k = (block, i, block_i)
    if k in seen: return seen[k]

    total = 0
    if i == len(a):
        if block_i == len(b) and block == 0: return 1
        if block_i == len(b) - 1 and b[block_i] == block: return 1
        return 0

    for c in ['.', '#']:
        if a[i] == c or a[i] == '?':
            if c == '.' and block == 0:
                total += test(seen, a, b, 0, i + 1, block_i)
            elif c == '.' and block > 0 and block_i < len(b) and b[block_i] == block:
                total += test(seen, a, b, 0, i + 1, block_i + 1)
            elif c == '#':
                total += test(seen, a, b, block + 1, i + 1, block_i)

    seen[k] = total
    return total


def calc(line, part=1):
    a, b = line.split(' ')
    list_a, b = list(a), [int(d) for d in b.split(',')]

    if part == 2:
        list_a = list('?'.join(a for _ in range(5)))
        b = b + b + b + b + b

    seen = {}
    return test(seen, list_a, b)


for part in [1, 2]:
    print('part {part}'.format(part=part), sum([calc(line, part) for line in lines_in]))

from math import pow

with open("inputs/2024/24.txt", "r") as f:
    content = f.read().split('\n\n')

wires = dict()
for line in content[0].split('\n'):
    w, val = line.split(': ')
    wires[w] = int(val)

for line in content[1].split('\n'):
    val, w = line.split(' -> ')
    wires[w] = val


def solve(wires, x=None, y=None, swaps=None):
    _wires = wires.copy()

    if x is not None:
        for _w in _wires:
            if _w.startswith('x'):
                _wires[_w] = (x >> int(_w[1:])) & 1

    if y is not None:
        for _w in _wires:
            if _w.startswith('y'):
                _wires[_w] = (y >> int(_w[1:])) & 1

    # x_wires = [w for w in _wires if w.startswith('x')]
    # x_wires.sort(key=lambda x: -1 * int(x[1:]))
    # values = [str(_wires[w]) for w in x_wires]
    # print(''.join(values), "{0:b}".format(x))
    # assert ''.join(values) == "{0:b}".format(x)

    if swaps is not None:
        for s in swaps:
            a, b = s
            _wires[a], _wires[b] = _wires[b], _wires[a]

    def get(wire):
        val = _wires[wire]
        if isinstance(val, int): return val
        a, op, b = val.split(' ')
        a, b = get(a), get(b)

        if op == 'AND':
            res = a & b
        elif op == 'OR':
            res = a | b
        else:
            res = a ^ b

        _wires[wire] = res
        return res

    for key in [k for k in _wires.keys() if k.startswith('z')]:
        get(key)

    z_wires = [w for w in _wires if w.startswith('z')]
    z_wires.sort(key=lambda x: -1 * int(x[1:]))
    values = [_wires[w] for w in z_wires]
    ans = 0
    for v in values:
        ans <<= 1
        ans += v
    return ans


def crawl(inp):
    global wires
    queue = [(inp, 0)]

    while queue:
        f, lv = queue.pop(0)
        _f = wires[f]
        p = "".join(["   " for _ in range(lv)])
        if isinstance(_f, int) or _f.startswith('z') or _f.startswith('x') or _f.startswith('y'):
            print(f'{f}: {p}{str(_f)}')
        else:
            print(f'{f}: {p}{_f}')
            a, _, b = _f.split(' ')
            if lv >= 5: continue
            queue.append((a, lv + 1))
            queue.append((b, lv + 1))


def swap(a, b):
    wires[a], wires[b] = wires[b], wires[a]


swap('z39', 'twr')
swap('z10', 'ggn')

swap('grm', 'z32')
swap('jcb', 'ndw')

crawl('z19')

for i, line in enumerate(content[1].split('\n')):
    a, op, b, _, targ = line.split(' ')
    if targ in ['z45', 'z39', 'twr', 'z10', 'ggn', 'jcb', 'ndw']: continue
    if targ.startswith('z'):
        if op != 'XOR':
            print(i, line)
    else:
        if (
                not ((a.startswith('x') or a.startswith('y')) and (
                        b.startswith('x') or b.startswith('y')))) and op == 'XOR':
            print(i, line)

res = solve(wires)
print('part 1', res)

for b in range(44):
    x, y = [int(pow(2, b)), int(pow(2, b))]
    _res = solve(wires, x, y)
    if _res != x + y:
        l = ["{0:b}".format(a) for a in [x, y, _res, x + y]]
        print(f'======vv {b} vv======')

        for a in l:
            print(' '.join([a.rjust(2) for a in list(a.rjust(44, "0"))]))
        print(' '.join([str(a + 1).rjust(2) for a in reversed(range(44))]))
        print(' ')

print('part 2', ','.join(sorted(['grm', 'z32', 'z39', 'twr', 'z10', 'ggn', 'jcb', 'ndw'])))

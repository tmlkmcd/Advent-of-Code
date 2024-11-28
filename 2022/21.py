import sys
from numbers import Number
from collections import defaultdict
lines_in = [line.strip() for line in sys.stdin]

def get_monkeys(humn=None):
    monkeys = defaultdict(None)
    for m in lines_in:
        name, num = m.split(': ')
        if humn is not None and name == 'humn': monkeys['humn'] = humn
        else:
            try: monkeys[name] = int(num)
            except: monkeys[name] = num.split(' ')
    return monkeys

def riddle(humn=None):
    monkeys = get_monkeys(humn)
    while isinstance(monkeys['root'], list):
        for m in monkeys:
            if isinstance(monkeys[m], Number): continue
            a, op, b = monkeys[m]
            if isinstance(monkeys[a], Number) and isinstance(monkeys[b], Number):
                if humn is not None and m == 'root': monkeys[m] = (monkeys[a], monkeys[b])
                elif op == '+': monkeys[m] = monkeys[a] + monkeys[b]
                elif op == '-': monkeys[m] = monkeys[a] - monkeys[b]
                elif op == '*': monkeys[m] = monkeys[a] * monkeys[b]
                elif op == '/': monkeys[m] = monkeys[a] / monkeys[b]
    return monkeys['root']

print('part 1:', int(riddle()))

low = 0
high = 1e15

while low < high:
    mid = int((low + high) // 2)
    a, b = riddle(humn=mid)
    if a > b: low = mid  # this needs to be reversed for the test input
    elif a < b: high = mid
    else:
        print('part 2:', mid)
        break

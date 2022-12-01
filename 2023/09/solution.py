import sys

lines_in = [line.strip() for line in sys.stdin]

def solve(history, part=1):
    values = [history]

    while True:
        series = values[len(values) - 1]
        next_series = [series[i] - series[i - 1] for i, n in enumerate(series) if i != 0]
        values.append(next_series)
        if all([a == 0 for a in next_series]): break

    target = 0
    for index in reversed(range(len(values))):
        if index == 0: return target
        if part == 1: target += values[index - 1][len(values[index - 1]) - 1]
        else: target = values[index - 1][0] - target


total, total2 = 0, 0
for line in lines_in:
    row = [int(a) for a in line.split(' ')]
    total += solve(row)
    total2 += solve(row, 2)

print('part 1', total)
print('part 2', total2)

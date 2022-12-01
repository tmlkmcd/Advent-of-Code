import sys
from collections import Counter

lines_in = [line.strip() for line in sys.stdin]
grid = dict()
part = 2

max_x, max_y, min_x, min_y = -1e9, -1e9, 1e9, 1e9
n_x, n_y = 0, 0

for line in lines_in:
    rock = [[int(a) for a in coord.split(',')] for coord in line.split(' -> ')]

    for n, (x, y) in enumerate(rock):
        max_x = max(x, max_x)
        max_y = max(y, max_y)
        min_x = min(x, min_x)
        min_y = min(y, min_y)

        if n < (len(rock) - 1):
            xx, yy = rock[n + 1]
            if x == xx:
                while y < yy:
                    grid[(y, x)] = '#'
                    y += 1
                while y > yy:
                    grid[(y, x)] = '#'
                    y -= 1
            if y == yy:
                while x < xx:
                    grid[(y, x)] = '#'
                    x += 1
                while x > xx:
                    grid[(y, x)] = '#'
                    x -= 1
        else:
            grid[(y, x)] = '#'

if part == 2:
    for _ in range(2000):
        grid[(max_y + 2, _ - 1000)] = '#'

full = False

while True:
    x_s, y_s = 500, 0
    moving_sand = True

    while moving_sand and not full:
        if (y_s + 1, x_s) not in grid:
            y_s += 1
            if y_s > max_y and part == 1:
                full = True
            continue

        if (y_s + 1, x_s - 1) not in grid:
            y_s += 1
            x_s -= 1
            continue

        if (y_s + 1, x_s + 1) not in grid:
            y_s += 1
            x_s += 1
            continue

        grid[(y_s, x_s)] = 'o'
        if part == 2 and y_s == 0 and x_s == 500:
            full = True
        moving_sand = False

    if full:
        break

print(f'part {part}', Counter(grid.values())['o'])

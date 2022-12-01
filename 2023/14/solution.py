import sys

lines_in = [line.strip() for line in sys.stdin]
grid = [list(line) for line in lines_in]
seen_grids = {}

def tilt(grid, direction='u'):
    grid_copy = [['.' if c == 'O' else c for c in row] for row in grid]
    if direction == 'u':
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell != 'O': continue
                for t in reversed(range(y + 1)):
                    if t == 0 or grid_copy[t - 1][x] == 'O' or grid_copy[t - 1][x] == '#':
                        grid_copy[t][x] = 'O'
                        break

    if direction == 'd':
        for y, row in enumerate(reversed(grid)):
            yy = len(grid) - y
            for x, cell in enumerate(row):
                if cell != 'O': continue
                for t in range(y + 1):
                    tt = yy + t - 1
                    if tt == len(grid) - 1 or grid_copy[tt + 1][x] == 'O' or grid_copy[tt+ 1][x] == '#':
                        grid_copy[tt][x] = 'O'
                        break

    if direction == 'l':
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell != 'O': continue
                for t in reversed(range(x + 1)):
                    if t == 0 or grid_copy[y][t - 1] in 'O#':
                        grid_copy[y][t] = 'O'
                        break

    if direction == 'r':
        for y, row in enumerate(grid):
            for x, cell in enumerate(reversed(row)):
                xx = len(grid[0]) - x
                if cell != 'O': continue
                for t in range(x + 1):
                    tt = xx + t - 1
                    if tt == len(grid[0]) - 1 or grid_copy[y][tt + 1] in 'O#':
                        grid_copy[y][tt] = 'O'
                        break

    return grid_copy

def calc(grid):
    l = len(grid)
    score = 0
    for y, row in enumerate(grid):
        score += (l - y) * len([a for a in row if a == 'O'])
    return score

def hash_grid(grid):
    m = ''
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == 'O':
                m += '{y},{x}|'.format(y=y, x=x)
    return m


g = tilt(grid, 'u')
print('part 1', calc(g))

steps, target_steps = 0, 1000000000
g, dropped = grid, False

while steps < target_steps:
    for d in 'uldr': g = tilt(g, d)
    steps += 1
    h = hash_grid(g)
    if not dropped and h in seen_grids:
        dropped = True
        target_steps = steps + ((target_steps - steps) % (steps - seen_grids[h]))
    seen_grids[h] = steps

print('part 2', calc(g))

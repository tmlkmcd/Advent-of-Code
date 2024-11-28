import sys
import math
import collections
import itertools

lines_in = [line.strip() for line in sys.stdin]
grid = [list(line) for line in lines_in]

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == 'S': s_y, s_x = y, x

steps, delta_steps = {(s_y, s_x): True}, [
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1)
]

def take_step():
    global grid, delta_steps, steps
    new_step = {}
    for y, x in steps:
        for dy, dx in delta_steps:
            yy, xx = y + dy, x + dx
            if grid[yy % len(grid)][xx % len(grid[0])] != '#':
                new_step[(yy, xx)] = True
    steps = new_step

num_steps = 0

for _ in range(25):
    for __ in range(65):
        take_step()
        num_steps += 1
    print('pt1', len([k for k in steps]), ': in {st} steps'.format(st=num_steps))



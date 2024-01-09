import sys
from collections import Counter

points = []
instructions = []
reading_instructions = False

part = 2

for line in sys.stdin:
    if len(line.strip()) == 0:
        reading_instructions = True
        continue

    if reading_instructions: instructions.append(line.strip())
    else: points.append(line.strip())

points_a = []

for p in points:
    points_a.append([int(a) for a in p.split(',')])

grid = []

def visualize():
    global grid
    for row in grid: print(' '.join(row))

def count():
    global grid
    total = 0
    for row in grid: total += Counter(row)['#']
    return total

max_x = -1
max_y = -1

for p in points_a:
    x = p[0]
    y = p[1]

    if x >= max_x: max_x = x + 1
    if y >= max_y: max_y = y + 1

for y in range(max_y):
    grid.append(['.' for _ in range(max_x)])

for p in points_a:
    x = p[0]
    y = p[1]
    grid[y][x] = '#'

def fold(instruction):
    global grid
    _, __, axis = instruction.split(' ')
    direction, magnitude = axis.split('=')
    magnitude = int(magnitude)

    if direction == 'y':
        for y, row in enumerate(grid[magnitude + 1:]):
            for x, cell in enumerate(row):
                if cell == '.': continue
                grid[magnitude - (y + 1)][x] = '#'

        grid = grid[:magnitude]
    else:
        for y, row in enumerate(grid):
            for x, cell in enumerate(row[magnitude + 1:]):
                if cell == '.': continue
                grid[y][magnitude - (x + 1)] = '#'
        grid = [row[:magnitude] for row in grid]

if part == 1:
    fold(instructions[0])
    print(count())
else:
    for inst in instructions:
        fold(inst)
    visualize()

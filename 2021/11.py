import sys

dumbo = []

for line in sys.stdin:
    dumbo.append([int(i) for i in line.strip()])

xx = len(dumbo[0])
yy = len(dumbo)

part = 2

def visualize(dumbo_grid):
    print('================')
    for row in dumbo_grid:
        print(''.join([str(i) for i in row]))
    print('================')

def flash(y, x, grid, flashes=0):
    grid[y][x] = 'f'
    flashes += 1
    new_coords = [
        [y, x - 1],
        [y, x + 1],
        [y - 1, x],
        [y + 1, x],
        [y - 1, x - 1],
        [y + 1, x - 1],
        [y - 1, x + 1],
        [y + 1, x + 1]
    ]

    for yn, xn in new_coords:
        try:
            if yn < 0 or xn < 0: continue
            if grid[yn][xn] == 'f': continue
        except:
            continue

        grid[yn][xn] = grid[yn][xn] + 1

        if grid[yn][xn] >= 10:
            n_grid, n_flashes = flash(yn, xn, grid, flashes)

            grid = n_grid
            flashes = n_flashes

    return grid, flashes


def iterate():
    global dumbo
    new_dumbo = []
    flashes = 0

    for row in dumbo:
        new_dumbo.append([i for i in row])

    for x in range(xx):
        for y in range(yy):
            if new_dumbo[y][x] != 'f':
                new_dumbo[y][x] = new_dumbo[y][x] + 1

    for x in range(xx):
        for y in range(yy):
            if new_dumbo[y][x] == 'f': continue
            if new_dumbo[y][x] >= 10:
                grid, n_flashes = flash(y, x, new_dumbo)
                new_dumbo = grid
                flashes += n_flashes

    for x in range(xx):
        for y in range(yy):
            if new_dumbo[y][x] == 'f':
                new_dumbo[y][x] = 0

    dumbo = new_dumbo
    return flashes

total = 0

def all_flash(grid):
    for r in grid:
        if len([i for i in r if i > 0]) > 0:
            return False
    return True

if part == 1:
    for i in range(100):
        total += iterate()
    print(total)

else:
    steps = 0
    while True:
        steps += 1
        iterate()
        if all_flash(dumbo):
            print('part 2', steps)
            break






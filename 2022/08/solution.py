import sys
import itertools

lines_in = [line.strip() for line in sys.stdin]
grid = [[int(a) for a in list(line)] for line in lines_in]

visible = dict()


def scan_edge(from_corner='topleft'):
    global grid, visible
    for x in range(len(grid)):
        highest = -1
        for y in range(len(grid)) if from_corner == 'topleft' else reversed(range(len(grid))):
            if grid[y][x] > highest:
                visible[f"{x},{y}"] = True
                highest = grid[y][x]
                if highest == 9: break
    for y in range(len(grid)):
        highest = -1
        for x in range(len(grid)) if from_corner == 'topleft' else reversed(range(len(grid))):
            if grid[y][x] > highest:
                visible[f"{x},{y}"] = True
                highest = grid[y][x]
                if highest == 9: break

scan_edge()
scan_edge(from_corner='bottomright')
print('part 1', len(visible.values()))

def scan(coords):
    global grid
    y, x = coords
    x1, x2, y1, y2 = 0, 0, 0, 0
    max_height = grid[y][x]

    _x = x - 1
    while _x >= 0:
        x1 += 1
        if grid[y][_x] >= max_height: break
        _x -= 1

    x_ = x + 1
    while x_ < len(grid):
        x2 += 1
        if grid[y][x_] >= max_height: break
        x_ += 1

    _y = y - 1
    while _y >= 0:
        y1 += 1
        if grid[_y][x] >= max_height: break
        _y -= 1

    y_ = y + 1
    while y_ < len(grid):
        y2 += 1
        if grid[y_][x] >= max_height: break
        y_ += 1

    return x1 * x2 * y1 * y2

pt2 = -1

for c in itertools.product(range(len(grid)), repeat=2):
    pt2 = max(pt2, scan(c))

print('part 2', pt2)

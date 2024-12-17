with open("inputs/2024/12.txt", "r") as f:
    content = f.read().split('\n')

grid = [[a for a in list(row)] for row in content]
g_length, g_height = len(grid[0]), len(grid)
explored = dict()
perimeters = dict()


def in_bounds(y, x):
    return 0 <= y < g_height and 0 <= x < g_length


def scan(y, x, explored_key=None, region=None):
    global explored, perimeters

    coord = (y, x)
    if region is not None and coord in region: return
    for key in explored:
        if coord in explored[key]: return

    if region is None:
        explored_key = grid[y][x]
        while explored_key in explored:
            explored_key += '-'
        region = set()
        explored[explored_key] = region
        perimeters[explored_key] = []

    region.add(coord)

    for n, (dy, dx) in enumerate([(1, 0), (-1, 0), (0, 1), (0, -1)]):
        yy, xx = y + dy, x + dx
        if in_bounds(yy, xx) and grid[yy][xx] == grid[y][x]:
            scan(yy, xx, explored_key, region)
        else:
            direction = ''
            if n == 0: direction = 'd'
            if n == 1: direction = 'u'
            if n == 2: direction = 'r'
            if n == 3: direction = 'l'
            perimeters[explored_key] += [(y, x, direction)]


def perimeter_to_sides(perimeters):
    sides = set()
    checked = set()
    for section in perimeters:
        if section in checked: continue
        sides.add(section)
        y, x, direction = section

        checked.add(section)
        if direction == 'u' or direction == 'd':
            for n in [-1, 1]:
                yy, xx = y, x
                while in_bounds(yy, xx) and grid[yy][xx] == grid[y][x] and (yy, xx, direction) in perimeters:
                    checked.add((yy, xx, direction))
                    xx += n

        if direction == 'l' or direction == 'r':
            for n in [-1, 1]:
                yy, xx = y, x
                while in_bounds(yy, xx) and grid[yy][xx] == grid[y][x] and (yy, xx, direction) in perimeters:
                    checked.add((yy, xx, direction))
                    yy += n
    return sides


for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        scan(y, x)

pt1, pt2 = 0, 0

for key in explored:
    pt1 += len(explored[key]) * len(perimeters[key])
    pt2 += len(explored[key]) * len(perimeter_to_sides(perimeters[key]))

print('part 1', pt1)
print('part 2', pt2)

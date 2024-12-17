with open("inputs/2024/16.txt", "r") as f:
    content = f.read().split('\n')

grid = [[cell for cell in row] for row in content]
start, end, pt2_nodes = None, None, set()
fastest = None
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == 'S':
            start = (y, x)
        elif cell == 'E':
            end = (y, x)

directions = {
    'r': (0, 1),
    'l': (0, -1),
    'u': (-1, 0),
    'd': (1, 0)
}


def opposite(d):
    if d == 'r': return 'l'
    if d == 'l': return 'r'
    if d == 'u': return 'd'
    if d == 'd': return 'u'


def get_options(y, x, d):
    for direction in directions:
        if direction == opposite(d): continue
        dy, dx = directions[direction]

        if grid[y + dy][x + dx] != '#':
            if direction == d: yield 1, y + dy, x + dx, d
            yield 1000, y, x, direction


def find_fastest():
    global grid, start, end, directions, pt2_routes, fastest
    explored = dict()
    explored[(start[0], start[1], 'r')] = 0
    queue = [(start[0], start[1], 0, 'r', 0, [(start[0], start[1], 'r')])]

    while queue:
        y, x, score, d, nn, route = queue.pop(0)
        explored[(y, x, d)] = score

        if (y, x) == end:
            if fastest is None:
                for (y, x, d) in route: pt2_nodes.add((y, x))
                fastest = score
            elif score == fastest:
                for (y, x, d) in route: pt2_nodes.add((y, x))
            continue

        for option in get_options(y, x, d):
            n_score, ny, nx, nd = option
            if (ny, nx, nd) not in explored:
                _route = [r for r in route]
                _route.append((ny, nx, nd))
                queue.append((ny, nx, score + n_score, nd, nn + 1, _route))

        queue.sort(key=lambda x: x[2])


find_fastest()

for y, row in enumerate(grid):
    print(''.join([cell if (y, x) not in pt2_nodes else 'O' for x, cell in enumerate(row)]))
print('part 1', fastest)
print('part 2', len(pt2_nodes))

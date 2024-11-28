# https://stackabuse.com/dijkstras-algorithm-in-python/
# HOLY SH!T
# solution is slow

import sys

grid = []
tmp_grid = []

for line in sys.stdin: tmp_grid.append([int(i) for i in line.strip()])

def pt2_grid_increment(grid, n):
    n_tmp_grid = []
    for row in tmp_grid:
        n_tmp_grid.append([((i + n) % 9) if ((i + n) % 9) > 0 else 9 for i in row])
    return n_tmp_grid

for y_ in range(5):
    for _ in range(len(tmp_grid)):
        grid.append([])
    for x_ in range(5):
        n = x_ + y_
        to_add = pt2_grid_increment(tmp_grid, n)

        for i, row in enumerate(to_add):
            grid[(len(tmp_grid) * y_) + i] += row

xx = len(grid[0])
yy = len(grid)

points = []
for r in grid: points.append([None for _ in r])

visited = []
for r in grid: visited.append([False for _ in r])

to_visit = {}

def by_val(k):
    global to_visit
    return to_visit[k]

def get_next():
    global to_visit
    return min(to_visit.keys(), key=by_val)

def scan(point):
    global points_checked
    global visited
    global points

    while True:
        x, y = point
        visited[y][x] = True

        try: del to_visit[(x, y)]
        except: pass

        neighbours = []

        if x > 0: neighbours.append((x - 1, y))
        if x < xx - 1: neighbours.append((x + 1, y))

        if y > 0: neighbours.append((x, y - 1))
        if y < yy - 1: neighbours.append((x, y + 1))

        for n in neighbours:
            _x, _y = n
            if visited[_y][_x] is True: continue

            n_points = points[y][x] + grid[_y][_x]

            if points[_y][_x] is None: points[_y][_x] = n_points
            elif points[_y][_x] > n_points: points[_y][_x] = n_points

            to_visit[(_x, _y)] = points[_y][_x]

        try: point = get_next()
        except: return points[yy - 1][xx - 1]

points[0][0] = 0
print(scan((0, 0)))



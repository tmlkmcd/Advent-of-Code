with open("inputs/2024/06.txt", "r") as f:
    content = f.read().split('\n')

grid, start = [list(row) for row in content], None
pt1_visited, pt2 = set(), 0

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == '^':
            start = (y, x)
            break
    if start is not None: break


def loop(_grid, part=1):
    global pt2
    visited = set()
    visited.add(start)
    current, direction = start, 0

    while True:
        y, x = current
        dy, dx = [(-1, 0), (0, 1), (1, 0), (0, -1)][direction]

        if (y, x, direction) in visited:
            pt2 += 1
            break

        if 0 <= y + dy < len(_grid) and 0 <= x + dx < len(_grid[0]):
            if _grid[y + dy][x + dx] != '#':
                current = (y + dy, x + dx)
                if part == 1:
                    visited.add(current)
                else:
                    visited.add((y, x, direction))
                continue
            else:
                direction = (direction + 1) % 4
        else:
            break

    if part == 1:
        global pt1_visited
        pt1_visited = visited

    return len(visited)


print('part 1:', loop(grid))

for y, x in pt1_visited:
    cell = grid[y][x]
    if cell == '#': continue

    n_grid = [[cell for cell in row] for row in grid]
    n_grid[y][x] = '#'
    loop(n_grid, 2)

print('part 2:', pt2)

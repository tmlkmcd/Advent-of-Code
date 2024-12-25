with open("inputs/2024/20.txt", "r") as f:
    content = f.read().split('\n')

grid = [[a for a in line] for line in content]
start, end = None, None

for y in range(len(grid)):
    for x in range(len(grid[y])):
        if grid[y][x] == 'S':
            start = (y, x)
            grid[y][x] = '.'
        elif grid[y][x] == 'E':
            end = (y, x)
            grid[y][x] = '.'


def get_choices(current, _grid):
    y, x = current
    for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        yy, xx = y + dy, x + dx
        if not (len(_grid) > yy >= 0 and len(_grid[0]) > xx >= 0): continue
        if _grid[yy][xx] != '#':
            yield yy, xx


def solve():
    _grid, queue = [row.copy() for row in grid], [(start, [])]
    visited = dict()
    while queue:
        a, path = queue.pop(0)
        y, x = a
        if (y, x) in visited: continue
        n_path = path + [(y, x)]
        visited[(y, x)] = n_path
        if (y, x) == end: return n_path
        for choice in get_choices((y, x), _grid):
            queue.append((choice, n_path))


def can_cheat_2(y, x, d=2):
    for dy in range(-1 * d, d + 1):
        for dx in range(-1 * d, d + 1):
            yy, xx = y + dy, x + dx
            if not (
                    len(grid) > yy >= 0
                    and len(grid[0]) > xx >= 0
            ): continue
            if yy == y and xx == x: continue
            man_distance = abs(dy) + abs(dx)
            if man_distance > d: continue
            if grid[yy][xx] != '.': continue
            yield (yy, xx), man_distance


path, indeces, ans, ans_2 = solve(), dict(), 0, 0
for n, p in enumerate(path): indeces[p] = n

for y, row in enumerate(grid):
    # print(f'progress: {y}/{len(grid)}')
    for x, cell in enumerate(row):
        if cell != '#':

            a = indeces[(y, x)]
            cc = can_cheat_2(y, x)
            for ex, d in cc:
                b = indeces[ex]
                if b < a: continue
                saving = (b - a) - d
                if saving >= 100: ans += 1

            cc2 = can_cheat_2(y, x, 20)
            for ex_2, d_2 in cc2:
                b2 = indeces[ex_2]
                if b2 < a: continue
                saving_2 = (b2 - a) - d_2
                if saving_2 >= 100: ans_2 += 1

print('part 1', ans)
print('part 2', ans_2)

import sys

lines_in = [line.strip() for line in sys.stdin]
grid = [list(line) for line in lines_in]
max_y, max_x = len(grid), len(grid[0])

def solve(part=1):
    global grid
    # a million times larger, OR 1 + 999999
    expansion = 1 if part == 1 else 999999
    galaxies, g_list, total = {}, [], 0
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == '#':
                k = str(y) + ',' + str(x)
                galaxies[k] = {
                    'coord': (y, x),
                    'x-nudge': 0,
                    'y-nudge': 0
                }

    for y in reversed(range(max_y)):
        if all([a == '.' for a in grid[y]]):
            for g in galaxies:
                if galaxies[g]['coord'][0] > y:
                    galaxies[g]['y-nudge'] += expansion

    for x in reversed(range(max_x)):
        if all([row[x] == '.' for row in grid]):
            for g in galaxies:
                if galaxies[g]['coord'][1] > x:
                    galaxies[g]['x-nudge'] += expansion

    for g in galaxies:
        gg = galaxies[g]
        yy, xx = gg['coord']
        if gg['y-nudge'] > 0: yy += gg['y-nudge']
        if gg['x-nudge'] > 0: xx += gg['x-nudge']
        g_list.append((yy, xx))

    for i, g in enumerate(g_list):
        for j, gg in enumerate(g_list):
            if j <= i: continue
            y, x = g
            yy, xx = gg
            total += abs(yy - y) + abs(xx - x)

    return total

for part in [1, 2]:
    print('part {p}:'.format(p=part), solve(part))


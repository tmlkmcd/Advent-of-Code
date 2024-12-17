with open("inputs/2024/10-test2.txt", "r") as f:
    content = f.read().split('\n')

grid = [[int(a) if a != '.' else 1 for a in list(row)] for row in content]
g_length, g_height = len(grid[0]), len(grid)


def crawl(start, peaks, paths, path=None, height=0):
    global grid

    if path == None: path = []
    path.append(start)

    if height == 9:
        peaks.add(start)
        paths.add(tuple(path))
        return

    for dy, dx in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        yy, xx = start
        yy += dy
        xx += dx
        if 0 <= yy < g_height and 0 <= xx < g_length and grid[yy][xx] == height + 1:
            crawl((yy, xx), peaks, paths, path, height + 1)


pt1, pt2 = 0, 0
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == 0:
            peaks, paths = set(), set()
            crawl((y, x), peaks, paths)
            pt1 += len(peaks)
            pt2 += len(paths)

print('part 1', pt1)
print('part 2', pt2)

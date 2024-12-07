with open("inputs/2024/04.txt", "r") as f:
    content = f.read()


def scan(y, x):
    count = 0
    deltas = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]

    for dy, dx in deltas:
        yy, xx = y, x
        good = True
        for char in 'XMAS':
            if (yy < 0 or yy >= height or xx < 0 or xx >= length) or (grid[yy][xx] != char):
                good = False
                break

            yy += dy
            xx += dx

        if good:
            count += 1

    return count


def scan_2(y, x):
    if y < 1 or y >= height - 1 or x < 1 or x >= length - 1:
        return False

    tl = grid[y - 1][x - 1]
    tr = grid[y - 1][x + 1]
    bl = grid[y + 1][x - 1]
    br = grid[y + 1][x + 1]

    return (
            (tl == 'M' and br == 'S') or (tl == 'S' and br == 'M')
    ) and (
            (tr == 'M' and bl == 'S') or (tr == 'S' and bl == 'M')
    )


grid = content.split('\n')
length, height = len(grid[0]), len(grid)

pt1, pt2 = 0, 0
for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell == 'X':
            pt1 += scan(y, x)
        elif cell == 'A':
            pt2 += 1 if scan_2(y, x) else 0

print('part 1', pt1)
print('part 2', pt2)

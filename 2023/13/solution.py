import sys

lines_in = [line.strip() for line in sys.stdin]
class Mirror:
    def __init__(self, grid, vert_line=-1, hori_line=-1):
        self.grid = [list(line) for line in grid]
        self.size_x = len(grid[0])
        self.size_y = len(grid)
        self.vert_line = vert_line
        self.hori_line = hori_line

    def test_vert(self, part=1):
        for try_y in range(self.size_y):
            if try_y == 0: continue
            could_be = True

            for dy in range(min(try_y, self.size_y - try_y)):
                for x in range(self.size_x):
                    if self.grid[try_y - (dy + 1)][x] != self.grid[try_y + dy][x]:
                        could_be = False
                        break
                if not could_be: break
            if could_be:
                if part == 1:
                    self.vert_line = try_y
                    return try_y
                else:
                    if try_y != self.vert_line:
                        return try_y
        return -1

    def test_hori(self, part=1):
        for try_x in range(self.size_x):
            if try_x == 0: continue
            could_be = True

            for dx in range(min(try_x, self.size_x - try_x)):
                for y in range(self.size_y):
                    if self.grid[y][try_x - (dx + 1)] != self.grid[y][try_x + dx]:
                        could_be = False
                        break
                if not could_be: break
            if could_be:
                if part == 1:
                    self.hori_line = try_x
                    return try_x
                else:
                    if try_x != self.hori_line:
                        return try_x
        return -1

    def smudge(self, y, x):
        grid_copy = [[c for c in row] for row in self.grid]
        grid_copy[y][x] = '.' if grid_copy[y][x] == '#' else '#'
        return Mirror([''.join(row) for row in grid_copy], self.vert_line, self.hori_line)

    def test_smudges(self):
        for y in range(self.size_y):
            for x in range(self.size_x):
                nm = self.smudge(y, x)
                hori_2, vert_2 = nm.test_hori(2), nm.test_vert(2)
                if vert_2 > -1 or hori_2 > -1:
                    return (hori_2 if hori_2 > -1 else 0) + (vert_2 * 100 if vert_2 > -1 else 0)

mirrors, current_mirror = [], []
for line in lines_in:
    if line == '':
        mirrors.append(Mirror(current_mirror))
        current_mirror = []
        continue
    current_mirror.append(line)

if len(current_mirror) > 0:
    mirrors.append(Mirror(current_mirror))
    current_mirror = []

total, total2 = 0, 0
for m in mirrors:
    vert, hori = m.test_vert(), m.test_hori()
    total += (hori if hori > -1 else 0) + (vert * 100 if vert > -1 else 0)
    total2 += m.test_smudges()

print('part 1', total)
print('part 2', total2)

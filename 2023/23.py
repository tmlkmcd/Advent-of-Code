import sys

lines_in = [line.strip() for line in sys.stdin]
grid = [list(line) for line in lines_in]
steps = { 'r': (0, 1), 'l': (0, -1), 'u': (-1, 0), 'd': (1, 0) }
max_path, waiting, junctions = -1, {}, {}

class Path:
    def __init__(self, current=(1, 1), path=frozenset({(0, 1), (1, 1)})):
        self.current = current
        self.path = path.copy()

    def __eq__(self, other):
        if len(self.path) != len(other.path): return False
        return self.current == other.current and self.path == other.path

    def __hash__(self):
        return hash(self.current) ^ hash(self.path)

    def get_len(self):
        return len(self.path)

    def clone_with(self, coord):
        return Path(coord, frozenset(self.path) | {coord})



seen = set()

def solve_1(path):
    global max_path, waiting
    if path in seen: return
    y, x = path.current

    valid = 0

    for c in 'uldr':
        dy, dx = steps[c]
        yy, xx = y + dy, x + dx
        if (yy, xx) in path.path: continue
        if yy == 125 and xx == 133 and c != 'd': continue
        if yy == len(grid):
            asdasd = len(path.path) - 1
            max_path = max(max_path, asdasd)
            print('max: {m} ({f}), waiting: {w}/{s}'.format(m=max_path, f=asdasd, w=len(waiting), s=len(seen)))
            continue

        if grid[yy][xx] == '#': continue

        # if grid[yy][xx] == '^' and c != 'u': continue
        # if grid[yy][xx] == '<' and c != 'l': continue
        # if grid[yy][xx] == 'v' and c != 'd': continue
        # if grid[yy][xx] == '>' and c != 'r': continue

        new_path = path.clone_with((yy, xx))

        if new_path in waiting: continue

        waiting.add(new_path)
        valid += 1
    if valid >= 2:
        seen.add(path)



# find_junctions()
# print(junctions)
#

waiting = {Path()}

while len(waiting) > 0:
    p = waiting.pop()
    solve_1(p)

print(max_path)
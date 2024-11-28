import sys
from collections import deque

grid = [list(line.strip()) for line in sys.stdin]
start = (0, grid[0].index('.'))
end = (len(grid) - 1, grid[len(grid) - 1].index('.'))
grid_height, grid_width = len(grid) - 2, len(grid[0]) - 2
blizzards = []

class Blizzard:
    def __init__(self, y, x, icon):
        self.y = y
        self.x = x
        self.const_x = None
        self.const_y = None
        match icon:
            case '^':
                self.const_x = x
                self.find = self.find_up
            case '>':
                self.const_y = y
                self.find = self.find_right
            case 'v':
                self.const_x = x
                self.find = self.find_down
            case '<':
                self.const_y = y
                self.find = self.find_left

    def find_up(self, t): return (((self.y - 1) - t) % grid_height) + 1
    def find_right(self, t): return (((self.x - 1) + t) % grid_width) + 1
    def find_down(self, t): return (((self.y - 1) + t) % grid_height) + 1
    def find_left(self, t): return (((self.x - 1) - t) % grid_width) + 1

    def is_on_spot_at_time(self, t, spot):
        yy, xx = spot
        if self.const_x is not None: return self.find(t) == yy if self.const_x == xx else False
        if self.const_y is not None: return self.find(t) == xx if self.const_y == yy else False

for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell in ['^', '<', '>', 'v']: blizzards.append(Blizzard(y, x, cell))

def move(start, end, time):
    P = set()  # previous
    S = deque([(time, start[0], start[1])])  # state

    while S:
        t, y, x = S.popleft()
        if (y, x) == end: return t
        tt = t + 1
        for dy, dx in [(1, 0), (0, 1), (0, 0), (0, -1), (-1, 0)]:
            yy = y + dy
            xx = x + dx
            if (tt, yy, xx) in P: continue
            P.add((tt, yy, xx))
            if not 0 <= yy <= (len(grid) - 1): continue
            if grid[yy][xx] == '#': continue
            bad = False
            for b in blizzards:
                if b.is_on_spot_at_time(tt, (yy, xx)):
                    bad = True
                    break
            if bad: continue
            S.append((tt, yy, xx))

t = move(start, end, 0)
print('part 1', t)
t = move(end, start, t)
t = move(start, end, t)
print('part 2', t)

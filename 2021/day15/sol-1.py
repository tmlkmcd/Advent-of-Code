import sys

part = 1

grid = []
for line in sys.stdin: grid.append([int(i) for i in line.strip()])
xx = len(grid[0])
yy = len(grid)

paths = {}

fastest_to = {}

class Path:
    def __init__(self, path):
        self.path = path
        self.score = None

        location = path[-1]
        x, y = location

        if x < 0 or x >= xx or y < 0 or y >= yy: return

        if location not in fastest_to or self.get_score() < fastest_to[location].get_score():
            fastest_to[location] = self
            self.scan()

    def get_score(self):
        if self.score is None:
            s = 0
            for p in self.path:
                x, y = p
                s += grid[y][x]

            self.score = s - grid[0][0]

        return self.score

    def scan(self):
        x, y = self.path[-1]

        Path(self.path + [(x + 1, y)])
        Path(self.path + [(x, y + 1)])

Path([(0, 0)])

print(fastest_to[(xx - 1, yy - 1)].get_score())






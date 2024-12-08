from itertools import combinations

with open("inputs/2024/08.txt", "r") as f:
    content = f.read().split('\n')

grid, nodes, antinodes_1, antinodes_2 = [list(row) for row in content], dict(), dict(), dict()
length, height = len(grid[0]), len(grid)


def within_bounds(y, x): return 0 <= y < height and 0 <= x < length


for y, row in enumerate(grid):
    for x, cell in enumerate(row):
        if cell != '.':
            if cell not in nodes: nodes[cell] = []
            nodes[cell].append((y, x))

for node, positions in nodes.items():
    for a in combinations(positions, 2):
        y1, x1 = a[1]
        y2, x2 = a[0]
        dy, dx = y2 - y1, x2 - x1

        an1, an2 = (y1 - dy, x1 - dx), (y2 + dy, x2 + dx)

        if within_bounds(*an1): antinodes_1[an1] = node
        if within_bounds(*an2): antinodes_1[an2] = node

        antinodes_2[a[0]] = node
        antinodes_2[a[1]] = node

        while within_bounds(*an1):
            antinodes_2[an1] = node
            an1 = (an1[0] - dy, an1[1] - dx)

        while within_bounds(*an2):
            antinodes_2[an2] = node
            an2 = (an2[0] + dy, an2[1] + dx)

print('part 1', len(antinodes_1.items()))
print('part 2', len(antinodes_2.items()))

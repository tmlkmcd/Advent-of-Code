serial = 7511
grid = []


def calc(x, y, serial):
    rack = x + 10
    power = ((rack * y) + serial) * rack
    power /= 100
    power %= 10
    return int(power) - 5


for y in range(300):
    row = [calc(x + 1, y + 1, serial) for x in range(300)]
    grid.append(row)

score_1 = (0, 0, 0)
score_2 = (0, 0, 0, 0)

for y, row in enumerate(grid):
    for x, cell in enumerate(grid):
        for size in range(50): # 300 for safety, but this is a guess-optimisation (which works)
            if size == 0: continue
            if x + size > 300 or y + size > 300: continue

            the_score = sum([
                sum(row[x:x + size]) for row in grid[y:y + size]
            ])

            if size == 3 and the_score > score_1[0]:
                score_1 = (the_score, x + 1, y + 1)

            if the_score > score_2[0]:
                score_2 = (the_score, x + 1, y + 1, size)

print('pt1:', score_1[1:])
print('pt2:', score_2[1:])

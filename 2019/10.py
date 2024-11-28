#yuck

import sys
from numpy import arctan
from math import degrees

field = []

for line in sys.stdin:
    field.append([x for x in line.strip()])

def visualise(field, amt):
    field_i = [[str(i) for i, _ in enumerate(field[0])]] + field
    field_i = [[str(i - 1)] + x for i, x in enumerate(field_i)]
    def pad(x):
        y = x if x.strip() != "-1" else " "
        while len(y) < amt:
            y = " " + y
        return y

    for _ in field_i:
        print("".join([pad(x) for x in _]))

def find_hcd(x, y):
    # highest common denominator
    hcd = 1
    if x > y:
        small = y
    else:
        small = x
    for i in range(1, small + 1):
        if (x % i == 0) and (y % i == 0):
            hcd = i

    return hcd


def check_line_of_sight(x1, y1, x2, y2, field):
    if x1 == x2 and y1 == y2: return False

    dx = x2 - x1
    dy = y2 - y1
    adx = abs(dx)
    ady = abs(dy)

    hcd = find_hcd(adx, ady)

    # does the gradient intersect any other potential points?
    grad_intersects = ((dy == 0 or dx == 0) or (hcd > 1))
    if not grad_intersects:
        if field[y2][x2] == "V": return False
        if field[y2][x2] == "#":
            field[y2][x2] = "V"
            return True
        return False

    # check line of sight vertically
    if dx == 0:
        d = 1 if ady == dy else -1
        for y in range(y1 + d, y2 + d, d):
            if field[y][x1] == "V": return False
            if field[y][x1] == "#":
                field[y][x1] = "V"
                return True
        return False

    # check line of sight horizontally
    if dy == 0:
        d = 1 if adx == dx else -1
        for x in range(x1 + d, x2 + d, d):
            if field[y1][x] == "V": return False
            if field[y1][x] == "#":
                field[y1][x] = "V"
                return True
        return False

    # check all other lines of sight that have multiple points along them
    ndx = 1 if dx > 0 else -1
    ndx = int(ndx * adx / ady) if adx % ady == 0 else int(ndx * adx / hcd)
    ndy = 1 if dy > 0 else -1
    ndy = int(ndy * ady / adx) if ady % adx == 0 else int(ndy * ady / hcd)
    d = 0

    while True:
        try:
            x = int(x1 + (d + 1) * ndx)
            y = int(y1 + (d + 1) * ndy)
            if (x < 0 or y < 0): break # this one caused me a lot of problems because negative indexes wrap around in python
            if field[y][x] == "V": return False
            if field[y][x] == "#":
                field[y][x] = "V"
                return True
            d += 1
        except:
            break

    return False

def populate_field(x1, y1):
    global field
    field_copy = [row.copy() for row in field]
    for y2 in range(len(field)):
        for x2 in range(len(field[0])):
            check_line_of_sight(x1, y1, x2, y2, field_copy)
    field_copy[y1][x1] = "%"
    return field_copy

maximum = [0, 0, 0]
field_copy_ultimate = [row.copy() for row in field]
for y in range(len(field)):
    for x in range(len(field[0])):
        if field[y][x] == "#":
            new_field = populate_field(x, y)
            num_vis = [item for sublist in new_field for item in sublist].count("V")
            if num_vis > maximum[2]:
                maximum = [x, y, num_vis]
            field_copy_ultimate[y][x] = str(num_vis)

print("Part 1: Maximum is at coord:", maximum[0], maximum[1], "with number", maximum[2])
# visualise(field_copy_ultimate, 5)

# part 2
# do i dare manually calculate angles and compare them?
# yes

pt1_x = maximum[0]
pt1_y = maximum[1]

# print("Re-visualising with", pt1_x, pt1_y)
grid_with_best_location_marked = populate_field(pt1_x, pt1_y)

visualise(grid_with_best_location_marked, 3)

angles = []

for y, row in enumerate(grid_with_best_location_marked):
    for x, cell in enumerate(row):
        if cell != "V": continue
        # SOH CAH TOA #trollface
        a = y - pt1_y
        o = x - pt1_x
        if o == 0: angle = 0
        elif a == 0: angle = 90
        else: angle = (round((degrees(arctan(abs(o/a)))) * 100)) / 100

        if a < 0 and o > 0: pass
        elif a > 0 and o >= 0: angle = 180 - angle
        elif a > 0 and o < 0: angle += 180
        elif a < 0 and o < 0: angle = 360 - angle

        angles.append((x * 100 + y, angle))
        # print("(" + str(x) + ",", str(y) + ")", angle, "degrees;", "o:", o, "a:", a)

angles.sort(key=lambda tup: tup[1])
print(angles[199])

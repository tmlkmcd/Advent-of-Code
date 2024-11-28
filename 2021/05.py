import sys

lines = []
matrix = []

dimensions = 0

part = 2

for x in range(dimensions):
    row = []
    for y in range(dimensions):
        row.append(0)
    matrix.append(row)

def visualize():
    global matrix

    for r in matrix:
        my_str = ''

        for c in r:
            if c == 0: my_str += '.'
            else: my_str += str(c)
            my_str += ' '

def find_overlaps():
    global matrix
    total = 0

    for r in matrix:
        for c in r:
            if c > 1: total += 1

    return total

class Line:
    def __init__(self, txt):
        coord1, coord2 = txt.split(' -> ')
        x1, y1 = coord1.split(',')
        x2, y2 = coord2.split(',')

        self.x1 = int(x1)
        self.x2 = int(x2)
        self.y1 = int(y1)
        self.y2 = int(y2)

    def is_straight_line(self):
        return self.x1 == self.x2 or self.y1 == self.y2

    def get_coords(self):
        coords = []

        if self.x1 == self.x2:
            min_y = min(self.y1, self.y2)
            max_y = max(self.y1, self.y2)
            for y in range(min_y, max_y + 1):
                coords.append([self.x1, y])

        if self.y1 == self.y2:
            min_x = min(self.x1, self.x2)
            max_x = max(self.x1, self.x2)
            for x in range(min_x, max_x + 1):
                coords.append([x, self.y1])

        if (part == 2):
            if abs(self.y1 - self.y2) == abs(self.x1 - self.x2):
                min_x = min(self.x1, self.x2)
                max_x = max(self.x1, self.x2)

                min_y = min(self.y1, self.y2)
                max_y = max(self.y1, self.y2)

                d = max_x - min_x

                dx = (self.x2 - self.x1) / d
                dy = (self.y2 - self.y1) / d

                for x in range(abs(self.x1 - self.x2) + 1):
                    coords.append([int(self.x1 + x * dx), int(self.y1 + x * dy)])

        return coords


for line in sys.stdin:
    lines.append(Line(line.strip()))

for l in lines:
    if l.is_straight_line is False: continue

    for x, y in l.get_coords():
        matrix[y][x] += 1

# visualize()
print('part', part, find_overlaps())

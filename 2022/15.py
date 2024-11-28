import sys
import re
from intervaltree import IntervalTree

lines_in = [line.strip() for line in sys.stdin]
pt_1_row = 2000000
empty = dict()

def get_mh_distance(p1, p2):
    x, y = p1
    nx, ny = p2
    return abs(x - nx) + abs(y - ny)

class Sensor:
    def __init__(self, in_line):
        x, y, nx, ny = re.findall(r'-?\d+', in_line)
        x, y, nx, ny = [int(a) for a in [x, y, nx, ny]]
        self.position = (x, y)
        self.nearest_beacon = (nx, ny)
        self.mh = get_mh_distance(self.position, self.nearest_beacon)

    def get_empty(self, row):
        x, y = self.position
        mh = get_mh_distance(self.position, self.nearest_beacon)
        row_span = mh - (abs(row - y))
        if row not in empty: empty[row] = IntervalTree()
        if row_span < 0: return
        empty[row][x - row_span:x + row_span + 1] = ([x - row_span, x + row_span + 1])


sensors = [Sensor(l) for l in lines_in]
for s in sensors: s.get_empty(pt_1_row)
empty[pt_1_row].merge_overlaps(strict=False)
print('pt 1:', [a.length() - 1 for a in empty[pt_1_row]][0])

for y in range(2650000, 2700000): # shortcut for re-running, this would normally be 4e6
    for s in sensors: s.get_empty(y)
    empty[y].merge_overlaps(strict=False)
    if len(empty[y]) > 1:
        for a in empty[y][0]: print('pt 2:', a[1] * 4000000 + y)
        break

# print('pt 2:', 3316868 * 4000000 + 2686239)
import re
import sys
from math import floor

sys.setrecursionlimit(10 ** 6)

with open("inputs/2024/13.txt", "r") as f:
    content = f.read().split('\n\n')


def parse_claw_machine(line, part=1):
    a, b, prize = line.split('\n')

    [a, b] = [re.findall(r"^Button [AB]: X\+(\d+), Y\+(\d+)", x)[0] for x in [a, b]]
    prize = re.findall(r"^Prize: X=(\d+), Y=(\d+)", prize)[0]

    prize = [int(p) for p in prize]
    if part == 2:
        prize = [p + 10000000000000 for p in prize]

    return [int(aa) for aa in a], [int(bb) for bb in b], prize


def attempt(machine):
    px, py = machine[2][0], machine[2][1]

    ax, ay = machine[0][0], machine[0][1]
    bx, by = machine[1][0], machine[1][1]

    # by ( n * ax ) + by ( m * bx ) = by * px
    # bx ( n * ay ) + bx ( m * by ) = bx * py

    # by * ax * n - bx ( n * ay ) = by * px - bx * py
    # n ( by * ax - bx * ay ) = by * px - bx * py
    # n = ( by * px - bx * py ) / ( by * ax - bx * ay )

    # m = (by * px - by ( n * ax )) / by * bx

    n = (by * px - bx * py) / (by * ax - bx * ay)
    m = ((by * px) - (by * n * ax)) / (by * bx)

    if n % 1 == 0 and m % 1 == 0:
        return floor(3 * n + m)


pt1, pt2 = 0, 0
for machine in [parse_claw_machine(a) for a in content]:
    coins = attempt(machine)
    pt1 += coins if coins is not None else 0

for machine in [parse_claw_machine(a, 2) for a in content]:
    coins = attempt(machine)
    pt2 += coins if coins is not None else 0

print('part 1', pt1)
print('part 2', pt2)

import sys

opcode = []
puzzle_input = 2

part = 2

for line in sys.stdin:
    for num in [int(x) for x in line.split(",")]:
        opcode.append(num)

grid_size = 50 if part == 1 else 1600

grid = []
for _ in range(grid_size):
    grid.append(["." for _ in range(grid_size)])

def visualise():
    for row in grid:
        print("".join(row))

def run_program(intcode, inputs):
    l = intcode.copy() # 'l'ocal intcode
    for _ in range(200):
        l.append(0)
    p = 0
    input_p = 0

    relative_base = 0

    while True:
        if (l[p] % 100) == 99:
            print("done!")
            break

        o = l[p] % 10

        dummy_opcode = str(100000000 + l[p])

        mode_1 = dummy_opcode[-3]
        mode_2 = dummy_opcode[-4]
        mode_3 = dummy_opcode[-5]

        if mode_1 == "0": rpa = l[p + 1]
        elif mode_1 == "1": rpa = p + 1
        elif mode_1 == "2": rpa = l[p + 1] + relative_base

        if mode_2 == "0": rpb = l[p + 2]
        elif mode_2 == "1": rpb = p + 2
        elif mode_2 == "2": rpb = l[p + 2] + relative_base

        if mode_3 == "0": rpc = l[p + 3]
        elif mode_3 == "1": rpc = p + 3
        elif mode_3 == "2": rpc = l[p + 3] + relative_base

        if o == 1:
            l[rpc] = l[rpa] + l[rpb]
            p += 4
        elif o == 2:
            l[rpc] = l[rpa] * l[rpb]
            p += 4
        elif o == 3:
            l[rpa] = inputs[input_p]
            input_p += 1
            p += 2
        elif o == 4:
            # print("| output", l[rpa], "|")
            return l[rpa]
            # p += 2
        elif o == 5:
            if l[rpa] != 0: p = l[rpb]
            else: p += 3
        elif o == 6:
            if l[rpa] == 0: p = l[rpb]
            else: p += 3
        elif o == 7:
            if l[rpa] < l[rpb]: l[rpc] = 1
            else: l[rpc] = 0
            p += 4
        elif o == 8:
            if l[rpa] == l[rpb]: l[rpc] = 1
            else: l[rpc] = 0
            p += 4
        elif o == 9:
            relative_base += l[rpa]
            p += 2
        else: raise "oh noes"
    return l[0]

total = 0 # part 1 only
points = [] # part 2 only

for x in range(grid_size):
    if part == 2 and x < 600: continue
    if x % 100 == 0: print("x...", x)
    for y in range(grid_size):
        if part == 2 and y < 600: continue
        if x > 0.9 * y or y > 1.6 * x: continue
        o = run_program(opcode, [x, y])
        
        if o == 1:
            total += 1
            grid[x][y] = "#"
            if part == 2:
                points.append(",".join([str(n) for n in [x, y]]))

if part == 1:
    print(total)
    visualise()
    exit()

size_santa_ship = 100 # always 100 for the real answer but varying it here to test
esss = size_santa_ship - 1 # effective size of santa's ship
ans = [-1, -1]

l_p = len(points)
try:
    for _, p in enumerate(points):
        x, y = [int(n) for n in p.split(",")]
        np1 = ",".join([str(x + esss), str(y)])
        np2 = ",".join([str(x), str(y + esss)])
        if np1 in points and np2 in points:
            ans = [x, y]
            raise Exception("found it")
    print("Got to the end, no ans")
except:
    x, y = ans
    print(x * 10000 + y)

# debugging 

# for x, row in enumerate(grid):
#     for y, _ in enumerate(grid):
#         if x >= ans[0] and x < (ans[0] + size_santa_ship) and y >= ans[1] and y < (ans[1] + size_santa_ship):
#             grid[x][y] = "O"

# visualise()
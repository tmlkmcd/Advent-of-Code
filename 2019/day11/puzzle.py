import sys

opcode = []
part = 2

for line in sys.stdin:
    for num in [int(x) for x in line.split(",")]:
        opcode.append(num)


dim = 200
grid = [["." for _ in range(dim)] for _ in range(dim)]

painted = []
direction = "U"
turn = [
    {"U": "L", "L": "D", "D": "R", "R": "U"}, # turn left
    {"U": "R", "R": "D", "D": "L", "L": "U"}  # turn right
]
dx = {"U": 0, "R": 1, "D": 0, "L": -1}
dy = {"U": -1, "R": 0, "D": 1, "L": 0}
coords = [int(dim/2), int(dim/2)]
if part == 2:
    grid[coords[0]][coords[1]] = "#"
is_turning = False

def pad(x):
    y = str(x)
    while len(y) < 3:
        y = " " + y
    return y

def interpret_output(out):
    global is_turning
    global direction
    global coords
    if (is_turning):
        direction = turn[out][direction]
        coords = [coords[0] + dy[direction], coords[1] + dx[direction]]
        if coords[0] < 0 or coords[1] < 0:
            raise "negative"
    else:
        grid[coords[0]][coords[1]] = "." if out == 0 else "#"
        this_coord = pad(coords[0]) + pad(coords[1])
        if this_coord not in painted: painted.append(this_coord)

    is_turning = not is_turning


def run_program(intcode):
    l = intcode.copy() # 'l'ocal intcode
    for _ in range(200):
        l.append(0)
    p = 0

    relative_base = 0

    while True:
        if (l[p] % 100) == 99:
            print("done!")
            while(l[len(l) - 1] == 0): l.pop()
            print(l)
            break

        # print("------------------------------------------")

        o = l[p] % 10 # opcode

        # if o < 3 or o == 7 or o == 8: print(l[p:p+4])
        # elif (o == 5 or o == 6): print(l[p:p+3])
        # else: print(l[p:p+2])

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

        m = max(rpa, rpb, rpc)
        while (m > len(l) - 1):
            l.append(0)

        if o == 1:
            l[rpc] = l[rpa] + l[rpb]
            # print("pointer", rpc, "setting to", l[rpa], "plus", l[rpb])
            p += 4
        elif o == 2:
            l[rpc] = l[rpa] * l[rpb]
            # print("pointer", rpc, "setting to", l[rpa], "times", l[rpb])
            p += 4
        elif o == 3:
            # print("INPUT!!?!?!?!?", rpa)
            l[rpa] = 1 if grid[coords[0]][coords[1]] == "#" else 0
            p += 2
        elif o == 4:
            # print("============")
            # print("| output", l[rpa], "|")
            interpret_output(l[rpa])
            # print("============")
            p += 2
        elif o == 5:
            if l[rpa] != 0: p = l[rpb]
            else: p += 3
            # print("pointer currently", p, "if", l[rpa], "NOT 0 then setting to", l[rpb])
        elif o == 6:
            if l[rpa] == 0: p = l[rpb]
            else: p += 3
            # print("pointer currently", p, "if", l[rpa], "IS 0 then setting to", l[rpb])
        elif o == 7:
            if l[rpa] < l[rpb]: l[rpc] = 1
            else: l[rpc] = 0
            p += 4
            # print("target position is", rpc, "if", l[rpa], "LESS THAN", l[rpb], "setting target to 1")
        elif o == 8:
            if l[rpa] == l[rpb]: l[rpc] = 1
            else: l[rpc] = 0
            p += 4
            # print("target position is", rpc, "if", l[rpa], "EQUAL TO", l[rpb], "setting target to 1")
        elif o == 9:
            relative_base += l[rpa]
            p += 2
            # print("adjusting relative base by ", l[rpa], ", it is now", relative_base)
        else: raise "oh noes"
    return l[0]

run_program(opcode)

for row in grid:
    print("".join(row))

print(len(painted))
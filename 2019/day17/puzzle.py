import sys

opcode = []
part = 2

for line in sys.stdin:
    for num in [int(x) for x in line.split(",")]:
        opcode.append(num)

grid = [[]]

def add_char(charcode):
    if charcode == 10:
        grid.append([])
        return
    grid[-1].append(chr(charcode))
    
def visualise(grid):
    for row in grid:
        print("".join(row))

def str_to_ascii(inp):
    if len(inp) == 0: return []
    al = []
    for char in inp:
        al.append(ord(char))
    al.append(10)
    return al


puzzle_inputs = [
    "A,B,A,C,B,C,B,C,A,C",
    "L,10,R,12,R,12",
    "R,6,R,10,L,10",
    "R,10,L,10,L,12,R,6",
    "n"
]

puzzle_inputs = str_to_ascii(puzzle_inputs[0]) + str_to_ascii(puzzle_inputs[1]) + str_to_ascii(puzzle_inputs[2]) + str_to_ascii(puzzle_inputs[3]) + str_to_ascii(puzzle_inputs[4])

def run_program(intcode):
    l = intcode.copy() # 'l'ocal intcode
    for _ in range(2000):
        l.append(0)
    p = 0

    relative_base = 0
    i = -1

    while True:
        if (l[p] % 100) == 99:
            print("done!")
            # print(l)
            break

        o = l[p] % 10 # opcode

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
            i += 1
            l[rpa] = puzzle_inputs[i]
            p += 2
        elif o == 4:
            # print("============")
            print("| output", l[rpa], "|")
            # print("============")
            add_char(l[rpa])
            p += 2
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

if part == 1:
    run_program(opcode)
    starting_x, starting_y = -1, -1

    def check_is_intersection(x, y):
        try:
            return grid[y][x] == "#" and grid [y-1][x] == "#" and grid [y+1][x] == "#" and grid [y][x-1] == "#" and grid [y][x+1] == "#"
        except:
            return False

    total_param = 0

    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if check_is_intersection(x, y):
                total_param += x * y

    print(total_param)
    exit()

opcode[0] = 2
run_program(opcode)
visualise(grid)
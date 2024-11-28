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
    try:
        grid[-1].append(chr(charcode))
    except:
        print("Part", part, "answer:", charcode)
    
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

if part == 1:
    puzzle_inputs = [
        "OR D J",
        "NOT T T",
        "NOT C T",
        "AND T J",
        "NOT B T",
        "OR T J",
        "NOT A T",
        "OR T J",
        "AND D J",
        "WALK"
    ]
else:
    puzzle_inputs = [
        "OR D J",
        "NOT T T",
        "NOT C T",
        "AND T J",
        "NOT B T",
        "OR T J",
        "NOT A T",
        "OR T J",
        "AND D J",
        "OR H T",
        "AND T J",
        "RUN"
    ]

inp = []
for pi in puzzle_inputs: inp = inp + str_to_ascii(pi)

def run_program(intcode):
    l = intcode.copy() # 'l'ocal intcode
    for _ in range(200):
        l.append(0)
    p = 0
    i = -1

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
            i += 1
            l[rpa] = inp[i]
            p += 2
        elif o == 4:
            # print("============")
            # print("| output", l[rpa], "|")
            add_char(l[rpa])
            # print("============")
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

run_program(opcode)

visualise(grid)
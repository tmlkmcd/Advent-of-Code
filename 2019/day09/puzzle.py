import sys

opcode = []
puzzle_input = 2

for line in sys.stdin:
    for num in [int(x) for x in line.split(",")]:
        opcode.append(num)

def run_program(intcode):
    l = intcode.copy() # 'l'ocal intcode
    for _ in range(200):
        l.append(0)
    p = 0

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
            l[rpa] = puzzle_input
            p += 2
        elif o == 4:
            print("============")
            print("| output", l[rpa], "|")
            print("============")
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
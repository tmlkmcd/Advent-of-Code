# messy. much debugging lines in place because i had trouble actually interpreting the instructions correctly.

import sys

opcode = []
puzzle_input = 5

for line in sys.stdin:
    for num in [int(x) for x in line.split(",")]:
        opcode.append(num)

def run_program(intcode):
    l = intcode.copy() # 'l'ocal intcode
    p = 0

    while True:
        if (l[p] % 100) == 99:
            print("done!")
            print(l)
            break

        # print("------------------------------------------")

        o = l[p] % 10 # opcode
        if (o > 10000):
            raise "replaced in immediate mode, something went wrong"

        # if o < 3 or o == 7 or o == 8: print(l[p:p+4])
        # elif (o == 5 or o == 6): print(l[p:p+3])
        # else: print(l[p:p+2])

        dummy_opcode = str(1000000 + l[p])
        a, b, c = 0, 0, 0

        if dummy_opcode[-3] == "0": a = l[l[p + 1]]
        else: a = l[p + 1]
        
        # print("first param:", a)
        if (o < 3 or o > 4):
            if dummy_opcode[-4] == "0": b = l[l[p + 2]]
            else: b = l[p + 2]

            # print("second param:", b)
            if (o < 3 or o > 6):
                c = l[p + 3]
                # print("third param:", c)

        if o == 1:
            l[c] = a + b
            # print("pointer", c, "setting to", a, "plus", b)
            p += 4
        elif o == 2:
            l[c] = a * b
            # print("pointer", c, "setting to", a, "times", b)
            p += 4
        elif o == 3:
            l[l[p + 1]] = puzzle_input
            # print("setting", l[p + 1], " to ", puzzle_input)
            p += 2
        elif o == 4:
            print("============")
            print("| output", a, "|")
            print("============")
            p += 2
        elif o == 5:
            if a != 0: p = b
            else: p += 3
            # print("pointer currently", p, "if", a, "NOT 0 then setting to", b)
            # break
        elif o == 6:
            if a == 0: p = b
            else: p += 3
            # print("pointer currently", p, "if", a, "IS 0 then setting to", b)
        elif o == 7:
            if a < b: l[c] = 1
            else: l[c] = 0
            p += 4
            # print("target position is", c, "if", a, "LESS THAN", b, "setting target to 1")
        elif o == 8:
            if a == b: l[c] = 1
            else: l[c] = 0
            p += 4
            # print("target position is", c, "if", a, "EQUAL TO", b, "setting target to 1")
        else: raise "oh noes"
    return l[0]

run_program(opcode)
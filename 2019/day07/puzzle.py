import sys
from itertools import permutations

opcode = []
puzzle_input = 5

part = 2

for line in sys.stdin:
    for num in [int(x) for x in line.split(",")]:
        opcode.append(num)

def run_program(intcode, phase, out_of_last, pointer=0):
    l = intcode.copy() # 'l'ocal intcode
    p = pointer
    output = out_of_last
    num_inputs = 0
    inputs = [phase, out_of_last]

    while True:
        if (l[p] % 100) == 99:
            # print("done! output:", output)
            if part == 1:
                return output
            else:
                return output, l, p, True
            break

        o = l[p] % 10 # opcode
        if (o > 10000):
            raise "replaced in immediate mode, something went wrong"

        dummy_opcode = str(1000000 + l[p])
        a, b, c = 0, 0, 0

        if dummy_opcode[-3] == "0": a = l[l[p + 1]]
        else: a = l[p + 1]

        if (o < 3 or o > 4):
            if dummy_opcode[-4] == "0": b = l[l[p + 2]]
            else: b = l[p + 2]

            if (o < 3 or o > 6):
                c = l[p + 3]

        if o == 1:
            l[c] = a + b
            p += 4
        elif o == 2:
            l[c] = a * b
            p += 4
        elif o == 3:
            try:
                ii = inputs[num_inputs]
            except:
                ii = output
            l[l[p + 1]] = ii
            num_inputs += 1
            p += 2
        elif o == 4:
            output = a
            p += 2
            if part == 2:
                # print("returned early")
                return output, l, p, False
        elif o == 5:
            if a != 0: p = b
            else: p += 3
        elif o == 6:
            if a == 0: p = b
            else: p += 3
        elif o == 7:
            if a < b: l[c] = 1
            else: l[c] = 0
            p += 4
        elif o == 8:
            if a == b: l[c] = 1
            else: l[c] = 0
            p += 4
        else: raise "oh noes"
    return l[0]

# part 1
if part == 1:
    outputs = []

    for guess in list(permutations([0, 1, 2, 3, 4], 5)):
        output = 0
        for i, _ in enumerate(["A", "B", "C", "D", "E"]):
            output = run_program(opcode, guess[i], output)
            outputs.append(output)

    print(max(outputs))


# part 2
if part == 2:
    outputs = []

    for guess in list(permutations([5, 6, 7, 8, 9], 5)):
        intcodes = {
            "A": [opcode, 0],
            "B": [opcode, 0],
            "C": [opcode, 0],
            "D": [opcode, 0],
            "E": [opcode, 0]
        }
        output = 0
        current_perm = 0
        amps = ["A", "B", "C", "D", "E"]
        while True:
            amp = amps[current_perm % len(amps)]
            inp = guess[current_perm] if current_perm < len(guess) else output 
            # print(amp, inp, output)
            output, new_opcode, p, finished = run_program(intcodes[amp][0], inp, output, intcodes[amp][1])
            if not finished:
                intcodes[amp] = [new_opcode, p]
            current_perm += 1

            if finished and amp == "E":
                outputs.append(output)
                # print(output)
                break       

    print(max(outputs))
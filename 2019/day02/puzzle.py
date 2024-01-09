import sys

intcode = None

part = 2

for line in sys.stdin:
    intcode = line

intcode = [int(num) for num in intcode.split(",")]

def run_program(intcode, noun, verb):
    intcode_l = intcode.copy()
    intcode_l[1] = noun
    intcode_l[2] = verb
    position = 0

    while True:
        if (intcode_l[position]) == 99:
            break

        first = intcode_l[intcode_l[position + 1]]
        second = intcode_l[intcode_l[position + 2]]
        replace_position = intcode_l[position + 3]

        if (intcode_l[position]) == 1:
            intcode_l[replace_position] = first + second
        elif (intcode_l[position]) == 2:
            intcode_l[replace_position] = first * second
        else:
            raise "oh noes"
        position += 4
    return intcode_l[0]


if (part == 1):
    print(run_program(intcode, 12, 2))

if (part == 2):
    for noun in range(99 + 1):
        for verb in range(99 + 1):
            output = run_program(intcode, noun, verb)
            if (output == 19690720):
                print(noun, verb)
                break

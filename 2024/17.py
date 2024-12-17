import re
import math

with open("inputs/2024/17.txt", "r") as f:
    content = f.read().split('\n\n')

[a, b, c] = [int(_a) for _a in re.findall(r"(\d+)", content[0])]
program, pt2_found = [int(_a) for _a in content[1].split(' ')[1].split(',')], False


class Computer:
    def __init__(self, a, b, c, program):
        self.a = a
        self.b = b
        self.c = c
        self.instruction_pointer = 0
        self.program = program
        self.output = []

    def get_combo_operand(self, operand):
        if 0 <= operand <= 3:
            return operand
        elif operand == 4:
            return self.a
        elif operand == 5:
            return self.b
        elif operand == 6:
            return self.c

    def perform_func(self, opcode, operand):
        if opcode == 0 or opcode == 6 or opcode == 7:
            numerator = self.a
            denominator = math.pow(2, self.get_combo_operand(operand))
            if opcode == 0:
                self.a = numerator // denominator
            elif opcode == 6:
                self.b = numerator // denominator
            elif opcode == 7:
                self.c = numerator // denominator
        elif opcode == 1:
            self.b ^= operand
        elif opcode == 2:
            self.b = int(self.get_combo_operand(operand)) % 8
        elif opcode == 3:
            if self.a != 0:
                self.instruction_pointer = operand
                return
        elif opcode == 4:
            self.b = int(self.b) ^ int(self.c)
        elif opcode == 5:
            self.output.append(int(self.get_combo_operand(operand) % 8))

        self.instruction_pointer += 2

    def run(self):
        while self.instruction_pointer < len(self.program):
            args = program[self.instruction_pointer:self.instruction_pointer + 2]
            self.perform_func(*args)


def scan(so_far):
    global pt2_found
    if pt2_found: return
    s = 0
    for n in reversed(so_far):
        s += n
        s *= 8

    for nn in range(8):
        a = s + nn
        c_ = Computer(a, 0, 0, program)
        c_.run()

        if c_.output == program[-len(c_.output):]:
            if len(c_.output) == len(program):
                print('part 2', a)
                pt2_found = a
                return
            _so_far = [nn] + so_far
            scan(_so_far)


computer = Computer(a, b, c, program)
computer.run()
print('part 1', ','.join([str(int(a)) for a in computer.output]))
scan([])

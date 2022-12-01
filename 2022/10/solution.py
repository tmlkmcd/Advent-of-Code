import sys

lines_in = [line.strip() for line in sys.stdin]

score = 0
cycle = 0
x = 1

display = []

for line in lines_in:
    instruction = line.split(' ')
    if instruction[0] == 'noop':
        if abs(cycle % 40 - x) <= 1: display.append('#')
        else: display.append('.')
        cycle += 1

        if (cycle - 20) % 40 == 0: score += (cycle * x)
    else:
        if abs(((cycle) % 40) - x) <= 1: display.append('#')
        else: display.append('.')

        if abs(((cycle + 1) % 40) - x) <= 1: display.append('#')
        else: display.append('.')

        cycle += 2
        if (cycle - 21) % 40 == 0: score += ((cycle - 1) * x)
        elif (cycle - 20) % 40 == 0: score += (cycle * x)
        x += int(instruction[1])

print('pt1', score)

for r in range(6):
    print(''.join(display[r * 40: (r + 1) * 40]))
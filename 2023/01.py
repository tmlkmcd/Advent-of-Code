import sys

lines_in = [line.strip() for line in sys.stdin]
total, total2 = 0, 0

for line in lines_in:
    for d in line:
        if d.isdigit():
            total += int(d) * 10
            break
    for d in reversed(line):
        if d.isdigit():
            total += int(d)
            break

print('part 1', total)

digits = {
    '1': 'one',
    '2': 'two',
    '3': 'three',
    '4': 'four',
    '5': 'five',
    '6': 'six',
    '7': 'seven',
    '8': 'eight',
    '9': 'nine'
}


def scan(line, direction='l'):
    r = range(len(line))
    for index in r if direction == 'l' else reversed(r):
        for n in digits:
            if line[index] == n or line[index:index+len(digits[n])] == digits[n]:
                return int(n)


for line in lines_in:
    total2 += scan(line) * 10 + scan(line, 'r')

print('part 2', total2)

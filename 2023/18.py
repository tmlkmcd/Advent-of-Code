import sys
lines_in = [line.strip() for line in sys.stdin]

def parse(line, part=1):
    direction, amt, hex = line.split(' ')

    if part == 1: return (direction, int(amt))
    else:
        if hex[7] == '0': direction = 'R'
        elif hex[7] == '1': direction = 'D'
        elif hex[7] == '2': direction = 'L'
        elif hex[7] == '3': direction = 'U'
        return (direction, int(hex[2:7], 16))

def calc_area(ins):
    area, y = 0, 0
    for instr in ins:
        direction, amt = instr
        if direction == 'R': area += y * amt
        elif direction == 'L': area -= y * amt
        elif direction == 'U': y += amt
        elif direction == 'D': y -= amt
    return area

def calc_boundary(ins):
    return sum([a for _, a in ins])

def solve(part=1):
    ins = [parse(line, part) for line in lines_in]
    area = calc_area(ins)
    boundary = calc_boundary(ins)
    return area + (boundary // 2) + 1

for part in [1, 2]:
    print('part {p}: {a}'.format(p=part,a=solve(part)))


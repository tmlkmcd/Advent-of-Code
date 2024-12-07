with open("inputs/2024/07.txt", "r") as f:
    content = f.read().split('\n')


def parse_line(line):
    result, _operands = line.split(': ')
    return [int(result), [int(operand) for operand in _operands.split(' ')]]


def try_operation(_target, current, remaining, part=1):
    if len(remaining) == 0: return current == _target
    if current > _target: return False

    try_next = [current + remaining[0], current * remaining[0]]
    if part == 2: try_next.append(int(str(current) + str(remaining[0])))

    return any(try_operation(_target, _next, remaining[1:], part) for _next in try_next)


calibrations = [parse_line(line) for line in content]
pt1, pt2 = 0, 0

for i, line in enumerate(calibrations):
    if i % 20 == 0: print(i, '/', len(calibrations))
    target, operands = line
    if try_operation(target, operands[0], operands[1:]): pt1 += target
    if try_operation(target, operands[0], operands[1:], 2): pt2 += target

print('part 1:', pt1)
print('part 2:', pt2)

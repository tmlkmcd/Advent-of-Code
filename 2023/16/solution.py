import sys

lines_in = [line.strip() for line in sys.stdin]
grid = [list(line) for line in lines_in]
max_y, max_x = len(grid), len(grid[0])

def step(current, energised, later):
    global max_y, max_x
    y, x, direction = current

    if direction == 'u': y -= 1
    elif direction == 'd': y += 1
    elif direction == 'l': x -= 1
    elif direction == 'r': x += 1

    if y >= max_y or y < 0 or x >= max_x or x < 0:
        return

    if (y, x) in energised and direction in energised[(y, x)]: return

    if (y, x) in energised: energised[(y, x)].append(direction)
    else: energised[(y, x)] = [direction]

    n = grid[y][x]
    if n == '.':
        step((y, x, direction), energised, later)
    if n == '\\':
        if direction == 'r': step((y, x, 'd'), energised, later)
        if direction == 'u': step((y, x, 'l'), energised, later)
        if direction == 'd': step((y, x, 'r'), energised, later)
        if direction == 'l': step((y, x, 'u'), energised, later)
    if n == '/':
        if direction == 'r': step((y, x, 'u'), energised, later)
        if direction == 'u': step((y, x, 'r'), energised, later)
        if direction == 'd': step((y, x, 'l'), energised, later)
        if direction == 'l': step((y, x, 'd'), energised, later)
    if n == '-':
        if direction in 'lr':
            step((y, x, direction), energised, later)
        else:
            later.append((y, x, 'l'))
            step((y, x, 'r'), energised, later)
    if n == '|':
        if direction in 'ud':
            step((y, x, direction), energised, later)
        else:
            later.append((y, x, 'u'))
            step((y, x, 'd'), energised, later)

def find_energised(start):
    energised, later = {}, []
    step(start, energised, later)
    while len(later) > 0: step(later.pop(0), energised, later)
    return len([k for k in energised])


print('part 1', find_energised((0, -1, 'r')))

pt2_highest = -1

for sy in range(max_y):
    pt2_highest = max(pt2_highest, find_energised((sy, -1, 'r')))
    pt2_highest = max(pt2_highest, find_energised((sy, max_x, 'l')))
for sx in range(max_x):
    pt2_highest = max(pt2_highest, find_energised((-1, sx, 'd')))
    pt2_highest = max(pt2_highest, find_energised((max_x, sx, 'u')))

print('part 2', pt2_highest)

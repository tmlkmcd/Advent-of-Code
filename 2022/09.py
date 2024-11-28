import sys

lines_in = [line.strip().split(' ') for line in sys.stdin]

t_visited_pt1 = dict()
t_visited_pt2 = dict()
ropes = [(0, 0) for _ in range(10)]

def move_tail(index):
    global ropes
    x, y = ropes[index]
    xx, yy = ropes[index + 1]
    _direction = []

    if x - xx > 1: _direction.append('R')
    if x - xx < -1: _direction.append('L')
    if y - yy > 1: _direction.append('U')
    if y - yy < -1: _direction.append('D')
    if len(_direction) == 0: return

    m_x, m_y = x, y
    if 'U' in _direction: m_y -= 1
    if 'L' in _direction: m_x += 1
    if 'D' in _direction: m_y += 1
    if 'R' in _direction: m_x -= 1
    ropes[index + 1] = (m_x, m_y)

    # index + 1 == len(ropes) - 1 for both parts 1 and 2
    if index == 0: t_visited_pt1[ropes[index + 1]] = True
    if index == len(ropes) - 2: t_visited_pt2[ropes[index + 1]] = True

def move_head(direction):
    global ropes
    x, y = ropes[0]
    match direction:
        case 'U': y += 1
        case 'L': x -= 1
        case 'D': y -= 1
        case 'R': x += 1
    ropes[0] = (x, y)
    for r in range(len(ropes) - 1): move_tail(r)

def visualise(movement):
    global ropes
    grid = []
    for _ in range(21):
        grid.append(['.' for _ in range(20)])

    for n, rope in enumerate(ropes):
        x, y = rope
        grid[y][x] = 'H' if n == 0 else str(n)

    print(movement)
    for row in reversed(grid): print(''.join(row))
    print('===============')

t_visited_pt1[(0, 0)] = True
t_visited_pt2[(0, 0)] = True

for movement in lines_in:
    direction, num = movement
    for _ in range(int(num)):
        move_head(direction)
    # visualise(movement)

print(f'part 1: {len(t_visited_pt1.values())}; part 2: {len(t_visited_pt2.values())}')

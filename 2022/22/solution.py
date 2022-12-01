import sys
import re

lines_in = [line.replace('\n', '') for line in sys.stdin]
maze, maze_unpadded = [], [list(l) for l in lines_in[:-2]]
max_row_len = max([len(l) for l in maze_unpadded])

for row in maze_unpadded:
    while len(row) < max_row_len: row += ' '
    maze.append(row)

instructions, instructions_line = [], lines_in[-1]
steps = re.findall(r'\d+', instructions_line)
turns = re.findall(r'[RL]', instructions_line)

directions = ['R', 'D', 'L', 'U']
movements = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}
indicator = {'R': '>', 'D': 'V', 'L': '<', 'U': '^'}

for n in range(len(steps)):
    instructions.append(int(steps[n]))
    if n < len(steps) - 1: instructions.append(turns[n])

start = (0, maze[0].index('.'))

position = start
position_2 = start
facing = 'R'
facing_2 = 'R'


def travel(coord, direction):
    y, x = coord
    dy, dx = movements[direction]
    return y + dy, x + dx


def visualize(position, travelled):
    global maze
    print('======')
    for n, row in enumerate(maze):
        v_row = []
        for m, a in enumerate(row):
            if (n, m) == position:
                v_row.append('!')
            else:
                flag = False
                for t, b in reversed(travelled):
                    if (n, m) == t:
                        v_row.append(indicator[b])
                        flag = True
                        break
                if not flag: v_row.append(a)
        print(''.join(v_row))


def turn(facing, direction):
    current = directions.index(facing)
    return directions[(current + (1 if direction == 'R' else -1)) % len(directions)]


def step(amt, s_position):
    l_position = s_position
    for _ in range(amt):
        yy, xx = travel(l_position, facing)
        if yy > len(maze) - 1 or (facing == 'D' and maze[yy][xx] == ' '):
            yy = 0
            while maze[yy][xx] == ' ': yy += 1
        if yy < 0 or (facing == 'U' and maze[yy][xx] == ' '):
            yy = len(maze) - 1
            while maze[yy][xx] == ' ': yy -= 1
        if xx > len(maze[yy]) - 1 or (facing == 'R' and maze[yy][xx] == ' '):
            xx = 0
            while maze[yy][xx] == ' ': xx += 1
        if xx < 0 or (facing == 'L' and maze[yy][xx] == ' '):
            xx = len(maze[yy]) - 1
            while maze[yy][xx] == ' ': xx -= 1
        if maze[yy][xx] == '#':
            return l_position
        else:
            l_position = (yy, xx)
    return l_position


def get_face(c_position):
    y, x = c_position
    if 0 <= y < 50:
        if 50 <= x < 100: return 'a'
        if 100 <= x < 150: return 'b'
    if 50 <= y < 100 and 50 <= x < 100: return 'c'
    if 100 <= y < 150:
        if 0 <= x < 50: return 'd'
        if 0 <= x < 100: return 'e'
    if 0 <= y < 200 and 0 <= x < 50: return 'f'
    return 'oob'


def change_face(pos, face, d):
    if face == 'a':
        match d:
            case 'R': return travel(pos, d), 'b', 'R'
            case 'D': return travel(pos, d), 'c', 'D'
            case 'L': return (149 - pos[0], 0), 'd', 'R'
            case 'U': return (100 + pos[1], 0), 'f', 'R'
    if face == 'b':
        match d:
            case 'R': return (149 - pos[0], 99), 'e', 'L'
            case 'D': return (pos[1] - 50, 99), 'c', 'L'
            case 'L': return travel(pos, d), 'a', 'L'
            case 'U': return (199, pos[1] - 100), 'f', 'U'
    if face == 'c':
        match d:
            case 'R': return (49, pos[0] + 50), 'b', 'U'
            case 'D': return travel(pos, d), 'e', 'D'
            case 'L': return (100, pos[0] - 50), 'd', 'D'
            case 'U': return travel(pos, d), 'a', 'U'
    if face == 'd':
        match d:
            case 'R': return travel(pos, d), 'e', 'R'
            case 'D': return travel(pos, d), 'f', 'D'
            case 'L': return (149 - pos[0], 50), 'a', 'R'
            case 'U': return (pos[1] + 50, 50), 'c', 'R'
    if face == 'e':
        match d:
            case 'R': return (149 - pos[0], 149), 'b', 'L'
            case 'D': return (pos[1] + 100, 49), 'f', 'L'
            case 'L': return travel(pos, d), 'd', 'L'
            case 'U': return travel(pos, d), 'c', 'U'
    if face == 'f':
        match d:
            case 'R': return (149, pos[0] - 100), 'e', 'U'
            case 'D': return (0, pos[1] + 100), 'b', 'D'
            case 'L': return (0, pos[0] - 100), 'a', 'D'
            case 'U': return travel(pos, d), 'd', 'U'
    print(face, d)


def step_2(amt, s_position, facing, travelled):
    l_position = s_position
    l_facing = facing
    for _ in range(amt):
        travelled.append((l_position, l_facing))
        face = get_face(l_position)
        n_position = travel(l_position, l_facing)
        n_facing = l_facing
        if get_face(n_position) != face:
            n_position, l_face, n_facing = change_face(l_position, face, l_facing)
        yy, xx = n_position
        if maze[yy][xx] == '#':
            return l_position, l_facing
        else:
            l_position = n_position
            l_facing = n_facing
    return l_position, l_facing


travelled = []

for instruction in instructions:
    if isinstance(instruction, int):
        position = step(instruction, position)
        position_2, facing_2 = step_2(instruction, position_2, facing_2, travelled)
    else:
        facing = turn(facing, instruction)
        facing_2 = turn(facing_2, instruction)

visualize(position_2, travelled)

y, x = position
y2, x2 = position_2
pt_1 = ((y + 1) * 1000) + ((x + 1) * 4) + directions.index(facing)
pt_2 = ((y2 + 1) * 1000) + ((x2 + 1) * 4) + directions.index(facing_2)

print(f'part 1: {pt_1}, part 2: {pt_2}')

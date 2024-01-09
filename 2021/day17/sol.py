import sys

trench = None

for line in sys.stdin: trench = line.strip()

_, dims = trench.split(': ')
x, y = dims.split(', ')

def parse_number(s):
    _, nn = s.split('=')
    limits = [int(nnn) for nnn in nn.split('..')]
    limits.sort()
    return limits

min_x, max_x = parse_number(x)
min_y, max_y = parse_number(y)

def is_in_target_zone(position):
    x, y = position
    return min_x <= x <= max_x and min_y <= y <= max_y

def has_cleared_target_zone(position):
    x, y = position
    return x > max_x or y < min_y

def will_reach_target_zone_x(velocity):
    global min_x
    global max_x

    px = 0
    dx, _ = velocity

    while dx > 0:
        px += dx
        if min_x <= px <= max_x: return True
        if px > max_x: return False
        dx -= 1

    return False






def visualize(trajectory):
    global min_x
    global max_x
    global min_y
    global max_y

    min_grid_x = min(min([x for x, y in trajectory]), min_x)
    max_grid_x = max(max([x for x, y in trajectory]), max_x)
    min_grid_y = min(min([y for x, y in trajectory]), min_y)
    max_grid_y = max(max([y for x, y in trajectory]), max_y)

    grid = [['.' for x in range(max_grid_x - min_grid_x + 1)] for y in range(max_grid_y - min_grid_y + 1)]

    for y in range(min_y - min_grid_y, max_y - min_grid_y):
        for x in range(min_x - min_grid_x, max_x - min_grid_x):
            grid[y][x] = 'T'

    for xx, yy in trajectory:
        try: grid[yy - min_grid_y][xx - min_grid_x] = 'X'
        except: print(yy - min_grid_y, xx - min_grid_x)

    grid.reverse()

    for y in grid: print(''.join(y))


def launch(velocity):
    if not will_reach_target_zone_x(velocity): return False, [], -1

    position = [0, 0]
    n_velocity = velocity
    highest_y = -1e9

    trajectory = []

    while True:
        position = [position[0] + n_velocity[0], position[1] + n_velocity[1]]
        trajectory.append(position)
        if position[1] > highest_y: highest_y = position[1]
        n_velocity[0] += (1 if n_velocity[0] < 0 else (-1 if n_velocity[0] > 0 else 0))
        n_velocity[1] -= 1
        if is_in_target_zone(position):
            return True, trajectory, highest_y
        if has_cleared_target_zone(position):
            return False, trajectory, -1


h_y = -1e9
num_successes = 0

for s_y in range(-1500, 1500): # big fat guess, might need to be larger ranges for different inputs
    for s_x in range(-150, 150):
        success, trajectory, highest_y = launch([s_x, s_y])

        if not success: continue
        num_successes += 1
        if highest_y > h_y: h_y = highest_y

print('part 1', h_y)
print('part 2', num_successes)


